# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

#SheetTable ID
ClassificationTableID = "1tgncyt99QU_z4rqAgIUqaKloP4t7LRsU7EbjZqgwI9Y";
ProductTableID = "1zF4_rNfMfAILf3ar0c26OOOgMx380pOwiA2ZPYtyPcE";

#Protocol
RequestID = "1fjFxDg2c6fcPkkGA5YIiRCbFYEkzJO7cb_hAw-DfA24";

#Table_RABGE
productName_Range = "ProductName!A2:G"
productDescription_Range = "ProductDescription!A2:E"
weedName_Range = "WeedName!A2:G"
weedDescription_Range = "WeedDescription!A2:C"

product_Range = "Product!A2:C"
productPurpose_Range = "ProductPurpose!A2:B"

service = api_google.service_sheets

#Словарь заглавных букв латинского алфавита(для динамической записи в таблицы компонентов)
charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Class(table)
"""Классы для таблицы подгружаемых из гугла"""

#Requesr
"""Таблицы Основного/Исходного продукта"""
class PaternProduct:
    def __init__(self, ID_Product, ID_ProductGroup, product):
        self.ID_Product = ID_Product
        self.ID_ProductGroup = ID_ProductGroup
        self.product = product
    def to_dict(self):
		return {"ID_Product": self.ID_Product,
				"ID_ProductGroup": self.ID_ProductGroup,
				"product": self.product}
list_patern_product = []

class PaternProductPurpose:
    def __init__(self, ID_Purpose, purpose):
        self.ID_Purpose = ID_Purpose
        self.purpose = purpose
    def to_dict(self):
		return {"ID_Purpose": self.ID_Purpose,
				"purpose": self.purpose}
list_patern_product_purpose = []

"""Таблицы для классификаций продукта"""
class ProductName:
    def __init__(self, ID_Product, ID_Name, product, addName, minM, maxM, M):
        self.ID_Product = ID_Product
        self.ID_Name = ID_Name
        self.product = product
        self.addName = addName
        self.minM = minM
        self.maxM = maxM
        self.M = M
    def to_dict(self):
		return {"ID_Product": self.ID_Product,
				"ID_Name": self.ID_Name,
				"product": self.product,
				"addName": self.addName,
				"minM": self.minM,
				"maxM": self.maxM,
				"M": self.M}
list_product_name = []

class ProductDescription:
    def __init__(self, ID_Description, ID_Class, description, percent_M, ID_Products):
        self.ID_Description = ID_Description
        self.ID_Class = ID_Class
        self.description = description
        self.percent_M = percent_M
        self.ID_Products = ID_Products
    def to_dict(self):
        return{"ID_Description": self.ID_Description,
               "ID_Class": self.ID_Class,
               "description": self.description,
               "percent_M": self.percent_M,
               "ID_Products": self.ID_Products}
list_product_description = []

class WeedName:
    def __init__(self, ID_Weed, ID_Class, ID_Name, weed, minM, maxM, M):
        self.ID_Weed = ID_Weed
        self.ID_Class = ID_Class
        self.ID_Name = ID_Name
        self.weed = weed
        self.minM = minM
        self.maxM = maxM
        self.M = M
    def to_dict(self):
        return{"ID_Weed": self.ID_Weed,
               "ID_Class": self.ID_Class,
               "ID_Name": self.ID_Name,
               "weed": self.weed,
               "minM": self.minM,
               "maxM": self.maxM,
               "M": self.M}
list_weed_name = []

class WeedDescription:
    def __init__(self, ID_Description, ID_Class, description):
        self.ID_Description = ID_Description
        self.ID_Class = ID_Class
        self.description = description
    def to_dict(self):
        return{"ID_Description": self.ID_Description,
               "ID_Class": self.ID_Class,
               "description": self.description}
list_weed_description = []

#Result
class Result_Requirements:
    def __init__(self, ID_protocol, ID_requirements, product, purpose, purity_percent, photo_link, capacity, fraction_count, companent_count):
        self.ID_protocol = ID_protocol
        self.ID_requirements = ID_requirements
        self.product = product
        self.purpose = purpose
        self.purity_percent = purity_percent
        self.photo_link = photo_link
        self.capacity = capacity
        self.fraction_count = fraction_count
        self.companent_count = companent_count
    def to_dict(self):
        return{"ID_protocol": self.ID_protocol,
               "ID_requirements": self.ID_requirements,
               "product": self.product,
               "purpose": self.purpose,
               "purity_percent": self.purity_percent,
               "photo_link": self.photo_link,
               "capacity": self.capacity,
               "fraction_count": self.fraction_count,
               "companent_count": self.companent_count}
