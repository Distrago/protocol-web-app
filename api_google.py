# -*- coding: utf-8 -*-

#Google API code
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/gmail.send']

#Main Code
service_sheets = None 
service_drive = None 
service_slides = None 
service_gmail = None 

def connect():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    global service_sheets
    global service_drive
    global service_slides
    global service_gmail

    service_sheets = build('sheets', 'v4', credentials=creds)
    service_drive = build('drive', 'v3', credentials=creds)
    service_slides = build('slides', 'v1', credentials=creds)
    service_gmail = build('gmail', 'v1', credentials=creds)

connect()