# from geopy.geocoders import Nominatim

# if __name__ == "__main__":
#   address = '207 N. Defiance St, Archbold, OH'
#   user_agent = 'David'
#   location = Nominatim(user_agent=user_agent).geocode(address)
#   print(location.latitude, location.longitude)

import http.client
import json
from urllib.parse import quote_plus

base = '/search'

def geocode(address):
  
  path = '{}?q={}&format=json'.format(base, quote_plus(address))
  user_agent = 'David'
  headers = {'User-Agent': user_agent}
  connection = http.client.HTTPConnection('nominatim.openstreetmap.org')
  connection.request('GET', path, None, headers)
  rawreply = connection.getresponse().read()
  reply = json.loads(rawreply.decode('utf-8'))
  print(reply[0]['lat'], reply[0]['lon'])
  
if __name__ == '__main__':
  geocode('207 N. Defiance St, Archbold, OH')
  