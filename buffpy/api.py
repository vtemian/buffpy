import json
import urllib.parse
from typing import Callable

from rauth import OAuth2Session, OAuth2Service

from .exceptions import BuffpyRestException
from .response import ResponseObject


BASE_URL = "https://api.bufferapp.com/1/{}"
PATHS = {
    "INFO": "info/configuration.json"
}
AUTHORIZE_URL = "https://bufferapp.com/oauth2/authorize"
ACCESS_TOKEN = "https://api.bufferapp.com/1/oauth2/token.json"

DEFAULT_PARSER = json.loads
OAUTH_SERVICE_NAME = "buffer"


class API:
    """
    Small and clean class that embrace all basic
    operations with the buffer app
    """

    def __init__(self, client_id, client_secret, access_token=None):
        self.session = OAuth2Session(client_id=client_id,
                                     client_secret=client_secret,
                                     access_token=access_token)

    @property
    def access_token(self):
        return self.session.access_token

    @access_token.setter
    def access_token(self, value: str):
        self.session.access_token = value

    def get(self, url: str, parser: Callable = DEFAULT_PARSER) -> str:
        if not self.session.access_token:
            raise ValueError("Please set an access token first!")

        response = self.session.get(url=BASE_URL.format(url))

        if response.ok:
            return parser(response.content)

        self._handleResponseError(url, response, parser)

    def post(self, url: str, parser: Callable = DEFAULT_PARSER, **params) -> str:
        if not self.session.access_token:
            raise ValueError("Please set an access token first!")

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = self.session.post(url=BASE_URL.format(url), headers=headers,
                                     **params)

        if response.ok:
            return parser(response.content)

        self._handleResponseError(url, response, parser)

    def _handleResponseError(self, url: str, response, parser: Callable):
        http_code = response.status_code

        error_code, description = None, response.content

        try:
            parsed = parser(response.content)
            error_code, description = (parsed["error_unquotecode"],
                                       parsed["message"])
        except: # noqa
            pass

        raise BuffpyRestException(url, http_code, error_code, description)

    @property
    def info(self):
        """
        Returns an object with the current configuration that Buffer is using,
        including supported services, their icons and the varying limits of
        character and schedules.

        The services keys map directly to those on profiles and updates so that
        you can easily show the correct icon or calculate the correct character
        length for an update.
        """

        return ResponseObject(self.get(url=PATHS["INFO"]))


class AuthService(object):

    def __init__(self, client_id, client_secret, redirect_uri):
        self.outh_service = OAuth2Service(client_id=client_id,
                                          client_secret=client_secret,
                                          name=OAUTH_SERVICE_NAME,
                                          authorize_url=AUTHORIZE_URL,
                                          access_token_url=ACCESS_TOKEN,
                                          base_url=BASE_URL.format(""))
        self.redirect_uri = redirect_uri

    def create_session(self, access_token: str = None):
        return self.outh_service.get_session(access_token)

    def get_access_token(self, auth_code: str):
        data = {
            "code": urllib.parse.unquote(auth_code),
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri
        }

        return self.outh_service.get_access_token(data=data,
                                                  decoder=json.loads)

    @property
    def authorize_url(self):
        return self.outh_service.get_authorize_url(response_type="code",
                                                   redirect_uri=self.redirect_uri)
