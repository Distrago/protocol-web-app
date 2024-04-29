# -*- coding: utf-8 -*-
from __future__ import print_function
import api_google

#SheetTable ID
DealerInfoList = "1erj3rQ7xz-g8eDy4fJyEEn9usIvPdzn2Hb0TnTexU9U"

service = api_google.service_sheets

"""Классы для таблицы подгружаемых из гугла"""
class dealerInfo:
    def __init__ (self, row_data):
        self.id_dealer = row_data[0]
        self.img_logoTop = row_data[1]
        self.img_logoBottom = row_data[2]
        self.textTop = row_data[3]
        self.textBottom = row_data[4]
        self.dealerBitrix24 = row_data[5]
        self.companyName = row_data[6]
    def to_dict(self):
        return {"id_dealer": self.id_dealer,
                "img_logoTop": self.img_logoTop,
                "img_logoBottom": self.img_logoBottom,
                "textTop": self.textTop,
                "textBottom": self.textBottom,
                "dealerBitrix24": self.dealerBitrix24,
                "companyName": self.companyName}
list_dealerInfo = []

def upload_google_table():
    DealerInfo_Range = ["DealerInfo!A2:G"]
    
    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=DealerInfoList,
		ranges=DealerInfo_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    
    dealerInfo_value = valueRanges[0].get('values', [])
    
    #Заполнение массива информации о дилерах
    for row in dealerInfo_value:
        list_dealerInfo.append(dealerInfo(row))