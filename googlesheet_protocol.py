# -*- coding: utf-8 -*-
from __future__ import print_function
from collections import Counter
from collections import OrderedDict
import operator
import math
import api_google

#GoogleSheetTableRequirements
import googlesheet_requirements

#SheetTable ID
ProtocolID = "1HLbW1tGSY3jM-deUjNSujPRSHBNudF_oFfM46wpm-dQ"

#Table_RANGE
Protocol_Range = "Protocol!A2:K"
Product_Range = "Product!A2:J"
Sorting_Range = "Sorting!A2:H"
Accept_Range = "Accept!A2:K"
Reject_Range = "Reject!A2:K"

ProtocolTableAll_Range = ["Protocol!A2:K", "Product!A2:L", "Sorting!A2:H", "Accept!A2:K", "Reject!A2:K"]

#Google API service
service = api_google.service_sheets

#Словарь заглавных букв латинского алфавита(для динамической записи в таблицы компонентов)
charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Class(table)
"""Классы для таблицы подгружаемых из гугла"""

"""Протокол"""
class Protocol:
    def __init__(self, ID_Protocol, ID_Requirements, write_type, equipment, configuration, sortingValue, componentValue, company_name, ID_creater, ID_responsible, create_date):
        self.ID_Protocol = ID_Protocol
        self.ID_Requirements = ID_Requirements
        self.write_type = write_type #Запись которая оприделяет тип сохраненных данных, обычно быудет испорльзоваться девелоперский "тест"
        self.equipment = equipment
        self.configuration = configuration
        self.sortingValue = sortingValue
        self.componentValue = componentValue
        self.company_name = company_name
        self.ID_creater = ID_creater
        self.ID_responsible = ID_responsible
        self.create_date = create_date
    def to_dict(self):
        return {"ID_Protocol": self.ID_Protocol,
                "ID_Requirements": self.ID_Requirements,
                "write_type": self.write_type,
                "equipment": self.equipment,
                "configuration": self.configuration,
                "sortingValue": self.sortingValue,
                "componentValue": self.componentValue,
                "company_name": self.company_name,
                "ID_creater": self.ID_creater,
                "ID_responsible": self.ID_responsible,
                "create_date": self.create_date}
list_protocol = []

class Product:
    def __init__(self, ID_Protocol, ID_Requirements, ID_Product, productName, purpose, purity, capacity, capacity_type, selection, selection_type, photoFolder, ID_mainPhoto):
        self.ID_Protocol = ID_Protocol
        self.ID_Requirements = ID_Requirements
        self.ID_Product = ID_Product
        self.productName = productName
        self.purpose = purpose
        self.purity = purity
        self.capacity = capacity
        self.capacity_type = capacity_type
        self.selection = selection
        self.selection_type = selection_type
        self.photoFolder = photoFolder
        self.ID_mainPhoto = ID_mainPhoto
    def to_dict(self):
        return {"ID_Protocol": self.ID_Protocol,
                "ID_Requirements": self.ID_Requirements,
                "ID_Product": self.ID_Product,
                "productName": self.productName,
                "purpose": self.purpose,
                "purity": self.purity,
                "capacity": self.capacity,
                "capacity_type": self.capacity_type,
                "selection": self.selection,
                "selection_type": self.selection_type,
                "photoFolder": self.photoFolder,
                "ID_mainPhoto": self.ID_mainPhoto}
list_product = []
 
class Sorting:
    def __init__(self, ID_Protocol, ID_Sorting, inbox_fraction, trays_number, purity, capacity, capacity_type, programFolder):
        self.ID_Protocol = ID_Protocol
        self.ID_Sorting = ID_Sorting
        self.inbox_fraction = inbox_fraction
        self.trays_number = trays_number
        self.purity = purity
        self.capacity = capacity
        self.capacity_type = capacity_type
        self.programFolder = programFolder
    def to_dict(self):
        return {"ID_Protocol": self.ID_Protocol,
                "ID_Sorting": self.ID_Sorting,
                "inbox_fraction": self.inbox_fraction,
                "trays_number": self.trays_number,
                "purity": self.purity,
                "capacity": self.capacity,
                "capacity_type": self.capacity_type,
                "programFolder": self.programFolder}
