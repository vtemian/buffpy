import sys


class BuffpyException(Exception):
    pass


class BuffpyRestException(BuffpyException):
    """
    Represents any 4xx or 5xx exceptions from the Buffer API
    Reference: https://bufferapp.com/developers/api/errors

    Some ideas borrowed from Twilio"s REST exception handling

    """

    def __init__(self, url: str, http_code: str,
                 error_code: str = None, description: str = None,
                 method: str = "GET"):
        self.url = url
        self.http_code = http_code
        self.error_code = error_code
        self.description = description
        self.method = method

    def __str__(self) -> str:
        """
        :return: if on TTY, a friendly string conversion for the object,
        else a one liner indicating the error
        """

        if hasattr(sys.stderr, "isatty") and sys.stderr.isatty():
            return (
                "\nHTTP Error - Your request was:\n\n{request}"
                "\n\nBuffer returned the following error message:\n\nHTTP "
                "{http_code} error: {error_code} description:"
                "{description}\n".format(
                    request="{} {}".format(self.method, self.url),
                    http_code=self.http_code,
                    error_code=self.error_code,
                    description=self.description
                ))

        return "HTTP {} error: {} description: {}".format(self.http_code,
                                                          self.error_code,
                                                          self.description)
