import re
import pyperclip
import fnmatch
import openpyxl as ox


filepath = r'C:\cifs\home\bly6\Python Scripts\PyKAT\Operating Keycodes D36.xlsm'
wb = ox.load_workbook(filepath, data_only=True)
ws = wb['Splits PVT']
todays_styles = ws['A6':'A87']
activeKC = None
# assumes a copy of the worklist is in the clipboard
KAT_WL = re.compile('\s+').split(pyperclip.paste())

for each in todays_styles:
    single = str("*" + str(each[0].value))
    filter = fnmatch.filter(KAT_WL, single)
    if filter != []:
        activeKC = each[0].value
        break
if activeKC == "0" or activeKC is None:
    sys.exit('current WL selection is not in todays styles')

print(activeKC)

