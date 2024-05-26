import os.path

import io
from googleapiclient.http import MediaIoBaseDownload

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Spreadsheet():
  def __init__(self) -> None:
    self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    self.SAMPLE_SPREADSHEET_ID = "1pD8D8blyInoDpFYDQVIylAu67EZ_51dc_SCpsiaGKlA"
    self.SAMPLE_RANGE_NAME = "Página1!A5:D14"
    self.creds = None
    
  def auth(self):
    if os.path.exists("token.json"):
      self.creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)
    if not self.creds or not self.creds.valid:
      if self.creds and self.creds.expired and self.creds.refresh_token:
        self.creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", self.SCOPES
        )
        self.creds = flow.run_local_server(port=0)
      
      with open("token.json", "w") as token:
        token.write(self.creds.to_json())

  def read(self):
    try:
      service = build("sheets", "v4", credentials=self.creds)

      # Call the Sheets API
      sheet = service.spreadsheets()
      result = (
          sheet.values()
          .get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, range=self.SAMPLE_RANGE_NAME)
          .execute()
      )
      values = result.get("values", [])

      if not values:
        print("Nenhum dado encontrado.")
        return
    
      return [row[0] for row in values]
    
    except HttpError as err:
      print(err)
      
  def update(self,values):
    try:
      service = build("sheets", "v4", credentials=self.creds)

      # Call the Sheets API
      sheet = service.spreadsheets()
      body = {'values': values}
      result = (
          sheet.values().update(
            spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
            range="B5:D14",
            valueInputOption="USER_ENTERED",
            body=body
          ).execute()
      )
      return result
    
      
    
    except HttpError as err:
      print(err)