# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google


#SheetTable ID
IndustryID = "1eH_W1aeHS2jrIkydEGqUD_cwH4AFRC67xFm2YedduLQ"
ProductClassifier_MainID = "17HyLLDxIoj0dNmXbsWZ-q0QfAnfYoIYjcM99ODXUXBE"
ProductClassifier_SortID = "1cJQyfgBJTelWhFvhI0g95hUv0Mcukq5KLPR5MHiX1IQ"
ClassifierTempID = "1Zs98EF0KBVydQ69GLH1X8JJMFK-GN5NNviE2Of4Rzm4"
WeedClassifier_MainID = "1Cewk2Y8XL5uHCRXnJgzMQjYK1RCzvQuHfNSrGPqmDRQ"
#Table_RANGE
ClassifierTemp_Range = "temp!A2:O"
Category_Range = "Category!A2:B"
Class_Range = "Class!A2:C"
Weed_Range = "WeedName!A2:D"
DescriptionWeed_Range = "DescriptionProduct!A2:D"
#Industry
Industry_Range = "Industry!A2:C"
#ProductClassifier_Main
ProductGroup_Range = "ProductGroup!A2:C"
Product_Range = "Product!A2:J"
ProductType_Range = "ProductType!A2:C"
Purpose_Range = "Purpose!A2:B"
GOST_Range = "GOST!A2:D"
Segment_Range = "Segment!A2:B"
Region_Range = "Region!A2:B"
#Industry
Industry_Range = "Industry!A2:C"
Machine_Range = "Machine!A2:L"
Configuration_Range = "Configuration!A2:B"

ProductPart_Range = "ProductPart!A2:C"
ProductStatus_Range = "ProductStatus!A2:C"
ProductColor_Range = "ProductColor!A2:C"

#ProductClassifier_Sort

#Google API service
service = api_google.service_sheets

#Class(table)
class Industry:
    def __init__(self, row_data):
        self.ID_Industry = row_data[0]
        self.industryName = row_data[1]
        self.table_link = row_data[2]
    def to_dict(self):
        return {"ID_Industry": self.ID_Industry,
                "industryName": self.industryName,
                "table_link": self.table_link}
list_industry = []

class ProductGroup:
    def __init__(self, row_data):
        self.ID_ProductGroup = row_data[0]
        self.productGroupName = row_data[1]
        self.purpose_list = row_data[2]
    def to_dict(self):
        return {"ID_ProductGroup": self.ID_ProductGroup,
                "productGroupName": self.productGroupName,
                "purpose_list": self.purpose_list}
list_productGroup = []

class Product:
    def __init__(self, row_data):
        self.ID_Product = row_data[0]
        self.ID_ProductGroup = row_data[1]
        self.productName = row_data[2]
        self.wikilink = row_data[3]
        self.description = row_data[4]
        self.mass_of_1000 = row_data[5]
        self.size = row_data[6]
        self.purpose_seed = row_data[7]
        self.purpose_fodder = row_data[8]
        self.purpose_raw = row_data[9]
        self.purpose_export = row_data[10]
        self.purpose_groats = row_data[11]
    def to_dict(self):
        return{"ID_Product": self.ID_Product,
               "ID_ProductGroup": self.ID_ProductGroup,
               "productName": self.productName,
               "wikilink": self.wikilink,
               "description": self.description,
               "mass_of_1000": self.mass_of_1000,
               "size": self.size,
               "purpose_seed": self.purpose_seed,
               "purpose_fodder": self.purpose_fodder,
               "purpose_raw": self.purpose_raw,
               "purpose_export": self.purpose_export,
               "purpose_groats": self.purpose_groats}
list_product = []
               
class ProductType:
    def __init__(self, row_data):
        self.ID_ProductType = row_data[0]
        self.ID_Product = row_data[1]
        self.productTypeName = row_data[2]
    def to_dict(self):
        return{"ID_ProductType": self.ID_ProductType,
               "ID_Product": self.ID_Product,
               "productTypeName": self.productTypeName}
list_productType = []

class Purpose:
    def __init__(self,row_data):
        self.ID_Purpose = row_data[0]
        self.purposeName = row_data[1]
    def to_dict(self):
        return{"ID_Purpose": self.ID_Purpose,
               "purposeName": self.purposeName}
list_purpose = []