requirements = None

class Result_Fraction:
    def __init__(self, ID_requirements, ID_fraction, ID_valid_itemBlock, fraction_name, selection, exit, purity_percent, capacity, comment, photo_fraction):
        self.ID_requirements = ID_requirements
        self.ID_fraction = ID_fraction
        self.ID_valid_itemBlock = ID_valid_itemBlock
        self.fraction_name = fraction_name
        self.selection = selection
        self.exit = exit
        self.purity_percent = purity_percent
        self.capacity = capacity
        self.photo_fraction = photo_fraction
    def to_dict(self):
        return{"ID_requirements": self.ID_requirements,
               "ID_fraction": self.ID_fraction,
               "ID_valid_itemBlock": self.ID_valid_itemBlock,
               "fraction_name": self.fraction_name,
               "selection": self.selection,
               "exit": self.exit,
               "purity_percent": self.purity_percent,
               "capacity": self.capacity,
               "photo_fraction": self.photo_fraction}
requirements_fraction = []
requirements_companent = []

#Main Code
"""Подключение гугл таблиц"""
def product_name():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ClassificationTableID,
                                range=productName_Range).execute()
    values = result.get('values', []) 
    for row in values:
        list_product_name.append( ProductName( row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    print(unicode('Таблица Классификации продукта подгружена!', 'cp1251'))

def product_description():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ClassificationTableID,
                                range=productDescription_Range).execute()
    values = result.get('values', []) 
    for row in values:
        list_product_description.append( ProductDescription( row[0], row[1], row[2], row[3], row[4]))
    print(unicode('Таблица Классификации описания продукта подгружена!', 'cp1251'))

def weed_name():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ClassificationTableID,
                                range=weedName_Range).execute()
    values = result.get('values', []) 
    for row in values:
        list_weed_name.append( WeedName( row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    print(unicode('Таблица Классификации засорителей подгружена!', 'cp1251'))

def weed_description():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ClassificationTableID,
                                range=weedDescription_Range).execute()
    values = result.get('values', []) 
    for row in values:
        list_weed_description.append( WeedDescription( row[0], row[1], row[2]))
    print(unicode('Таблица Классификации описания засорителей подгружена!', 'cp1251')) 
  
def patern_product():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProductTableID,
                                range=product_Range).execute()
    values = result.get('values', []) 
    for row in values:
        list_patern_product.append( PaternProduct( row[0], row[1], row[2] ))
    print(unicode('Таблица основных типов продукта подгружена!', 'cp1251'))

def patern_product_purpose():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProductTableID,
                                range=productPurpose_Range).execute()
    values = result.get('values', []) 
    for row in values:
        list_patern_product_purpose.append( PaternProductPurpose( row[0], row[1]))
    print(unicode('Таблица назначения основных типов продукта подгружена!', 'cp1251'))    

#Загрузка таблиц гугл(важная функция!!)
def upload_google_table(): 
    product_name()
    product_description()
    weed_name()
    weed_description()
    
    patern_product()
    patern_product_purpose()

#Запись в таблицу результатов
def write_requirements_request(id_protocol, name_product, purpose_product, main_product_percent, photo_product, capacity, fraction_count, companent_count, comment):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestID,
		range='Requirements!C1:C').execute()
    values = result.get('values', [])
    
    id_requirements = len(values);
    
    if id_protocol == "":
        id_protocol = id_requirements
    
    write_values = [
        [
            id_protocol,
            id_requirements,
            "-",
            "-",
            "-",
            name_product,
            purpose_product,
            main_product_percent,
            photo_product,
            capacity,
            fraction_count,
            companent_count,
            "-",
            comment
		]
	]
    body = {
		'values': write_values
	}
    
    rangeRequirements = 'Requirements!B' + str(len(values) + 1) + ':O' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=RequestID, range=rangeRequirements,
    valueInputOption="USER_ENTERED", body=body).execute()
    
    
    return id_requirements;

