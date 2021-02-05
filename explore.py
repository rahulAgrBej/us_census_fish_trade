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
    'MONTH'
]

portHeaders = [
    'E_COMMODITY',
    'PORT',
    'PORT_NAME',
    'ALL_VAL_MO',
    'MONTH'
]

stateHeaders = [
    'E_COMMODITY',
    'STATE',
    'ALL_VAL_MO',
    'MONTH'
]

hsCodes = [
    '03'
]

years = [
    2017
]

ctyCodes = [
    1220
]

hsLvl = 'HS2'

"""
# INTL trade data example
tradeData = helpers.getTradeRecords('export', EXPORT_URL, tableHeaders, hsCodes, hsLvl, years, ctyCodes, API_KEY)
tradesFileFormat = ''
if tradeData != None:
    tradesFileFormat = helpers.makeCSV(tradeData)
print(tradesFileFormat)

# PORT trade data example
portData = helpers.getTradeRecords('export', PORT_EXPORT_URL, portHeaders, hsCodes, hsLvl, years, [], API_KEY)
portFileFormat = ''
if portData != None:
    portFileFormat = helpers.makeCSV(portData)
print(portFileFormat)

# STATE trade data example
stateData = helpers.getTradeRecords('export', STATE_EXPORT_URL, stateHeaders, hsCodes, hsLvl, years, [], API_KEY)
stateFileFormat = ''
if stateData != None:
    stateFileFormat = helpers.makeCSV(stateData)
print(stateFileFormat)
"""

QTY1_URL = 'https://api.census.gov/data/timeseries/intltrade/exports/hs?get=E_COMMODITY,E_COMMODITY_LDESC,UNIT_QY1,UNIT_QY2,ALL_VAL_MO,QTY_1_MO,QTY_1_MO_FLAG,QTY_2_MO,QTY_2_MO_FLAG&YEAR=2015&E_COMMODITY=0303240000'
QTY1_URL = QTY1_URL + '&key=' + API_KEY
q1Resp = requests.get(QTY1_URL)
print(q1Resp.status_code)
print(helpers.makeCSV(q1Resp.json()))