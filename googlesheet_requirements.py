# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

#SheetTable ID
RequestProtocolID = "1b0h1I4O47ZtKj9UkLiASbdJCfj505749r3d-lZWvE6w"
#Table_RANGE
Requirements_Range = "Requirements!A2:W"
Fractions_Range = "Fractions!A2:K"

service = api_google.service_sheets

#Словарь заглавных букв латинского алфавита(для динамической записи в таблицы компонентов)
charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#RequestProtocol
class Requirements:
    def __init__(self, ID_user, ID_deal, ID_requirements, equipment, configuration, program, productName, ID_product, selection_value, selection_type, photoFolder, ID_mainPhoto, capacity_value, capacity_type, time_value, time_type, hour_in_day, day_in_week, month_in_year, fraction_count, companent_count, create_date, company_name):
        self.ID_user = ID_user
        self.ID_deal = ID_deal
        self.ID_requirements = ID_requirements
        self.equipment = equipment
        self.configuration = configuration
        self.program = program
        self.productName = productName
        self.ID_product = ID_product
        self.selection_value = selection_value
        self.selection_type = selection_type
        self.photoFolder = photoFolder
        self.ID_mainPhoto = ID_mainPhoto
        self.capacity_value = capacity_value
        self.capacity_type = capacity_type
        self.time_value = time_value
        self.time_type = time_type
        self.hour_in_day = hour_in_day
        self.day_in_week = day_in_week
        self.month_in_year = month_in_year
        self.fraction_count = fraction_count
        self.companent_count = companent_count
        self.create_date = create_date
        self.company_name = company_name
    def to_dict(self):
        return{"ID_user": self.ID_user,
               "ID_deal": self.ID_deal,
               "ID_requirements": self.ID_requirements,
               "equipment": self.equipment,
               "configuration": self.configuration,
               "program": self.program,
               "productName": self.productName,
               "ID_product": self.ID_product,
               "selection_value": self.selection_value,
               "selection_type": self.selection_type,
               "photoFolder": self.photoFolder,
               "ID_mainPhoto": self.ID_mainPhoto,
               "capacity_value": self.capacity_value,
               "capacity_type": self.capacity_type,
               "time_value": self.time_value,
               "time_type": self.time_type,
               "hour_in_day": self.hour_in_day,
               "day_in_week": self.day_in_week,
               "month_in_year": self.month_in_year,
               "fraction_count": self.fraction_count,
               "companent_count": self.companent_count,
               "create_date": self.create_date,
               "company_name": self.company_name}
list_requirements = []

class Fraction:
    def __init__(self, ID_requirements, ID_fraction, fraction_name, main_fraction, purpose, exit, purity, capacity, comment, photoFolder, ID_mainPhoto):
        self.ID_requirements = ID_requirements
        self.ID_fraction = ID_fraction
        self.fraction_name = fraction_name
        self.main_fraction = main_fraction
        self.purpose = purpose
        self.exit = exit
        self.purity = purity
        self.capacity = capacity
        self.comment = comment
        self.photoFolder = photoFolder
        self.ID_mainPhoto = ID_mainPhoto
    def to_dict(self):
        return{"ID_requirements": self.ID_requirements,
               "ID_fraction": self.ID_fraction,
               "fraction_name": self.fraction_name,
               "main_fraction": self.main_fraction,
               "purpose": self.purpose,
               "exit": self.exit,
               "purity": self.purity,
               "capacity": self.capacity,
               "comment": self.comment,
               "photoFolder": self.photoFolder,
               "ID_mainPhoto": self.ID_mainPhoto}
list_fraction = []  
list_components = []     

