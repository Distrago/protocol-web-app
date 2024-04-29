# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

from datetime import datetime
#SheetTable ID
dragPlan = "1extEPG0Oj4aJQpmHNGBDNe8rc_YBEfi4JnBepE7ALbw"

#Table_RANGE
Project_Stage_Range = "Project_Stage!A2:D"
Project_SubStage_Range = "Project_SubStage!A2:D"
Project_Date_Range = "Project_Date!A3:H"
# Project_Plane_DataCheck_Range = "Project_Plane_DataCheck!A2:E"
service = api_google.service_sheets
#Словарь заглавных букв латинского алфавита(для динамической записи в таблицы компонентов)
charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Class(table)
"""Классы для таблицы подгружаемых из гугла"""
class Project_Stage:
    def __init__(self, row_data):
        self.apparat = row_data[0]
        self.machine = row_data[1]
        self.Commissioning = row_data[2]
        self.SPM = row_data[3]
    def to_dict(self):
        return{"apparat": self.apparat,
               "machine": self.machine,
               "Commissioning": self.Commissioning,
               "SPM": self.SPM}
list_Project_Stage = []

class Project_SubStage:
    def __init__(self, row_data):
        self.apparat = row_data[0]
        self.machine = row_data[1]
        self.Commissioning = row_data[2]
        self.SPM = row_data[3]
    def to_dict(self):
        return{"apparat": self.apparat,
               "machine": self.machine,
               "Commissioning": self.Commissioning,
               "SPM": self.SPM}
list_Project_SubStage = []

class Project_Date:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.project = row_data[1]
        self.projectName = row_data[2]
        self.week = row_data[3]
        self.projectType = row_data[4]
        self.stage = row_data[5]
        self.stageMore = row_data[6]
        self.planeData = row_data[7]
    def to_dict(self):
        return{"id": self.id,  
               "project": self.project,
               "projectName": self.projectName,
               "week": self.week,
               "projectType": self.projectType,
               "stage": self.stage,
               "stageMore": self.stageMore,
               "planeData": self.planeData}
list_Project_Date = []

# class Project_Plane_DataCheck:
#     def __init__(self, row_data):
#         self.id = row_data[0]
#         self.planeData = row_data[1]
#         self.Hide = row_data[2]
#         self.fakeDiv = row_data[3]
#         self.emptyWeek = row_data[4]
#     def to_dict(self):
#         return{"id": self.id,
#                "planeData": self.planeData,
#                "Hide": self.Hide,
#                "fakeDiv": self.fakeDiv,
#                "emptyWeek": self.emptyWeek}
# list_Project_Plane_DataCheck = []

#Функции для загрузки данных
def load_data_calendar():
    DnD_DATA_Range = ["Project_Stage!A2:D", "Project_SubStage!A2:D"]

    sheet = service.spreadsheets()

    result = sheet.values().batchGet(spreadsheetId=dragPlan,
		ranges=DnD_DATA_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    
    #выгрузка данных листа таблицы
    calendar_Stage_value = valueRanges[0].get('values', [])
    calendar_SubStage_value = valueRanges[1].get('values', [])
    # calendar_Plane_DataCheck_value = valueRanges[2].get('values', [])
    
    list_Stage = init_list_of_objects(len(calendar_Stage_value[0]))
    list_SubStage = init_list_of_objects(len(calendar_SubStage_value[0]))
    # list_Plane_DataCheck = init_list_of_objects(len(calendar_Plane_DataCheck_value[0]))

    # Заполнение листа стадий
    for row in calendar_Stage_value:
        for i in range(len(row)):
            if(row[i] != ""):
                list_Stage[i].append(row[i])            
    list_Project_Stage.append(Project_Stage(list_Stage))

    for row in calendar_SubStage_value:
        for i in range(len(row)):
            if(row[i] != ""):
                list_SubStage[i].append(row[i])
    list_Project_SubStage.append(Project_SubStage(list_SubStage))

    # for row in calendar_Plane_DataCheck_value:
    #     for i in range(len(row)):
    #         if(row[i] != ""):
    #             list_Plane_DataCheck[i].append(row[i])
    # list_Project_Plane_DataCheck.append(Project_Plane_DataCheck(list_Plane_DataCheck))
    
def refresh_Data_Project():
    del list_Project_Date[:]
    DnD_DATA_Range = ["Project_Date!A3:H"]

    sheet = service.spreadsheets()

    result = sheet.values().batchGet(spreadsheetId=dragPlan,
		ranges=DnD_DATA_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])

    calendar_Date_value = valueRanges[0].get('values', [])

    for row in calendar_Date_value:
       list_Project_Date.append(Project_Date(row))
#Смотри
def update_calendar(write_data):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=dragPlan,
		range='Project_Date!A3:H').execute()
    values = result.get('values', [])
    
    list_data = []
    #Проверка совпадений
    for row in values:
        for list in write_data:
            if row[3] == list[2] and row[4] == list[3] and row[6] == list[5]:
                list.insert(0, row[0])
                list_data.append(list)
                break
            if list == write_data[len(write_data)-1]:
                list_data.append(row)
    
    #Добавление оставшихся элементов
    id = len(values)
    for list in write_data:
        if len(list) == 7:
            list.insert(0, str(id))
            list_data.append(list)
            id = id + 1
    
    #Перезапись таблицы
    service.spreadsheets().values().update(
		spreadsheetId=dragPlan, range='Project_Date!A3:H',
    valueInputOption="USER_ENTERED", body={'values': list_data}).execute()
    
    return list_data     


#Генерация массива массивов
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() )
    return list_of_objects