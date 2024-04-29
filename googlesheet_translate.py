# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

#SheetTable ID
TranslateFile = "1LCh1mFVN1XgH_IAaIMH6EvvySmtBLUQg7e_y2SWcuWg"


#Table_RANGE
Total_Range = "Total!A2:C"
FirstPage_Range = "FirstPage!A2:C"
SpecifMenu_Range = "SpecifMenu!A2:C"
Specification_Range = "Specification!A2:C"
Delivery_Range = "Delivery!A2:C"
SmartSort_Range = "SmartSort!A2:C"
Lift_Range = "Lift!A2:C"
Compressor_Range = "Compressor!A2:J"
CompressorP_Range = "CompressorP!A2:C"
Elevators_Range = "Elevators!A2:C"

service = api_google.service_sheets

#Словарь заглавных букв латинского алфавита(для динамической записи в таблицы компонентов)
charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#
class Total:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
list_Total = []

class FirstPage:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
        
list_FirstPage = []  

class SpecifMenu:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
list_SpecifMenu = []

class Specification:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
list_Specification = []

class Delivery:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
list_Delivery = []

class SmartSort:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
list_SmartSort = []

class Lift:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
list_Lift = []

class Compressor:
    def __init__(self, row_data):
        self.compressor = row_data[0]
        self.seria = row_data[1]
        self.infoTitle = row_data[2]
        self.infoTitleEN = row_data[3]
        self.description = row_data[4]
        self.descriptionEN = row_data[5]
        self.description_seria = row_data[6]
        self.description_seriaEN = row_data[7]
        self.option = row_data[8]
        self.optionEN = row_data[9]
    def to_dict(self):
        return{"compressor": self.compressor,  
               "seria": self.seria,
               "infoTitle": self.infoTitle,
               "infoTitleEN": self.infoTitleEN,
               "description": self.description,
               "descriptionEN": self.descriptionEN,
               "description_seria": self.description_seria,
               "description_seriaEN": self.description_seriaEN,
               "option": self.option,
               "optionEN": self.optionEN}
list_Compressor = []

class CompressorP:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
list_CompressorP = []

class Elevators:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
list_Elevators = []


def load_CO_Translate():
    Translate_Range = ["Total!A2:C", "FirstPage!A2:C", "SpecifMenu!A2:C", "Specification!A2:C", "Delivery!A2:C", "SmartSort!A2:C", "Lift!A2:C", "Compressor!A2:J", "CompressorP!A2:C", "Elevators!A2:C"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=TranslateFile, ranges = Translate_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])# массив всех таблиц TranslateFile
#                        (нулевой элемент массива таблицы TranslateFile)

    #формирование массивов данных для каждой таблицы
    Total_Value = valueRanges[0].get('values', [])
    FirstPage_Value = valueRanges[1].get('values', [])
    SpecifMenu_Value = valueRanges[2].get('values', [])
    Specification_Value = valueRanges[3].get('values', [])
    Delivery_Value = valueRanges[4].get('values', [])
    SmartSort_Value = valueRanges[5].get('values', [])
    Lift_Value = valueRanges[6].get('values', [])
    Compressor_Value = valueRanges[7].get('values', [])
    CompressorP_Value = valueRanges[8].get('values', [])
    Elevators_Value = valueRanges[9].get('values', [])
    

    #Заполнение массива одной таблицы
    for row in Total_Value:       
        list_Total.append(Total(row))
        
    for row in FirstPage_Value:       
        list_FirstPage.append(FirstPage(row))
        
    for row in SpecifMenu_Value:
        list_SpecifMenu.append(SpecifMenu(row))

    for row in Specification_Value:
        list_Specification.append(Specification(row))
        
    for row in Delivery_Value:
        list_Delivery.append(Delivery(row))
    
    for row in SmartSort_Value:
        list_SmartSort.append(SmartSort(row))
        
    for row in Lift_Value:
        list_Lift.append(Lift(row))
   
    for row in Compressor_Value:
        list_Compressor.append(Compressor(row))

    for row in CompressorP_Value:
        list_CompressorP.append(CompressorP(row))

    for row in Elevators_Value:
        list_Elevators.append(Elevators(row))
   
    
#Общая функция загрузки таблиц
def upload_google_table():
    load_CO_Translate()
     
#Генерация массива массивов
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() )
    return list_of_objects    
#append-добавление элемента в список массива
