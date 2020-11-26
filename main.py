from secrets import *
import requests

host = 'https://thu.closed.social'

obtain_token = '/oauth/token'
token = requests.post(host+obtain_token, 
	         {'client_id': app_id, 
	          'client_secret': app_secret,
	          'redirect_uri': 'urn:ietf:wg:oauth:2.0:oob'})
print(token)