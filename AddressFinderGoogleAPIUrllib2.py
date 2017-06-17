import urllib
import xlrd
from xlwt import easyxf
import json
from xlutils.copy import copy
import os.path
import time


workbookO = xlrd.open_workbook('JSList01.xlsx')
worksheet = workbookO.sheet_by_name('Sheet1')

wbNew = copy(workbookO)
wb_sheet = wbNew.get_sheet(0)

apiKey = 'AIzaSyAR1eVYwgVp3m1-t02IffU3DiQWOpYP9QY'

print('\n')

for current_row in range(worksheet.nrows):

    firmName = worksheet.row(current_row)[0]

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(firmName, apiKey)

    content = urllib.urlopen(url).read()

    try:
        address = (json.loads(content)["results"][0]['formatted_address'])
        wb_sheet.write(current_row, 1, address)
        print(address)
    except:
        findAddress = 'Find Address Manually'
        wb_sheet.write(current_row, 1, 'Z.F.I.')
        print(content)
        pass
    #time.sleep(1)

print('\n')

file_path = '/Users/Ryan/Desktop/WebScrape1/Lists With Addresses/Leads With Addresses'

wbNew.save(file_path + '.csv' + os.path.splitext(file_path)[-1])
