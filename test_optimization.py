# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google
import googlesheet_protocol

#SheetTable ID
ProtocolID = "1HLbW1tGSY3jM-deUjNSujPRSHBNudF_oFfM46wpm-dQ"

#Table_RANGE
ProtocolTableAll_Range = ["Protocol!A2:G", "Product!A2:J", "Sorting!A2:G", "Accept!A2:K", "Reject!A2:K"]

#Google API service
service = api_google.service_sheets

def get_all_table(product_name):
    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=ProtocolID,
		ranges=ProtocolTableAll_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    protocol_value = valueRanges[0].get('values', [])
    product_value = valueRanges[1].get('values', [])
    sorting_value = valueRanges[2].get('values', [])
    accept_value = valueRanges[3].get('values', [])
    reject_value = valueRanges[4].get('values', [])
    
    
    for row in product_value:
        if row[3] == product_name:
            print(row[0])
    
    
get_all_table('?????')