def write_fractions_request(id_requirements, id_fraction, id_valid_itemBlock, fraction_name, selection, exit, purity_percent, capacity, comment, photo_fraction):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestID,
		range='Fractions!A1:A').execute()
    values = result.get('values', [])
    
    write_values = [
        [
            id_requirements,
            id_fraction,
            id_valid_itemBlock,
            fraction_name,
            selection,
            exit,
            purity_percent,
            capacity,
            comment,
            photo_fraction
		]
	]
    body = {
		'values': write_values
	}
    
    rangeFractions = 'Fractions!A' + str(len(values) + 1) + ':J' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=RequestID, range=rangeFractions,
    valueInputOption="USER_ENTERED", body=body).execute()
    
def write_companent_mainInfo_request(id_requirements, id_companent, companent_name, companent_description, companent_value, unit_type, companent_valid_check, companent_photo):    
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestID,
		range='Components!A1:A').execute()
    values = result.get('values', [])
    
    
    write_values = [
        [
            id_requirements,
            id_companent,
            companent_name,
            companent_description,
            companent_value,
            unit_type,
            companent_valid_check,
            companent_photo
        ]
    ]
    body = {
		'values': write_values
	}
    
    rangeComponents = 'Components!A' + str(len(values) + 1) + ':H' + str(len(values) + 1)
    
    service.spreadsheets().values().update(
		spreadsheetId=RequestID, range=rangeComponents,
    valueInputOption="USER_ENTERED", body=body).execute()    

def write_component_fractionInfo_request(id_fraction, str_number, companent_value, unit_type, companent_valid_check, companent_warnin_check):
    first_char, last_char = setup_char_vaule(int(id_fraction))

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestID,
		range='Components!A1:A').execute()
    values = result.get('values', [])
    
    write_values = [
        [
            companent_value,
            unit_type,
            companent_valid_check,
            companent_warnin_check
        ]
    ]
    body = {
        'values': write_values
    }
    
    line_number = str(len(values) - int(str_number))
    rangeComponents = 'Components!' + first_char + line_number +":"+ last_char + line_number
    
    service.spreadsheets().values().update(
		spreadsheetId=RequestID, range=rangeComponents,
    valueInputOption="USER_ENTERED", body=body).execute()  
   

def setup_char_vaule(id_fraction):
    id_charset = 4 + (id_fraction*4)
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
    
    return first_char, last_char

#Получение данных из таблиц результатов
def get_requirements_result(id_result):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestID,
		range='Requirements!B2:B').execute()
    values = result.get('values', [])
    
    id_row = 2; 
    
    for row in values:
        if str(row[0]) == str(id_result):
            break
        else:
            id_row += 1
    
    rangeRequirements = 'Requirements!B' + str(id_row) + ':O' + str(id_row)
    
    result = sheet.values().get(spreadsheetId=RequestID,
		range=rangeRequirements).execute()
    values = result.get('values', [])
    
    for row in values:
        requirements = Result_Requirements(row[0], row[1], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
    
    get_fraction_result(requirements)
    get_companent_result(requirements)
    
    return requirements.to_dict()
    
def get_fraction_result(data):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestID,
		range='Fractions!A2:A').execute()
    values = result.get('values', [])
    
    id_row = 2;
    
    for row in values:
        if int(row[0]) == int(data.ID_requirements):
            break
        else:
            id_row += 1
    
    rangeFractions = 'Fractions!A' + str(id_row) + ':J' + str(id_row -1 + int(data.fraction_count))
    
    result = sheet.values().get(spreadsheetId=RequestID,
		range=rangeFractions).execute()
    values = result.get('values', [])
    
    del requirements_fraction[:]
    
    for row in values:
        requirements_fraction.append(Result_Fraction(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

def get_companent_result(data):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=RequestID,
		range='Components!A3:A').execute()
    values = result.get('values', [])
    
    id_row = 3;
    
    for row in values:
        if int(row[0]) == int(data.ID_requirements):
            break
        else:
            id_row += 1
    
    id_char = int(data.fraction_count) * 4 + 7
    if id_char > len(charset)-1:
        id_char -= len(charset)
        last_char = "А" + charset[id_char]
    else:
        last_char = charset[id_char]
    
    rangeComponents = 'Components!A' + str(id_row) +":"+ last_char + str(id_row - 1 + int(data.companent_count))
    
    result = sheet.values().get(spreadsheetId=RequestID,
		range=rangeComponents).execute()
    values = result.get('values', [])
    
    del requirements_companent[:]
    
    for row in values:
        companent_data = {}
        for i in range(len(row)):
            name_row = "row_" + str(i)
            companent_data[name_row] = row[i]
        requirements_companent.append(companent_data)