#Запись данных в таблицы
"""
def write_requirements_protocol(id_requirements, equipment, configuration, program, productName, id_product, photoFolder, id_mainPhoto, capacity_value, capacity_type, fraction_count, component_count):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Requirements!C1:C').execute()
    values = result.get('values', [])
    
    write_values = [
        [
           id_requirements,
           equipment,
           configuration,
           program,
           productName,
           id_product,
           photoFolder,
           id_mainPhoto,
           capacity_value,
           capacity_type,
           fraction_count,
           component_count 
		]
	]
    body = {
		'values': write_values
	}
    
    rangeRequirements = 'Requirements!C' + str(len(values) + 1) + ':N' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=RequestProtocolID, range=rangeRequirements,
    valueInputOption="USER_ENTERED", body=body).execute()

def write_fraction_requirements_protocol(id_requirements, id_fraction, fraction_name, purpose, exit, purity, capacity, comment, photoFolder, id_mainPhoto):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Fractions!A1:A').execute()
    values = result.get('values', [])
    
    write_values = [
        [
            id_requirements,
            id_fraction,
            fraction_name,
            purpose,
            exit,
            purity,
            capacity,
            comment,
            photoFolder,
            id_mainPhoto
		]
	]
    body = {
		'values': write_values
	}
    
    rangeFractions = 'Fractions!A' + str(len(values) + 1) + ':J' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=RequestProtocolID, range=rangeFractions,
    valueInputOption="USER_ENTERED", body=body).execute()

def write_component_mainInfo(id_requirements, component_number, companent_name, id_companent, component_value, component_type, component_valid_check, component_remove_check, photoFolder, id_mainPhoto):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Components!A1:A').execute()
    values = result.get('values', [])
        
    write_values = [
        [
            id_requirements,
            component_number,
            companent_name,
            id_companent,
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
		spreadsheetId=RequestProtocolID, range=rangeComponents,
    valueInputOption="USER_ENTERED", body=body).execute()

def write_companent_fractionInfo(id_fraction, str_number, companent_value, unit_type, component_valid_check, component_warnin_check):
    first_char, last_char = setup_char_vaule(int(id_fraction))

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Components!A1:A').execute()
    values = result.get('values', [])
    
    write_values = [
        [
            companent_value,
            unit_type,
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
		spreadsheetId=RequestProtocolID, range=rangeComponents,
    valueInputOption="USER_ENTERED", body=body).execute()
"""
def setup_char_vaule(id_fraction):
    id_charset = 6 + (id_fraction*4)
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

#Получение фракций для системы поиска
def search_fraction_requirements(id_array):    
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Fractions!A2:K').execute()
    values = result.get('values', [])
    
    for row in values:
        for id in id_array:
            if row[0] == id:
                list_fraction.append( Fraction( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

#Новая функция поиска данных по требованиям
def new_get_requirements(id_requirements):
    #Получение статичнsх данных по требованиям
    Requirements_DATA = ["Requirements!A2:W",'Fractions!A2:K']

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=RequestProtocolID,
		ranges=Requirements_DATA, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    
    requirements_value = valueRanges[0].get('values', [])
    fraction_value = valueRanges[1].get('values', [])
    
    __list_requirements = []
    __list_fraction = []
    __list_components = []
    
    #Заполнение таблицы требований
    for row in requirements_value:
        if str(row[2]) == str(id_requirements):
            __list_requirements.append(Requirements(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22]))
    #Заполнение таблицы фракций
    for row in fraction_value:
        if str(row[0]) == str(id_requirements):
            __list_fraction.append( Fraction( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
                    
    #Получение динамических данных о компонентах требований
    id_char = int(__list_requirements[0].fraction_count) * 8 + 9
    if id_char > len(charset)-1:
        id_char -= 26
        last_char = "A" + charset[id_char]
    else:
        last_char = charset[id_char]
    
    rangeComponents = 'Components!A3:'+ last_char
    
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range=rangeComponents).execute()
    components_value = result.get('values', [])
    
    for row in components_value:
        if str(row[0]) == str(id_requirements):
            __list_components.append(row)

    return {"RequrementsData":{
                "requirements": [table.to_dict() for table in __list_requirements],
                "fraction": [table.to_dict() for table in __list_fraction],
                "components": __list_components
                }
            }
#Получение конкретных данных по требованиям
def get_requirements(id_requirements):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Requirements!A2:W').execute()
    values = result.get('values', [])
    
    for row in values:
        if str(row[2]) == str(id_requirements):
            list_requirements.append(Requirements(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22]))
            get_fractionm(row[2])
            get_component(row[2], row[19], row[20])
 
def get_fractionm(id_requirements):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Fractions!A2:K').execute()
    values = result.get('values', [])
    
    for row in values:
        if str(row[0]) == str(id_requirements):
            list_fraction.append( Fraction( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

def get_component(id_requirements, fractionValue, componentValue):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Components!A3:A').execute()
    values = result.get('values', [])
    
    id_row = 3;
    
    for row in values:
        if str(row[0]) == str(id_requirements):
            break
        else:
            id_row += 1
    
    id_char = int(fractionValue) * 8 + 9
    if id_char > len(charset)-1:
        id_char -= 26
        last_char = "A" + charset[id_char]
    else:
        last_char = charset[id_char]
    
    rangeComponents = 'Components!A' + str(id_row) +":"+ last_char + str(id_row - 1 + int(componentValue))
    
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range=rangeComponents).execute()
    values = result.get('values', [])
    
    for row in values:
        component_data = {}
        for i in range(len(row)):
            name_row = "row_" + str(i)
            component_data[name_row] = row[i]
        list_components.append(component_data)
        
def edit_requirements(id_requirements, write_data):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Requirements!C2:C').execute()
    values = result.get('values', [])
    
    id_row = 1;
    
    for row in values:
        if str(row[0]) == str(id_requirements):
            break
        else:
            id_row += 1
    #Удаление старого числа строк
    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 1834070610,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+1)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=RequestProtocolID, body=bodyDeleat).execute()
    #Добавление нового числа строк 
    bodyInsert = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': 1834070610,
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
        spreadsheetId=RequestProtocolID, body=bodyInsert).execute()        
    body = {
		'values': [write_data]
	}
    
    rangeRequirements = 'Requirements!A' + str(id_row+1) + ':W' + str(id_row+1)
    
    service.spreadsheets().values().update(
		spreadsheetId=RequestProtocolID, range=rangeRequirements,
    valueInputOption="USER_ENTERED", body=body).execute()
       
