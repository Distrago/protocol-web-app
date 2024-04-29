# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google
service = api_google.service_sheets

#ProtocolStatistics
ProtocolStatistics = "1MmWu4h_NIPpAZbRCnWKVG8EvSi3WQLRiCYNdHqIfDSY"
#Table Range
Statistics_Range = "Statistics!A2:Z"

class Statistics:
    def __init__ (self, row_data):
        self.id_delay = row_data[0]
        self.id_demands = row_data[1]
        self.id_protocol = row_data[2]
        self.date_demands = row_data[3]
        self.date_protocol = row_data[4]
        self.name_company = row_data[5]
        self.name_manager = row_data[6]
        self.name_technical = row_data[7]
        self.product_demands = row_data[8]
        self.percent_original = row_data[9]
        self.tc_original = row_data[10]
        self.purePercentFraction = row_data[11]
        self.tcMainFractiom = row_data[12]
        self.componentDemandsList = row_data[13]
        self.apparatConfiguration = row_data[14]
        self.prptocolType = row_data[15]
        self.protocolProduct = row_data[16]
        self.purePercentOriginalP = row_data[17]
        self.tcOriginalP = row_data[18]
        self.purePercentMainFractionP = row_data[19]
        self.tcMainFraction = row_data[20]
        self.protocolComponentList = row_data[21]
        self.apparatConfigurationProtocol = row_data[22]
        self.trays = row_data[23]
        self.sorting = row_data[24]
        self.relevance = row_data[25]
    def to_dict(self):
        return{
            "id_delay" : self.id_delay,
            "id_demands" : self.id_demands,
            "id_protocol" : self.id_protocol,
            "date_demands" : self.date_demands,
            "date_protocol" : self.date_protocol,
            "name_company" : self.name_company,
            "name_manager" : self.name_manager,
            "name_technical" : self.name_technical,
            "product_demands" : self.product_demands,
            "percent_original" : self.percent_original,
            "tc_original" : self.tc_original,
            "purePercentFraction" : self.purePercentFraction,
            "tcMainFractiom" : self.tcMainFractiom,
            "componentDemandsList" : self.componentDemandsList,
            "apparatConfiguration" : self.apparatConfiguration,
            "prptocolType" : self.prptocolType,
            "protocolProduct" : self.protocolProduct,
            "purePercentOriginalP" : self.purePercentOriginalP,
            "tcOriginalP" : self.tcOriginalP,
            "purePercentMainFractionP" : self.purePercentMainFractionP,
            "tcMainFraction" : self.tcMainFraction,
            "protocolComponentList" : self.protocolComponentList,
            "apparatConfigurationProtocol" : self.apparatConfigurationProtocol,
            "trays" : self.trays,
            "sorting" : self.sorting,
            "relevance" : self.relevance}
list_statistics = []

def read_statistics():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolStatistics,
                                range=Statistics_Range).execute()
    values = result.get('values', [])
    for row in values:
        list_statistics.append( Statistics(row))
    print("table statistics onload")

#Запись в конец таблицы
def write_statictic(write_data):
    sheet = service.spreadsheets()    
    result = sheet.values().get(spreadsheetId=ProtocolStatistics,
		range=Statistics_Range).execute()
    values = result.get('values', [])

    values_id = 0
    
    for row in values:
        if str(row[2]) == str(write_data[2]):
            values[values_id][25] = False
        values_id += 1
    
    oldRangeStatistic = 'Statistics!A2' + ':Z' + str(len(values) + 1)
    
    oldBody = {
		'values': values
	}
   
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolStatistics, range=oldRangeStatistic,
    valueInputOption="USER_ENTERED", body=oldBody).execute()  

    body = {
		'values': [write_data]
	}
    
    rangeStatistics = 'Statistics!A' + str(len(values) + 2) + ':Z' + str(len(values) + 2)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolStatistics, range=rangeStatistics,
    valueInputOption="USER_ENTERED", body=body).execute()
    
    
def edit_statistics(id_protocol, write_data):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolStatistics,
		range='Statistics!C2:C').execute()
    values = result.get('values', [])
    
    id_row = 1;
    
    for row in values:
        if str(row[0]) == str(id_protocol):
            break
        else:
            id_row += 1       
    #Удаление старых строк
    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 0,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+1)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolStatistics, body=bodyDeleat).execute()
    #Добавление нового числа строк 
    bodyInsert = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': 0,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+1)
                    },
                    'inheritFromBefore': True
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolStatistics, body=bodyInsert).execute()        
    body = {
		'values': [write_data]
	}
    
    rangeStatistics = 'Statistics!A' + str(id_row+1) + ':Y' + str(id_row+1)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolStatistics, range=rangeStatistics,
    valueInputOption="USER_ENTERED", body=body).execute()
