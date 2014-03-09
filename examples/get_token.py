from colorama import Fore

from buffpy import AuthService

client_id = 'add_apps_client_id'
client_secret = 'add_apps_secret'

print Fore.YELLOW + '---- START TOKEN RETRIEVING OPERATION ----' + Fore.RESET
redirect_uri = 'add_your_redirect_uri(with http)'


service = AuthService(client_id, client_secret, redirect_uri)

url = service.authorize_url
print Fore.GREEN + 'Access this url and retrieve the token: ' + Fore.RESET + url

auth_code = raw_input(Fore.GREEN + 'Paste the code from the redirected url: ' + Fore.RESET)
access_token = service.get_access_token(auth_code)
print Fore.GREEN + 'Acess TOKEN: ' + Fore.RESET + access_token

api = service.create_session(access_token)

#Do stuff with your session