list_sorting = []

"""Проход и Отбой"""
class AcceptReject:
    def __init__(self, ID_Protocol, ID_Sorting, fractionName, fractionNameID, selection, selectiont_type, exit, purity, capacity, photoFolder, ID_mainPhoto):
        self.ID_Protocol = ID_Protocol
        self.ID_Sorting = ID_Sorting
        self.fractionName = fractionName
        self.fractionNameID = fractionNameID
        self.selection = selection
        self.selectiont_type = selectiont_type
        self.exit = exit
        self.purity = purity
        self.capacity = capacity
        self.photoFolder = photoFolder
        self.ID_mainPhoto = ID_mainPhoto
    def to_dict(self):
        return {"ID_Protocol": self.ID_Protocol,
                "ID_Sorting": self.ID_Sorting,
                "fractionName": self.fractionName,
                "fractionNameID": self.fractionNameID,
                "selection": self.selection,
                "selectiont_type": self.selectiont_type,
                "exit": self.exit,
                "purity": self.purity,
                "capacity": self.capacity,
                "photoFolder": self.photoFolder,
                "ID_mainPhoto": self.ID_mainPhoto}
list_accept = []
list_reject = []

list_components = []

#Запись данных в таблицы
"""
def write_protocol(id_protocol, id_requirements, write_type, equipment, configuration, sortingValue, componentValue):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Protocol!A1:A').execute()
    values = result.get('values', [])
    
    #Автоматическое назначение айдишников
    if id_protocol == "-":
        id_protocol = len(values)
        
    write_values = [
        [
            id_protocol,
            id_requirements,
            write_type,
            equipment,
            configuration,
            sortingValue,
            componentValue
		]
	]
    body = {
		'values': write_values
	}
    rangeProtocol = 'Protocol!A' + str(len(values) + 1) + ':G' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeProtocol,
    valueInputOption="USER_ENTERED", body=body).execute()

    return id_protocol

def write_product(id_protocol, id_requirements, id_product, productName, purpose, purity, capacity, capacity_type, selection, selection_type, photoFolder, id_mainPhoto):
    sheet = service.spreadsheets()    
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Product!A1:A').execute()
    values = result.get('values', [])
    
    write_values = [
        [
            id_protocol,
            id_requirements,
            id_product,
            productName,
            purpose,
            purity,
            capacity, 
            capacity_type, 
            selection, 
            selection_type,
            photoFolder,
            id_mainPhoto
		]
	]
    body = {
		'values': write_values
	}
    rangeProduct = 'Product!A' + str(len(values) + 1) + ':L' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeProduct,
    valueInputOption="USER_ENTERED", body=body).execute()      

def write_sorting(id_protocol, id_sorting, inbox_fraction, purity, capacity, capacity_type, programFolder):
    sheet = service.spreadsheets()    
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Sorting!A1:A').execute()
    values = result.get('values', [])
    
    write_values = [
        [
            id_protocol,
            id_sorting,
            inbox_fraction,
            purity,
            capacity,
            capacity_type,
            programFolder
		]
	]
    body = {
		'values': write_values
	}
    rangeSorting = 'Sorting!A' + str(len(values) + 1) + ':G' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeSorting,
    valueInputOption="USER_ENTERED", body=body).execute()

def write_accept(id_protocol, id_sorting, fractionName, selection, selection_type, exit, purity, capacity, photoFolder, id_mainPhoto):
    sheet = service.spreadsheets()        
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Accept!A1:A').execute()
    values = result.get('values', [])
    
    write_values = [
        [
            id_protocol,
            id_sorting,
            fractionName,
            selection,
            selection_type,
            exit,
            purity,
            capacity,
            photoFolder,
            id_mainPhoto
		]
	]
    body = {
		'values': write_values
	}
    rangeAccept = 'Accept!A' + str(len(values) + 1) + ':J' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeAccept,
    valueInputOption="USER_ENTERED", body=body).execute()
    
def write_reject(id_protocol, id_sorting, fractionName, selection, selection_type, exit, purity, capacity, photoFolder, id_mainPhoto):
    sheet = service.spreadsheets()    
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Reject!A1:A').execute()
    values = result.get('values', [])
    
    write_values = [
        [
            id_protocol,
            id_sorting,
            fractionName,
            selection,
            selection_type,
            exit,
            purity,
            capacity,
            photoFolder,
            id_mainPhoto
		]
	]
    body = {
		'values': write_values
	}
    rangeReject = 'Reject!A' + str(len(values) + 1) + ':J' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeReject,
    valueInputOption="USER_ENTERED", body=body).execute()    
    
def write_component_mainInfo(id_protocol, id_component, component_number, component_name, component_value, component_type, component_valid_check, component_remove_check, photoFolder, id_mainPhoto):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Components!A1:A').execute()
    values = result.get('values', [])
    
    
    write_values = [
        [
            id_protocol,
            id_component,
            component_number,
            component_name,
            component_value,
            component_type,
            component_valid_check,
            component_remove_check,
            photoFolder,
            id_mainPhoto
        ]
    ]
    body = {
		'values': write_values
	}
    
    rangeComponents = 'Components!A' + str(len(values) + 1) + ':J' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeComponents,
    valueInputOption="USER_ENTERED", body=body).execute()     

def write_component_sortingInfo(id_AcceptReject, str_number, component_value, component_type, component_valid_check, component_warnin_check):
    first_char, last_char = setup_char_vaule(int(id_AcceptReject))

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Components!A1:A').execute()
    values = result.get('values', [])
    
    write_values = [
        [
            component_value,
            component_type,
            component_valid_check,
            component_warnin_check
        ]
    ]
    body = {
        'values': write_values
    }
    
    line_number = str(len(values) - int(str_number))
    rangeComponents = 'Components!' + first_char + line_number +":"+ last_char + line_number
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeComponents,
    valueInputOption="USER_ENTERED", body=body).execute() 
"""
def setup_char_vaule(id_AcceptReject):
    id_charset = 6 + (id_AcceptReject*4)
    if id_charset < len(charset)-1:
        first_char = charset[id_charset]
        try:
            last_char = charset[id_charset+3]
        except:
            id_charset -= len(charset)
            last_char = 'A' + charset[id_charset+3]
    else:
        temp = id_charset
        circle = -1
        while temp > len(charset)-1:
            temp -= len(charset)
            circle += 1 
        first_char = charset[circle]
        last_char = charset[circle]
        
    while id_charset > len(charset)-1 :
        id_charset -= len(charset)
        first_char += charset[id_charset]
        last_char += charset[id_charset+3]
    
    #заплатка при достижении совпадения
    if last_char == first_char:
        id_charset -= len(charset)
        last_char = 'A' + charset[id_charset+3]
        
    return first_char, last_char
    
