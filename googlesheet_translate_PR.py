# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

#SheetTable ID
ProtocolTranslate = "120hDWv46zAwhwA825E2uMJAPdZgtaKo2-FrQ7yvgWb0"


#Table_RANGE
Title_Range = "Title!A2:C"
Req_Range = "Req!A2:C"
Prot_Range = "Prot!A2:C"
Sort_Range = "Sort!A2:C"
Econom_Range = "Econom!A2:C"

service = api_google.service_sheets

#Словарь заглавных букв латинского алфавита(для динамической записи в таблицы компонентов)
charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#
class Title:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
list_Title = []

class Req:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
        
list_Req = []  

class Prot:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
        
list_Prot = []  

class Sort:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
        
list_Sort = []  

class Econom:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.RU = row_data[1]
        self.EN = row_data[2]
    def to_dict(self):
        return{"id": self.id,  
               "RU": self.RU,
               "EN": self.EN}
        
list_Econom = [] 

def load_Prot_Translate():
    Translate_Range = ["Title!A2:C", "Req!A2:C", "Prot!A2:C", "Sort!A2:C", "Econom!A2:C"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=ProtocolTranslate, ranges = Translate_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])# массив всех таблиц TranslateFile
#                        (нулевой элемент массива таблицы TranslateFile)

    #формирование массивов данных для каждой таблицы
    Title_Value = valueRanges[0].get('values', [])
    Req_Value = valueRanges[1].get('values', [])
    Prot_Value = valueRanges[2].get('values', [])
    Sort_Value = valueRanges[3].get('values', [])
    Econom_Value = valueRanges[4].get('values', [])
    
 
    #Заполнение массива одной таблицы
    for row in Title_Value:       
        list_Title.append(Title(row))
        
    for row in Req_Value:       
        list_Req.append(Req(row))

    for row in Prot_Value:       
        list_Prot.append(Prot(row))

    for row in Sort_Value:
        list_Sort.append(Sort(row))   
    
    for row in Econom_Value:
        list_Econom.append(Econom(row))
   
    
#Общая функция загрузки таблиц
def upload_google_table():
    load_Prot_Translate()
    # print(list_Title[0].to_dict())
     
#Генерация массива массивов
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() )
    return list_of_objects    
#append-добавление элемента в список массива
