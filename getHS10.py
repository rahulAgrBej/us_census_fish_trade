
# Get all HS level 10 codes

# Gets all codes from CSV file
inFilePath = 'htsdata.csv'

inF = open(inFilePath, 'r')
lines = inF.readlines()
inF.close()

# Processes string in CSV to get all HS level 10 codes
hs_10_codes = []

for line in lines[1:]:
    line = line.rstrip('\n')
    cells = line.split(',')
    if (len(cells[0]) > 0) and (cells[0][0].isdigit()):
        tempSplit = cells[0].split('.')
        hs10Code = ''.join(tempSplit)
        if (len(hs10Code) == 10) and hs10Code.isnumeric():
            hs_10_codes.append(hs10Code)


# Gets all Seafood HS level 6 codes

fName0 = 'relevantHScodes/hs_codes_verHS17.csv'
fName1 = 'relevantHScodes/raw_codes_arranged_for_matching_logic.csv'

fileNames = []

fileNames.append(fName0)
fileNames.append(fName1)

seafoodlvl6HScodes = set()

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
        seafoodlvl6HScodes.add(str(hsCode))

# Gets all HS lvl 10 codes that match the Seafood HS lvl 6 codes

seafoodLVL10 = []

for hs_10_code in hs_10_codes:
    if hs_10_code[:6] in seafoodlvl6HScodes:
        seafoodLVL10.append(hs_10_code)

print(len(seafoodLVL10))
print(seafoodLVL10)

# Outputs seafood hs lvl 10 codes
outStr = ''
for code in seafoodLVL10:
    outStr = outStr + code + '\n'

outFilePath = 'seafoodLvl10Codes.csv'
outF = open(outFilePath, 'w')
outF.write(outStr)
outF.close()