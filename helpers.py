import requests
import json

def makeCSV(data):
    csvStr = ''

    for row in data:
        for cell in row:
            csvStr += (str(cell)).replace(',', '')
            csvStr += ','
        csvStr = csvStr[:-1]
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
        print(resp.status_code)
        print(resp.content)
        tradeRecords = None
    return tradeRecords