def edit_fraction(id_requirements, fraction_count, write_data):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Fractions!A2:A').execute()
    values = result.get('values', [])
    
    id_row = 1;
    fractionValue = 0;
    
    #Подсчет числа строк в таблице
    for row in values:
        if str(row[0]) == str(id_requirements):
            fractionValue += 1
    #Поисх начального айдишника для вставки   
    for row in values:
        if str(row[0]) == str(id_requirements):
            break
        else:
            id_row += 1    
    #Удаление старого числа строк
    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 1915552840,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+fractionValue)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=RequestProtocolID, body=bodyDeleat).execute()
    #Добавление нового числа строк 
    bodyInsert = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': 1915552840,
                        'dimension': 'ROWS',
                        'startIndex': id_row,
                        'endIndex': (id_row+fraction_count)
                    },
                    'inheritFromBefore': True
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=RequestProtocolID, body=bodyInsert).execute()
    #Комплексная Запись(в будущем для всех элеменотов, возможно)
    bodyWrite = {
		'values': write_data
	}        
    rangeFractions = 'Fractions!A' + str(id_row+1) + ':K' + str(id_row+fraction_count)
    
    service.spreadsheets().values().update(
		spreadsheetId=RequestProtocolID, range=rangeFractions,
    valueInputOption="USER_ENTERED", body=bodyWrite).execute()

def edit_component(id_requirements, component_count, fraction_count, write_data):
    first_char, last_char = setup_char_vaule(int(fraction_count))
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestProtocolID,
		range='Components!A3:A').execute()
    values = result.get('values', [])
    
    id_row = 2;
    componentValue = 0;
    
    #Подсчет числа строк в таблице
    for row in values:
        if str(row[0]) == str(id_requirements):
            componentValue += 1
    #Поисх начального айдишника для вставки   
    for row in values:
        if str(row[0]) == str(id_requirements):
            break
        else:
            id_row += 1    
    #Удаление старого числа строк
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
        spreadsheetId=RequestProtocolID, body=bodyDeleat).execute()
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
        spreadsheetId=RequestProtocolID, body=bodyInsert).execute()
    #Комплексная Запись(в будущем для всех элеменотов, возможно)
    bodyWrite = {
		'values': write_data
	}        
    rangeComponents = 'Components!A' + str(id_row+1) +':'+last_char + str(id_row+component_count)
    
    service.spreadsheets().values().update(
		spreadsheetId=RequestProtocolID, range=rangeComponents,
    valueInputOption="USER_ENTERED", body=bodyWrite).execute()      