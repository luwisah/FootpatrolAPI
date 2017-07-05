from bs4 import BeautifulSoup
import requests

# Written by Luke Davis (@R8T3D)
# Under the MIT license

# you need to change this to yours 
cart_id = 'your_cart_id'

# this shouldn't change, only have it as a variable just in case.
x_api_key = 'EA0E72B099914EB3BA6BE90A21EA43A9'

class FootpatrolAPI(object):
	def __init__(self):
		self.s = requests.Session()

		self.s.get("https://commerce.mesh.mx/stores/size/updates?version=2.0")
		self.s.get("https://commerce.mesh.mx/stores/size/nav?channel=iphone-app")
		self.s.get("https://commerce.mesh.mx/stores/size/deviceConfigurations/AppConfig")
		self.s.get("https://commerce.mesh.mx/stores/size/snippets/iphone-app?expand=content")
		self.s.get("https://commerce.mesh.mx/stores/size/carts/" + cart_id)

	def add_to_cart(self, pidsize):
		headers = {
		    'Host': 'commerce.mesh.mx',
		    'Content-Type': 'application/json',
		    'X-API-Key': x_api_key,
		    'Accept': '*/*',
		    'X-Debug': '1',
		    'Accept-Language': 'en-us',
		    'User-Agent': 'size/2.0 CFNetwork/808.3 Darwin/16.3.0',
		    'MESH-Commerce-Channel': 'iphone-app',
		}

		data = '{"quantity":1}'

		self.s.put('https://commerce.mesh.mx/stores/size/carts/' + cart_id + '/' + pidsize, headers=headers, data=data)

api = FootpatrolAPI()
api.add_to_cart(raw_input("PID.SIZE? "))