class GOST:
    def __init__(self,row_data):
        self.ID_gost = row_data[0]
        self.gostName = row_data[1]
        self.description = row_data[2]
        self.link = row_data[3]
    def to_dict(self):
        return {"ID_gost": self.ID_gost,
                "gostName": self.gostName,
                "description": self.description,
                "link": self.link}
list_gost = []

class Segment:
    def __init__(self,row_data):
        self.ID_Segment = row_data[0]
        self.segmentName = row_data[1]
    def to_dict(self):
        return {"ID_Segment": self.ID_Segment,
                "segmentName": self.segmentName}
list_segment = []

class Region:
    def __init__(self,row_data):
        self.ID_Region = row_data[0]
        self.regionName = row_data[1]
    def to_dict(self):
        return {"ID_Region": self.ID_Region,
                "regionName": self.regionName}
list_region = []

class Category:
    def __init__(self,row_data):
        self.ID_Category = row_data[0]
        self.category = row_data[1]
    def to_dict(self):
        return {"ID_Category": self.ID_Category,
                "category": self.category}
list_category = []

class ClassWeed:
    def __init__(self,row_data):
        self.ID_Class = row_data[0]
        self.ID_Category = row_data[1]
        self.className = row_data[2]
    def to_dict(self):
        return {"ID_Class": self.ID_Class,
                "ID_Category": self.ID_Category,
                "className": self.className}
list_classWeed = []

class Weed:
    def __init__(self,row_data):
        self.ID_Weed = row_data[0]
        self.ID_Class = row_data[1]
        self.weedName = row_data[2]
        self.weedMass = row_data[3]
    def to_dict(self):
        return {"ID_Weed": self.ID_Weed,
                "ID_Class": self.ID_Class,
                "weedName": self.weedName,
                "weedMass": self.weedMass,}
list_weed = [] 
 
class DescriptionWeed:
    def __init__(self,row_data):
        self.ID_Description = row_data[0]
        self.ID_Category = row_data[1]
        self.ID_Class = row_data[2]
        self.descriptionName = row_data[3]
    def to_dict(self):
        return {"ID_Description": self.ID_Description,
                "ID_Category": self.ID_Category,
                "ID_Class": self.ID_Class,
                "descriptionName": self.descriptionName}
list_description = []

class Machine:
    def __init__(self, row_data):
        self.id_machine = row_data[0]
        self.machineName = row_data[1]
        self.id_configration = row_data[2]
        self.gabarit = row_data[3]
        self.col1 = row_data[4]
        self.col2 = row_data[5]
        self.col3 = row_data[6]
        self.col4 = row_data[7]
        self.col5 = row_data[8]
        self.col6 = row_data[9]
        self.col7 = row_data[10]
        self.id_industry = row_data[11]
    def to_dict(self):
        return{"id_machine": self.id_machine,
               "machineName": self.machineName, 
               "id_configration": self.id_configration,
               "gabarit": self.gabarit,
               "col1": self.col1,
               "col2": self.col2,
               "col3": self.col3,
               "col4": self.col4,
               "col6": self.col6,
               "col7": self.col7,
               "id_industry": self.id_industry,               
              }
list_machine = []

class Configuration:
    def __init__(self, row_data):
        self.id_configuration = row_data[0]
        self.configuration = row_data[1]      
    def to_dict(self):
        return{"id_configuration": self.id_configuration,
               "configuration": self.configuration,
               }
list_configuration = []

class ProductPart:
    def __init__(self, row_data):
        self.id_group = row_data[0]
        self.id_number = row_data[1]
        self.productPart = row_data[2]
    def to_dict(self):
        return {"id_group": self.id_group,
                "id_number": self.id_number,
                "productPart": self.productPart}
list_productPart = []

class ProductStatus:
    def __init__(self, row_data):
        self.id_group = row_data[0]
        self.id_number = row_data[1]
        self.productStatus = row_data[2]
    def to_dict(self):
        return {"id_group": self.id_group,
                "id_number": self.id_number,
                "productStatus": self.productStatus}
list_productStatus = []

class ProductColor:
    def __init__(self, row_data):
        self.id_group = row_data[0]
        self.id_number = row_data[1]
        self.productColor = row_data[2]
    def to_dict(self):
        return {"id_group": self.id_group,
                "id_number": self.id_number,
                "productColor": self.productColor}
