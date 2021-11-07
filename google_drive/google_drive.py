from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


class Drive():

    BASE_DIR = Path(__file__).resolve().parent.parent
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = str(BASE_DIR) + '\\google_drive\\creds_drive.json'
    SCRIPT_PATH = Path(__file__).resolve().parent

    def __init__(self):
        self.credentials = service_account.Credentials.from_service_account_file(
                self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.service = build('drive', 'v3', credentials=self.credentials)

    def upload_file(self, folder_id, name, file_path):
        file_metadata = {
                        'name': name,
                        'parents': [folder_id]
                    }
        media = MediaFileUpload(file_path, resumable=True)
        r = self.service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
        return r

    def create_folder(self, folder_id, name):
        file_metadata = {
                        'name': name,
                        'mimeType': 'application/vnd.google-apps.folder',
                        'parents': [folder_id]
                    }
        r = self.service.files().create(body=file_metadata, fields='id').execute()
        return r

