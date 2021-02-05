import requests
import json
import pprint
import helpers

# international import and export trade URLs
EXPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/exports/hs'
IMPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/imports/hs'

# subnational import and export trade URLs
# for ports:
PORT_EXPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/exports/porths'
PORT_IMPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/imports/porths'
# for state by state data:
STATE_EXPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/exports/statehs'
STATE_IMPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/imports/statehs'


# read in API key
f = open('census_api_key.txt', 'r')
API_KEY = f.read()
f.close()

testCountryURL = 'https://api.census.gov/data/timeseries/intltrade/exports/statehs?get=E_COMMODITY,CTY_CODE,CTY_NAME,ALL_VAL_MO,SUMMARY_LVL,MONTH&YEAR=2017&YEAR=2018&COMM_LVL=HS2&E_COMMODITY=03&CTY_CODE=1220'

# make sure there are no extra characters in key
API_KEY = API_KEY.rstrip('\n')

tableHeaders = [
    'E_COMMODITY',
    'CTY_CODE',
    'CTY_NAME',
    'ALL_VAL_MO',
    'SUMMARY_LVL',
    'DF',
    'MONTH'
]

hsCodes = [
    '03'
]

years = [
    2017,
    2018,
    2019,
    2020
]

ctyCodes = [
    1220
]

hsLvl = 'HS2'


tradeData = helpers.getTradeRecords('export', EXPORT_URL, tableHeaders, hsCodes, hsLvl, years, ctyCodes, API_KEY)
tradesFileFormat = ''
if tradeData != None:
    tradesFileFormat = helpers.makeCSV(tradeData)
print(tradesFileFormat)
"""

stateURL = 'https://api.census.gov/data/timeseries/intltrade/exports/statehs?get=STATE,ALL_VAL_MO,ALL_VAL_YR&time=2013-01'

stateURL = stateURL +'&key=' + API_KEY

stateResp = requests.get(stateURL)
print(stateResp.status_code)
if stateResp.status_code == 200:
    stateData = stateResp.json()
    print(makeCSV(stateData))
else:
    print(stateResp.status_code)
    print(stateResp.content)

portURL = 'https://api.census.gov/data/timeseries/intltrade/imports/porths?get=PORT,PORT_NAME,GEN_VAL_MO,GEN_VAL_YR&time=2013-06'
portURL = portURL + '&key=' + API_KEY
portResp = requests.get(portURL)
print(portResp.status_code)
if portResp.status_code == 200:
    portData = portResp.json()
    print(makeCSV(portData))
else:
    print(portResp.content)
"""