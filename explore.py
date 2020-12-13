import requests
import json


EXPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/exports/hs'
IMPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/imports/hs'

# read in API key
f = open('census_api_key.txt', 'r')
API_KEY = f.read()
f.close()

"""
https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMO
DITY,GEN_VAL_MO&time=2013-01&COMM_LVL=HS2
"""

# make sure there are no extra characters in key
API_KEY = API_KEY.rstrip('\n')

payload = {}
payload['key'] = API_KEY
payload['get'] = 'I_COMMODITY,GEN_VAL_MO'
payload['time'] = '2013-01'
payload['COMM_LVL'] = 'HS2'


resp = requests.get(IMPORT_URL, params=payload)
print(resp.status_code)
print(resp.content)
