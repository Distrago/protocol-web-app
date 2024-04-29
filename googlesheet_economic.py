# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

#SheetTable ID
requestEconomicTableID = "18jRh_wC7Wd2IOLDuCxUG2CLpXHATV3Is-UTd028YCOM"
#TableRange
rowClassifier = "rowClassifier!A2:E"

#Google API service
service = api_google.service_sheets

class ClassifierRow:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.name = row_data[1]
        self.sumParameters = row_data[2]
        self.dateParameters = row_data[3]
        self.incomeArrow = row_data[4]
        self.EN = row_data[5]
    def to_dict(self):
        return{"id": self.id,
               "name": self.name,
               "sumParameters": self.sumParameters,
               "dateParameters": self.dateParameters,
               "incomeArrow": self.incomeArrow,
               "EN": self.EN}
list_classifierRow = []


def load_requestEconomicTable():
    RequestEconomicTable_Range = ["rowClassifier!A2:F"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=requestEconomicTableID, ranges = RequestEconomicTable_Range,
                                     valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    
    classifierRow = valueRanges[0].get('values', [])
    
    for row in classifierRow:
        list_classifierRow.append(ClassifierRow(row))
        
def upload_google_table():
    load_requestEconomicTable()