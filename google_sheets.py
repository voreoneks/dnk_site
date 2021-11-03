from pprint import pprint

import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from release.models import *


class Sheet():

    CREDENTIALS_FILE = 'creds.json'
    spreadsheet_id = '1ZpaXmS3QBAIcSQRy_2QjWB0PiGkOs9AU0SniWgVclHY'
    
    def __init__(self, global_range, insert_data_option = 'INSERT_ROWS', value_input_option = "RAW", spreadsheet_id = '1ZpaXmS3QBAIcSQRy_2QjWB0PiGkOs9AU0SniWgVclHY'):
        self.spreadsheet_id = spreadsheet_id
        self.global_range = global_range
        self.insert_data_option = insert_data_option
        self.value_input_option = value_input_option
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'])
        self.httpAuth = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('sheets', 'v4', http = self.httpAuth)

    def append(self, data):
        values = self.service.spreadsheets().values().append(
        spreadsheetId=self.spreadsheet_id,
        range=self.global_range,
        valueInputOption = self.value_input_option,
        insertDataOption=self.insert_data_option,
        body=data
        )
        values.execute()

    def read(self, range, majorDimension):
        values = self.service.spreadsheets().values().get(
        spreadsheetId=self.spreadsheet_id,
        range=range,
        majorDimension=majorDimension
        ).execute()
        return values

    def write(self, data):
        values = self.service.spreadsheets().values().batchUpdate(
        spreadsheetId=self.spreadsheet_id,
        body={
            "valueInputOption": self.value_input_option,
            "data": [data]
        })
        values.execute()
