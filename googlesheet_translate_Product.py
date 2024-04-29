# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

#SheetTable ID
TranslateFile = "1WKxOrsqwx8puwMO2yBv6QTuHe12bZb8Iml5QgwFTQRY"


#Table_RANGE
List_Range = "List!A2:D"

service = api_google.service_sheets

#Словарь заглавных букв латинского алфавита(для динамической записи в таблицы компонентов)
charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#
class List:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.id_group = row_data[1]
        self.RU = row_data[2]
        self.EN = row_data[3]
    def to_dict(self):
        return{"id": self.id,
               "id_group": self.id_group,
               "RU": self.RU,
               "EN": self.EN}
list_List = []

def load_CO_Translate_Product():
    Translate_Range = ["List!A2:D"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=TranslateFile, ranges = Translate_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])# массив всех таблиц TranslateFile
#                        (нулевой элемент массива таблицы TranslateFile)

    #формирование массивов данных для каждой таблицы
    List_Value = valueRanges[0].get('values', [])
    

    #Заполнение массива одной таблицы
    for row in List_Value:       
        list_List.append(List(row))
    
    
#Общая функция загрузки таблиц
def upload_google_table():
    load_CO_Translate_Product()
     
#Генерация массива массивов
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() )
    return list_of_objects    
#append-добавление элемента в список массива
