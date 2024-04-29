# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

#ProductClassifire_Sort/ table id
ProductClassifire_Sort = "1cJQyfgBJTelWhFvhI0g95hUv0Mcukq5KLPR5MHiX1IQ"
#Table Range
Sort_Range = "Sort!A2:G"
Grainfeed_Range = "Grainfeed!A2:G"
Cereal_Range = "Cereal!A2:G"
Legumes_Range = "Legumes!A2:G"
Corn_Range = "Corn!A2:G"
Foragelegumes_Range = "Foragelegumes!A2:G"
Legumesherbs_Range = "Legumesherbs!A2:G"
Cerealherbs_Range = "Cerealherbs!A2:G"
Silo_Range = "Silo!A2:G"
Arid_Range = "Arid!A2:G"
Oilseeds_Range = "Oilseeds!A2:G"
Technical_Range = "Technical!A2:G"
Spinning_Range = "Spinning!A2:G"
Essentialoil_Range = "Essentialoil!A2:G"
Medicinal_Range = "Medicinal!A2:G"
Melliferous_Range = "Melliferous!A2:G"
Potatoes_Range = "Potatoes!A2:G"
Vegetable_Range = "Vegetable!A2:G"
Melons_Range = "Melons!A2:G"
Mushrooms_Range = "Mushrooms!A2:G"
Fruitpomefruits_Range = "Fruitpomefruits!A2:G"
Fruitstonefruits_Range = "Fruitstonefruits!A2:G"
Berry_Range = "Berry!A2:G"
Grapes_Range = "Grapes!A2:G"
Citrusandsubtropical_Range = "Citrusandsubtropical!A2:G"
Floraldecorative_Range = "Floraldecorative!A2:G"
Forest_Range = "Forest!A2:G"
Fodderrootcrops_Range = "Fodderrootcrops!A2:G"

service = api_google.service_sheets

class Sort:
    def __init__ (self, id_type, Sort_TM, Sort_code, Sort_name, Sort_Year, Sort_Region, Sort_Patent):
        self.id_type = id_type
        self.Sort_TM = Sort_TM
        self.Sort_code = Sort_code
        self.Sort_name = Sort_name
        self.Sort_Year = Sort_Year
        self.Sort_Region = Sort_Region
        self.Sort_Patent = Sort_Patent
    def to_dict(self):
        return{
          "id_type" : self.id_type,  
          "Sort_TM" : self.Sort_TM,
          "Sort_code" : self.Sort_code,  
          "Sort_name" : self.Sort_name, 
          "Sort_Year" : self.Sort_Year,  
          "Sort_Region" : self.Sort_Region,  
          "Sort_Patent" : self.Sort_Patent}
list_Sort = []
list_Grainfeed = []
list_Cereal = []
list_Legumes = []
list_Corn = []
list_Foragelegumes = []
list_Legumesherbs = []
list_Cerealherbs = []
list_Silo = []
list_Arid = []
list_Oilseeds = []
list_Technical = []
list_Spinning = []
list_Essentialoil = []
list_Medicinal = []
list_Melliferous = []
list_Potatoes = []
list_Vegetable = []
list_Melons = []
list_Mushrooms = []
list_Fruitpomefruits = []
list_Fruitstonefruits = []
list_Berry = []
list_Grapes = []
list_Citrusandsubtropical = []
list_Floraldecorative = []
list_Forest = []
list_Fodderrootcrops = []

def read_Sort(object_range, object_list, table_name):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProductClassifire_Sort,
                                range=object_range).execute()
    values = result.get('values', [])

    for row in values:
        object_list.append(Sort(row [0], row[1], row[2], row[3], row[4], row[5], row[6]))
    
    print(('������� '+str(table_name)+' ����������!', 'cp1251'))

def upload_google_table():
    read_Sort(Sort_Range, list_Sort, '����')
    read_Sort(Grainfeed_Range, list_Grainfeed, "Grainfeed")
    read_Sort(Cereal_Range, list_Cereal, "Cereal")
    read_Sort(Legumes_Range, list_Legumes, "Legumes")
    read_Sort(Corn_Range, list_Corn, "Corn")
    read_Sort(Foragelegumes_Range, list_Foragelegumes, "Foragelegumes")
    read_Sort(Legumesherbs_Range, list_Legumesherbs, "Legumesherbs")
    read_Sort(Cerealherbs_Range, list_Cerealherbs, "Cerealherbs")
    read_Sort(Silo_Range, list_Silo, "Silo")
    read_Sort(Arid_Range, list_Arid, "Arid")
    read_Sort(Oilseeds_Range, list_Oilseeds, "Oilseeds")
    read_Sort(Technical_Range, list_Technical, "Technical")
    read_Sort(Spinning_Range, list_Spinning, "Spinning")
    read_Sort(Essentialoil_Range, list_Essentialoil, "Essentialoil")
    read_Sort(Medicinal_Range, list_Medicinal, "Medicinal")
    read_Sort(Melliferous_Range, list_Melliferous, "Melliferous")
    read_Sort(Potatoes_Range, list_Potatoes, "Potatoes")
    read_Sort(Vegetable_Range, list_Vegetable, "Vegetable")
    read_Sort(Melons_Range, list_Melons, "Melons")
    read_Sort(Mushrooms_Range, list_Mushrooms, "Mushrooms")
    read_Sort(Fruitpomefruits_Range, list_Fruitpomefruits, "Fruitpomefruits")
    read_Sort(Fruitstonefruits_Range, list_Fruitstonefruits, "Fruitstonefruits")
    read_Sort(Berry_Range, list_Berry, "Berry")
    read_Sort(Grapes_Range, list_Grapes, "Grapes")
    read_Sort(Citrusandsubtropical_Range, list_Citrusandsubtropical, "Citrusandsubtropical")
    read_Sort(Floraldecorative_Range, list_Floraldecorative, "Floraldecorative")
    read_Sort(Forest_Range, list_Forest, "Forest")
    read_Sort(Fodderrootcrops_Range, list_Fodderrootcrops, "Fodderrootcrops")