list_productColor = []

def load_ProductClassifier_MainID():
    ProductMainID_Range = ["ProductGroup!A2:C", "Product!A2:L", "ProductType!A2:C", "Purpose!A2:B", "GOST!A2:D", "Region!A2:B", "ProductPart!A2:C", "ProductStatus!A2:C", "ProductColor!A2:C"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=ProductClassifier_MainID, ranges = ProductMainID_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
 
    ProductGroup_Value = valueRanges[0].get('values', [])
    Product_Value = valueRanges[1].get('values', [])
    ProductType_Value = valueRanges[2].get('values', [])
    Purpose_Value = valueRanges[3].get('values', [])
    GOST_Value = valueRanges[4].get('values', [])
    Region_Value = valueRanges[5].get('values', [])   
    ProductPart_Value = valueRanges[6].get('values', [])
    ProductStatus_Value = valueRanges[7].get('values', [])
    ProductColor_Value = valueRanges[8].get('values', [])
    
    for row in ProductGroup_Value:       
        list_productGroup.append(ProductGroup(row))
        
    for row in Product_Value:       
        list_product.append(Product(row))
        
    for row in ProductType_Value:
        list_productType.append(ProductType(row))

    for row in Purpose_Value:
        list_purpose.append(Purpose(row))
        
    for row in GOST_Value:
        list_gost.append(GOST(row))

    for row in Region_Value:
        list_region.append(Region(row))

    for row in ProductPart_Value:
        list_productPart.append(ProductPart(row))
    
    for row in ProductStatus_Value:
        list_productStatus.append(ProductStatus(row))
    
    for row in ProductColor_Value:
        list_productColor.append(ProductColor(row))
        
    #print(unicode("Таблицы продуктов подгруженны", 'cp1251'))

def load_WeedClassifier():
    WeedClassifier_Range = ["Category!A2:B",  "Class!A2:C", "WeedName!A2:D", "DescriptionProduct!A2:D"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId = WeedClassifier_MainID, ranges = WeedClassifier_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
 
    Category_Value = valueRanges[0].get('values', [])
    ClassWeed_Value = valueRanges[1].get('values', [])
    Weed_Value = valueRanges[2].get('values', [])
    Description_Value = valueRanges[3].get('values', [])
   
    for row in Category_Value:       
        list_category.append(Category(row))
        
    for row in ClassWeed_Value:       
        list_classWeed.append(ClassWeed(row))
        
    for row in Weed_Value:
        list_weed.append(Weed(row))

    for row in Description_Value:
        list_description.append(DescriptionWeed(row))
        
    #print(unicode("Таблицы засорителей подгруженны", 'cp1251'))

def load_Industry():
    IndustryID_Range = ["Industry!A2:C", "Machine!A2:L", "Configuration!A2:B"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=IndustryID, ranges = IndustryID_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
 
    Industry_Value = valueRanges[0].get('values', [])
    Machine_Value = valueRanges[1].get('values', [])
    Configuration_Value = valueRanges[2].get('values', [])

    for row in Industry_Value:       
        list_industry.append(Industry(row))        
     
    for row in Machine_Value:
        list_machine.append(Machine(row))

    for row in Configuration_Value:       
        list_configuration.append(Configuration(row))

    #print(unicode("Таблицы конфигураций подгруженны", 'cp1251'))

#READ FUNCTION
def classifier_useADD(write_data, length):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ClassifierTempID,
		range='temp!A2:A').execute()
    values = result.get('values', [])
  
    id_row = len(values) + 2
    
    bodyWrite = {
		'values': write_data
	}        
    rangeClassifierTemp = 'temp!A' + str(id_row) + ':O' + str(id_row + length)
    
    service.spreadsheets().values().update(
		spreadsheetId=ClassifierTempID, range=rangeClassifierTemp,
    valueInputOption="USER_ENTERED", body=bodyWrite).execute()   

def classifier_getADD(id_list):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ClassifierTempID,
		range='temp!A2:O').execute()
    values = result.get('values', [])
    
    list_classifier = []
    
    for id in id_list:
        for row in values:
            if str(row[0]) == id:
                temp_row = row
                
        list_classifier.append(temp_row)
    
    return list_classifier

        
def upload_google_table():
    load_ProductClassifier_MainID()
    load_WeedClassifier()
    load_Industry()