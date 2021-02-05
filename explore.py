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

def buildColHeaders(colHeaders):

    colNames = ''

    for colName in colHeaders:
        colNames += colName
        colNames += ','
    
    colNames = colNames[:-1]

    return colNames

def buildHS_Codes(tradeType, hsCodes, commLvl):

    commodityType = ''
    if tradeType == 'export':
        commodityType = 'E_COMMODITY'
    elif tradeType == 'import':
        commodityType = 'I_COMMODITY'
    
    hsURL = 'COMM_LVL=' + commLvl + '&'
    for hsCode in hsCodes:
        hsURL = hsURL + commodityType + '=' + hsCode + '&'
    hsURL = hsURL[:-1]
    return hsURL

def buildYears(years):
    yearURL = ''

    for year in years:
        yearURL = yearURL + 'YEAR=' + str(year) + '&'
    yearURL = yearURL[:-1]
    return yearURL

def buildCtyCodes(ctyCodes):
    ctyCodeURL = ''

    if len(ctyCodes) > 0:
        for ctyCode in ctyCodes:
            ctyCodeURL = ctyCodeURL + 'CTY_CODE=' + str(ctyCode) + '&'
        
        ctyCodeURL = ctyCodeURL[:-1]

    return ctyCodeURL

def getTradeRecords(tradeType, tradeURL, colHeaders, hsCodes, hsLvl, years, ctyCodes, apiKey):

    fullURL = tradeURL + '?get='
    fullURL = fullURL + buildColHeaders(colHeaders)
    fullURL = fullURL + '&' + buildHS_Codes(tradeType, hsCodes, hsLvl)
    fullURL = fullURL + '&' + buildYears(years)
    fullURL = fullURL + '&' + buildCtyCodes(ctyCodes)
    fullURL = fullURL + '&key=' + apiKey

    resp = requests.get(fullURL)

    if resp.status_code == 200:
        tradeRecords = resp.json()
    else:
        tradeRecords = None
    return tradeRecords

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

testCountryURL = 'https://api.census.gov/data/timeseries/intltrade/exports/hs?get=E_COMMODITY,CTY_CODE,CTY_NAME,ALL_VAL_MO,SUMMARY_LVL,MONTH&YEAR=2017&YEAR=2018&COMM_LVL=HS2&E_COMMODITY=03&CTY_CODE=1220'

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

tradeData = getTradeRecords('export', EXPORT_URL, tableHeaders, hsCodes, hsLvl, years, ctyCodes, API_KEY)
tradesFileFormat = ''
if tradeData != None:
    tradesFileFormat = makeCSV(tradeData)
print(tradesFileFormat)