#Получение протоколов по параметру
def search_protocol(productName, equipment, configuration):
    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=ProtocolID,
		ranges=ProtocolTableAll_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    
    protocol_value = valueRanges[0].get('values', [])
    product_value = valueRanges[1].get('values', [])
    sorting_value = valueRanges[2].get('values', [])
    accept_value = valueRanges[3].get('values', [])
    reject_value = valueRanges[4].get('values', [])
    
    id_protocol = []
    id_requirements = []
    
    #Поиск по продукту
    for row in product_value:
        if row[3] == productName:
            id_protocol.append(row[0])
            id_requirements.append(row[1])
    
    #Заполнение таблицы протокола
    for row in protocol_value:
        for id in id_protocol:
            if row[0] == id and row[2] != "0" and row[2] !="3" and (row[3] == equipment or equipment == "9999") and (row[4] == configuration or configuration == "9999"):
                list_protocol.append( Protocol( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            
    del id_protocol[:]
    del id_requirements[:]  
    
    for row in list_protocol:
        id_protocol.append(row.ID_Protocol)
        id_requirements.append(row.ID_Requirements)
    
    #Заполнение продукта
    for row in product_value:
        for id in id_protocol:
            if row[0] == id:
                list_product.append( Product( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
    #Заполнение сортировок
    for row in sorting_value:
        for id in id_protocol:
            if row[0] == id:        
                list_sorting.append( Sorting(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    #Заполнение проходов
    for row in accept_value:
        for id in id_protocol:
            if row[0] == id:        
                list_accept.append( AcceptReject( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    #Заполнение отбоев
    for row in reject_value:
        for id in id_protocol:
            if row[0] == id:        
                list_reject.append( AcceptReject( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    #Заполнение компонентов
    for row in list_protocol:
        for id in id_protocol:
            if row.ID_Protocol == id:
                get_protocol_component(row.ID_Protocol, row.sortingValue, row.componentValue)
    
    #Поиск фракций из требований(взято из требований)
    googlesheet_requirements.search_fraction_requirements(id_requirements)                
               
                
#Новая функция поиска данных по протоколу
def new_get_protocol_result(id_protocol):
    #Получение статичнsх данных по протоколу
    Protocol_DATA = ["Protocol!A2:K", "Product!A2:L", "Sorting!A2:H", "Accept!A2:K", "Reject!A2:K"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=ProtocolID,
		ranges=Protocol_DATA, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    
    protocol_value = valueRanges[0].get('values', [])
    product_value = valueRanges[1].get('values', [])
    sorting_value = valueRanges[2].get('values', [])
    accept_value = valueRanges[3].get('values', [])
    reject_value = valueRanges[4].get('values', [])
    
    __list_protocol = []
    __list_product = []
    __list_sorting = []
    __list_accept = []
    __list_reject = []
    __list_components = []
    
    #Заполнение таблицы протокола
    for row in protocol_value:
        if str(row[0]) == str(id_protocol):
            __list_protocol.append(Protocol( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))    
    #Заполнение таблицы продукта
    for row in product_value:
        if str(row[0]) == str(id_protocol):
            __list_product.append(Product( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))    
    #Заполнение таблицы сортировок
    for row in sorting_value:
        if str(row[0]) == str(id_protocol):
            __list_sorting.append(Sorting(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))    
    #Заполнение таблицы проходов
    for row in accept_value:
        if str(row[0]) == str(id_protocol):
            __list_accept.append(AcceptReject( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))    
    #Заполнение таблицы проходов
    for row in reject_value:
        if str(row[0]) == str(id_protocol):
            __list_reject.append(AcceptReject( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    
    #Получение динамических данных о компонентах протокола
    id_char = int(__list_protocol[0].sortingValue) * 8 + 9
    if id_char > len(charset)-1:
        id_char -= 26
        last_char = "A" + charset[id_char]
    else:
        last_char = charset[id_char]
    
    rangeComponents = 'Components!A3:'+ last_char
    
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range=rangeComponents).execute()
    components_value = result.get('values', [])
    
    for row in components_value:
        if str(row[0]) == str(id_protocol):
            __list_components.append(row)
    
    return {"ProtocolData":{
                "protocol": [table.to_dict() for table in __list_protocol],
                "product": [table.to_dict() for table in __list_product],
                "sorting": [table.to_dict() for table in __list_sorting],
                "accept": [table.to_dict() for table in __list_accept],
                "reject": [table.to_dict() for table in __list_reject],
                "components": __list_components
                }
            }
            
def protocolTopProduct():
    Data_Range = ["Protocol!A3:C","Components!A3:D"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=ProtocolID,
		ranges=Data_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    
    protocol_value = valueRanges[0].get('values', [])
    components_value = valueRanges[1].get('values', [])
    
    __list_protocolID = []
    __list_components = []
    
    #Составленияе списка айдишников протоколов(кроме тестовых)
    for row in protocol_value:
        if str(row[2]) != "0":
            __list_protocolID.append(row[0])
            
    for row in components_value:
        for id in __list_protocolID:
            if str(row[0]) == str(id):
                try:
                    temp = row[3].split('(')[0].rstrip(' ')
                except:
                    temp = "-"
                __list_components.append(temp)

    """
    for row in valueRanges[1]:
        if row[0] != "-":
            temp = row[0].split('(')[0].rstrip(' ')
            __list.append(temp)
    """            
    
    list_top_components = Counter(__list_components)
    list_top_components = sorted(list_top_components.items(), key=operator.itemgetter(1), reverse = True)
    
    return list_top_components

#Получение конкретных данных по протоколу
def get_protocol_result(id_protocol):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Protocol!A2:K').execute()
    values = result.get('values', [])
    
    for row in values:
        if str(row[0]) == str(id_protocol):
            list_protocol.append( Protocol( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            get_protocol_product(row[0])
            get_protocol_sorting(row[0])
            get_protocol_accept(row[0])
            get_protocol_reject(row[0])
            get_protocol_component(row[0], row[5], row[6])

#Получение конкретных данных по протоколу
def get_protocol(id_requirements):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Protocol!A2:K').execute()
    values = result.get('values', [])
    
    for row in values:
        if str(row[1]) == str(id_requirements):
            list_protocol.append( Protocol( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            get_protocol_product(row[0])
            get_protocol_sorting(row[0])
            get_protocol_accept(row[0])
            get_protocol_reject(row[0])
            get_protocol_component(row[0], row[5], row[6])
 
def get_protocol_product(id_protocol):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Product!A2:L').execute()
    values = result.get('values', [])

    for row in values:
        if str(row[0]) == str(id_protocol):
            list_product.append( Product( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

def get_protocol_sorting(id_protocol):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Sorting!A2:H').execute()
    values = result.get('values', [])

    for row in values:
        if int(row[0]) == int(id_protocol):
            list_sorting.append(Sorting(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        
def get_protocol_accept(id_protocol):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Accept!A2:K').execute()
    values = result.get('values', [])

    for row in values:
        if int(row[0]) == int(id_protocol):
            list_accept.append( AcceptReject( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))   
        
def get_protocol_reject(id_protocol):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Reject!A2:K').execute()
    values = result.get('values', [])

    for row in values:
        if int(row[0]) == int(id_protocol):
            list_reject.append( AcceptReject( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        
def get_protocol_component(id_protocol, sortingValue, componentValue):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Components!A3:A').execute()
    values = result.get('values', [])
    
    id_row = 3;
    
    for row in values:
        if int(row[0]) == int(id_protocol):
            break
        else:
            id_row += 1
    
    id_char = int(sortingValue) * 8 + 9
    if id_char > len(charset)-1:
        id_char -= 26
        last_char = "A" + charset[id_char]
    else:
        last_char = charset[id_char]
    
    rangeComponents = 'Components!A' + str(id_row) +":"+ last_char + str(id_row - 1 + int(componentValue))
    
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range=rangeComponents).execute()
    values = result.get('values', [])
    
    for row in values:
        component_data = {}
        for i in range(len(row)):
            name_row = "row_" + str(i)
            component_data[name_row] = row[i]
        list_components.append(component_data)
        
#маленькая функция по поиску протокола
def get_protocol_id(id_requirements, id_protocol):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Protocol!A2:B').execute()
    values = result.get('values', [])
    
    id_row = 1
    id_values = 0
    
    for row in values:
        if str(row[1]) == id_requirements:
            if int(id_protocol) == id_values:
                break
            else:
                id_values += 1
                id_row += 1
        else:
            id_row += 1
            
            
    return id_row
    
def edit_protocol(id_protocol, write_data):
    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 1834070610,
                        'dimension': 'ROWS',
                        'startIndex': int(id_protocol),
                        'endIndex': (int(id_protocol)+1)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyDeleat).execute()
    #Добавление нового числа строк 
    bodyInsert = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': 1834070610,
                        'dimension': 'ROWS',
                        'startIndex': int(id_protocol),
                        'endIndex': (int(id_protocol)+1)
                    },
                    'inheritFromBefore': True
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyInsert).execute()        
    body = {
		'values': [write_data]
	}
    
    rangeProtocol = 'Protocol!A' + str(int(id_protocol)+1) + ':K' + str(int(id_protocol)+1)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeProtocol,
    valueInputOption="USER_ENTERED", body=body).execute()   
    
def edit_sourceProduct(id_protocol, write_data):
    print(id_protocol)
    
    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 1002255392,
                        'dimension': 'ROWS',
                        'startIndex': int(id_protocol),
                        'endIndex': (int(id_protocol)+1)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyDeleat).execute()
    #Добавление нового числа строк 
    bodyInsert = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': 1002255392,
                        'dimension': 'ROWS',
                        'startIndex': int(id_protocol),
                        'endIndex': (int(id_protocol)+1)
                    },
                    'inheritFromBefore': True
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyInsert).execute()        
    body = {
		'values': [write_data]
	}
    
    rangeProduct = 'Product!A' + str(int(id_protocol)+1) + ':L' + str(int(id_protocol)+1)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeProduct,
    valueInputOption="USER_ENTERED", body=body).execute()    

def edit_sorting(id_protocol, sortong_count, write_data):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Sorting!A2:A').execute()
    values = result.get('values', [])
    
    id_row = 1;
    sortingValue = 0;
    
    #Подсчет числа строк в таблице
    for row in values:
        if str(row[0]) == str(id_protocol):
            sortingValue += 1
    #Поисх начального айдишника для вставки   
    for row in values:
        if str(row[0]) == str(id_protocol):
            break
        else:
            id_row += 1
    
    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 1800953086,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+sortingValue)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyDeleat).execute()
    #Добавление нового числа строк 
    bodyInsert = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': 1800953086,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+sortong_count)
                    },
                    'inheritFromBefore': True
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyInsert).execute()        
    body = {
		'values': write_data
	}
    
    rangeSorting = 'Sorting!A' + str(id_row+1) + ':H' + str(id_row+sortong_count)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeSorting,
    valueInputOption="USER_ENTERED", body=body).execute()
    
def edit_accept(id_protocol, sortong_count, write_data):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Accept!A2:A').execute()
    values = result.get('values', [])
    
    id_row = 1;
    sortingValue = 0;
    
    #Подсчет числа строк в таблице
    for row in values:
        if str(row[0]) == str(id_protocol):
            sortingValue += 1
    #Поисх начального айдишника для вставки   
    for row in values:
        if str(row[0]) == str(id_protocol):
            break
        else:
            id_row += 1
    
    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 1915552840,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+sortingValue)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyDeleat).execute()
    #Добавление нового числа строк 
    bodyInsert = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': 1915552840,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+sortong_count)
                    },
                    'inheritFromBefore': True
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyInsert).execute()        
    body = {
		'values': write_data
	}
    
    rangeAccept = 'Accept!A' + str(id_row+1) + ':K' + str(id_row+sortong_count)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeAccept,
    valueInputOption="USER_ENTERED", body=body).execute()
    
def edit_reject(id_protocol, sortong_count, write_data):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Reject!A2:A').execute()
    values = result.get('values', [])
    
    id_row = 1;
    sortingValue = 0;
    
    #Подсчет числа строк в таблице
    for row in values:
        if str(row[0]) == str(id_protocol):
            sortingValue += 1
    #Поисх начального айдишника для вставки   
    for row in values:
        if str(row[0]) == str(id_protocol):
            break
        else:
            id_row += 1
    
    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 697383260,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+sortingValue)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyDeleat).execute()
    #Добавление нового числа строк 
    bodyInsert = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': 697383260,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+sortong_count)
                    },
                    'inheritFromBefore': True
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyInsert).execute()        
    body = {
		'values': write_data
	}
    
    rangeReject = 'Reject!A' + str(id_row+1) + ':K' + str(id_row+sortong_count)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeReject,
    valueInputOption="USER_ENTERED", body=body).execute()
    
def edit_component(id_protocol, component_count, accept_reject_count, write_data):
    first_char, last_char = setup_char_vaule(int(accept_reject_count))
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProtocolID,
		range='Components!A3:A').execute()
    values = result.get('values', [])
    
    id_row = 2;
    componentValue = 0;
    
    #Подсчет числа строк в таблице
    for row in values:
        if str(row[0]) == str(id_protocol):
            componentValue += 1
    #Поисх начального айдишника для вставки   
    for row in values:
        if str(row[0]) == str(id_protocol):
            break
        else:
            id_row += 1
    
    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 2008015312,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+componentValue)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyDeleat).execute()
    #Добавление нового числа строк 
    bodyInsert = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': 2008015312,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+component_count)
                    },
                    'inheritFromBefore': True
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=ProtocolID, body=bodyInsert).execute()        
    body = {
		'values': write_data
	}
    
    rangeComponents = 'Components!A' + str(id_row+1) +':'+last_char + str(id_row+component_count)
    
    service.spreadsheets().values().update(
		spreadsheetId=ProtocolID, range=rangeComponents,
    valueInputOption="USER_ENTERED", body=body).execute()