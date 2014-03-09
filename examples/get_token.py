from colorama import Fore

from buffpy import AuthService

client_id = '531c789efeaa69c436000080'
client_secret = '818ae1eb0f615ffaf298ba6b6db658e0'

print Fore.YELLOW + '---- START TOKEN RETRIEVING OPERATION ----' + Fore.RESET
redirect_uri = 'http://vladtemian.info'


service = AuthService(client_id, client_secret, redirect_uri)

url = service.authorize_url
print Fore.GREEN + 'Access this url and retrieve the token: ' + Fore.RESET + url

auth_code = raw_input(Fore.GREEN + 'Paste the code from the redirected url: ' + Fore.RESET)
access_token = service.get_access_token(auth_code)
print Fore.GREEN + 'Acess TOKEN: ' + Fore.RESET + access_token

api = service.create_session(access_token)

#Do stuff with your session
