

# international import and export trade URLs
EXPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/exports/hs'
IMPORT_URL = 'https://api.census.gov/data/timeseries/intltrade/imports/hs'

# read in API key
f = open('census_api_key.txt', 'r')
API_KEY = f.read()
f.close()

# make sure there are no extra characters in key
API_KEY = API_KEY.rstrip('\n')

tableHeadersExport = [
    'CTY_CODE',
    'CTY_NAME',
    'ALL_VAL_MO',
    'SUMMARY_LVL',
    #'DF',
    #'AIR_VAL_MO', # air value
    #'AIR_WGT_MO', # air weight value
    #'VES_VAL_MO', # vessel value
    #'CNT_VAL_MO', # containerized vessel value
    'MONTH'
]

tableHeadersImport = [
    'CTY_CODE',
    'CTY_NAME',
    'GEN_VAL_MO',
    'AIR_VAL_MO', # air value
    'AIR_WGT_MO', # air weight value
    'VES_VAL_MO', # vessel value
    'VES_WGT_MO', # vessel value weight
    'CNT_VAL_MO', # containerized vessel value
    'CNT_WGT_MO', # containerized vessel weight value
    'MONTH',
    'SUMMARY_LVL'
    #'DF'
]

years = [
    2017,
    2018,
    2019,
    2020
]

ctyCodes = [
]

hsLvl = 'HS6'

# Get all relevant HS Codes from files

fName0 = 'relevantHScodes/hs_codes_verHS17.csv'
fName1 = 'relevantHScodes/raw_codes_arranged_for_matching_logic.csv'

fileNames = []

fileNames.append(fName0)
fileNames.append(fName1)

relevantHScodes = set()

for fName in fileNames:
    f = open(fName, 'r')
    rows = f.readlines()[1:]
    f.close()

    for row in rows:
        row = row.rstrip('\n')
        cells = row.split(',')
        hsCode = str(cells[0])
        if hsCode[0] == '\"':
            hsCode = str(hsCode[1:-1])

        if len(hsCode) == 5:
            hsCode = '0' + hsCode

        #print(f'{cells[0]} {hsCode}')
        relevantHScodes.add(str(hsCode))


