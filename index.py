import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
CREDS = ServiceAccountCredentials.from_json_keyfile_name('keys.json', SCOPES)
CLIENT = gspread.authorize(CREDS)
SPREADSHEET_ID = '18NmM9GqkKHkeysfgG3_ljjypDbdwuFQG7gec4lxWhGQ'
RANGE = '2020 Logs'
SHEET_NAME = 'Listen Log'
WORKING_SHEET = CLIENT.open(SHEET_NAME).sheet1
ROW_INPUT_DATA = [
    'Afksky',
    'Ofte jeg drommer mig dod',
    'Black',
    'Full Length',
    'Denmark',
    'https://vendetta-records.bandcamp.com/album/ofte-jeg-dr-mmer-mig-d-d'
]

def main():
    # readAllData()
    appendRow(ROW_INPUT_DATA)
    # getLastRecord()

def getLastRecord():
    rowCount = list(filter(None, WORKING_SHEET.col_values(1)))
    rowCountNum = len(rowCount)
    lastRecord = WORKING_SHEET.row_values(rowCountNum)
    print(lastRecord)

def appendRow(rowInputData):
    WORKING_SHEET.append_row(rowInputData)
    print('Row appended')

def readAllData():
    allData = WORKING_SHEET.get_all_records()
    print(allData)

if __name__ == '__main__':
    main()
