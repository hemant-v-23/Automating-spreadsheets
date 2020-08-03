import openpyxl, pprint
print('Opening workbook...')
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb.get_sheet_by_name('Population by census tract')
countyData={}

# fill in countyData with each county's population and tracts.

print('Reading rows...')
for row in range(2,sheet.max_row  + 1):
    # each row in the spreadsheet has data for one census tract.
    state=sheet['B' + str(row)].value
    county=sheet['C' + str(row)].value
    pop=sheet['D' + str(row)].value

# Open a new text file and write the contents of countyData to it.

# make sure the key  for this state exists.

countyData.setdefault(state, {})

# make sure the key for this county in this state exists.

countyData[state].setdefault(county, {'tracts':0, 'pop' : 0})
# eac row represents one census tract, so  increment by one.

countyData[state][county]['tracts']+=1

# increase the county pop by the pop in this census tract.
countyData[state][county]['pop']+=int(pop)

# open a new text file and write the contents of countyData to it.

print('Writing results...')
resultfile=open('census2010.py', 'w')
resultfile.write('alldata=' + pprint.pformat(countyData))
resultfile.close()
print('Done')

# To see output

import os
import census2010
census2010.allData['AK']['Anchorage']
{'pop':291826, 'tracts':55}