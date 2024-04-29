# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

#SheetTable ID
Separation = "15VLhY5sXYOBtF4vBsuiGObCx2T5jKqHS4Kw4E3f3DWE"

#Table_RANGE
#не обязательно указывать тк указаны в основной функции

service = api_google.service_sheets

#Словарь заглавных букв латинского алфавита(для динамической записи в таблицы компонентов)
charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#
class Model:
    def __init__(self, row_data):
        self.id_group = row_data[0]
        self.id = row_data[1]
        self.manufacturer = row_data[2]
        self.series = row_data[3]
        self.model = row_data[4]
        self.trays = row_data[5]
        self.priceNoneNDS = row_data[6]            
        self.customs = row_data[7]            
        self.imported = row_data[8]            
    def to_dict(self):
        return{"id_group": self.id_group,  
               "id": self.id,               
               "manufacturer": self.manufacturer,
               "series": self.series,
               "model": self.model,
               "trays": self.trays,
               "priceNoneNDS": self.priceNoneNDS,
               "customs": self.customs,
               "imported": self.imported}
list_Model = []

class Dillers:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.id_group = row_data[1]
        self.dillers = row_data[2]
                   
    def to_dict(self):
        return{"id": self.id,  
               "id_group": self.id_group,               
               "dillers": self.dillers}
list_Dillers = []


def load_Competitor_Data():
    Competitor_Range = ["Model!A2:I", "Dillers!A2:C"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=Separation, ranges = Competitor_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])# массив всех таблиц Separation
#                        (нулевой элемент массива таблицы Separation)

    #формирование массивов данных для каждой таблицы
    Model_Value = valueRanges[0].get('values', [])
    Dillers_Value = valueRanges[1].get('values', [])

    #Заполнение массива одной таблицы
    for row in Model_Value:       
        list_Model.append(Model(row))
    
    for row in Dillers_Value:       
        list_Dillers.append(Dillers(row))

  
#Общая функция загрузки таблиц
def upload_google_table():
    load_Competitor_Data()
     
#Генерация массива массивов
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() )
    return list_of_objects    
#append-добавление элемента в список массива
