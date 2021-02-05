import requests
import json
import pprint


def makeCSV(data):
    csvStr = ''

    for row in data:
        for cell in row:
            csvStr += str(cell)
            csvStr += ','
        csvStr += '\n'
    
    return csvStr

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

testCountryURL = 'https://api.census.gov/data/timeseries/intltrade/exports/hs?get=E_COMMODITY,CTY_CODE,CTY_NAME,ALL_VAL_MO,SUMMARY_LVL&YEAR=2017&COMM_LVL=HS2&E_COMMODITY=03&CTY_CODE=1220'

# make sure there are no extra characters in key
API_KEY = API_KEY.rstrip('\n')

payload = {}
payload['key'] = API_KEY
payload['get'] = 'I_COMMODITY,GEN_QY2_MO,UNIT_QY2'#
payload['time'] = '2013-01'
payload['COMM_LVL'] = 'HS2'

print('before request')
testCountryURL += '&key='
testCountryURL += API_KEY
resp = requests.get(testCountryURL)#IMPORT_URL, params=payload)
print('after request')

pp = pprint.PrettyPrinter(indent=3)
print(resp.status_code)
if (resp.status_code >= 200) and (resp.status_code < 300):
    incomingData = resp.json()
    print(makeCSV(incomingData))
else:
    print(resp.content)
