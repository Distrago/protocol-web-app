# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

#SheetTable ID
Separation = "1jp9htedKPNsCymOg20CxMLPpollqfB3DemBhh3_0tAs"
NoriaStat = "1xizoXdmaqWV-z3RId2e33z_4tTzH_Dcp0fafRXRZIa8"
CommercialOffer = "1US0fKBtOT206VMnAniVXSm_AAogxGHvnkw4FZZhs1Ns"
ProductTableID = '1afsf5p-mvvFxNBPCHFSDMDk-b7Mw__WMpxsZn8ueHAY'

CSort_2 = "1dtw92GZBXcMFGxYhu_YCRKpiNcBbmTBrNQg3bdblmvY" #new bitrix system

#Table_RANGE
Model_Range = "Model!A3:L"
Main_Range = "Main!A3:R"
Configuration_Range = "Configuration!A3:G"
Kompressor_Range = "Kompressor!A3:S"
KompressorType_Range = "KompressorType!A3:G"
Price_Range = "Price!A3:F"
product_Range = 'Products!A3:E'
Conditions_Range = "Conditions!B3:F"

Aspiration_Range = "Aspiration!A2:E"
Bunker_Range = "Bunker!A2:E"
Complect_Range = "Complect!A2:D"

Lift_Range = "Lift!A3:K"
Import_Range = "Import!A3:M"
Import_Range = "Import!A3:M"

service = api_google.service_sheets

#Словарь заглавных букв латинского алфавита(для динамической записи в таблицы компонентов)
charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#
class Model:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.Model = row_data[1]
        self.Voltage = row_data[2]
        self.Hz = row_data[3]
        self.Air_MPa = row_data[4]
        self.air_class = row_data[5]
        self.defence_class = row_data[6]
        self.defence_lvl = row_data[7]
        self.temp = row_data[8]
        self.wet = row_data[9]
        self.DBA = row_data[10]        
        self.explore_time = row_data[11]             
    def to_dict(self):
        return{"id": self.id,  
               "Model": self.Model,               
               "Voltage": self.Voltage,
               "Hz": self.Hz,
               "Air_MPa": self.Air_MPa,
               "air_class": self.air_class,
               "defence_class": self.defence_class,
               "defence_lvl": self.defence_lvl,
               "temp": self.temp,
               "wet": self.wet,
               "DBA": self.DBA,
               "explore_time": self.explore_time}
list_Model = []

class Main:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.Model = row_data[1]
        self.frame = row_data[2]
        self.modelNumber = row_data[3]
        self.Channel = row_data[4]
        self.Capacity = row_data[5]
        self.Weight = row_data[6]
        self.kW = row_data[7]
        self.air_flow = row_data[8]
        self.Air_flowMax = row_data[9]
        self.aspiration = row_data[10]        
        self.description = row_data[11]       
        self.imageName = row_data[12]
        self.sizeHeight = row_data[13]
        self.sizeDeep = row_data[14]
        self.sizeWidth = row_data[15] 
        self.ModelRU = row_data[16]   
        self.descriptionEN = row_data[17]   
    def to_dict(self):
        return{"id": self.id,
               "Model": self.Model,               
               "frame": self.frame,
               "modelNumber": self.modelNumber,
               "Channel": self.Channel,
               "Capacity": self.Capacity,
               "Weight": self.Weight,               
               "kW": self.kW,
               "air_flow": self.air_flow,
               "Air_flowMax": self.Air_flowMax,
               "aspiration": self.aspiration,
               "description": self.description,
               "imageName": self.imageName,
               "sizeHeight": self.sizeHeight,
               "sizeDeep": self.sizeDeep,
               "sizeWidth": self.sizeWidth,
               "ModelRU": self.ModelRU,
               "descriptionEN": self.descriptionEN}
list_Main = []  

class Configuration:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.Model = row_data[1]
        self.configuration = row_data[2]
        self.Cleaning_factor = row_data[3]
        self.CCD = row_data[4]             
        self.Description = row_data[5]
        self.DescriptionEN = row_data[6]
    def to_dict(self):
        return{"id": self.id,
               "Model": self.Model,               
               "configuration": self.configuration,
               "Cleaning_factor": self.Cleaning_factor,
               "CCD": self.CCD,
               "Description": self.Description,
               "DescriptionEN": self.DescriptionEN}
list_Configuration = []

class Kompressor:
     def __init__(self, row_data):
        self.id = row_data[0]
        self.compressorManufacturer = row_data[1]
        self.compressorModel = row_data[2]
        self.compressorEnginePower = row_data[3]                     
        self.fullName = row_data[4]
        self.fullNameEN = row_data[5]
        self.compressorVolume = row_data[6]             
        self.compressorCapacity = row_data[7]             
        self.compressorPressure = row_data[8]             
        self.compressorVoltage = row_data[9]             
        self.compressorHz = row_data[10]             
        self.compressorPhase = row_data[11]             
        self.compressorMass = row_data[12]             
        self.compressorPrice = row_data[13]             
        self.desiccant = row_data[14]
        self.filter = row_data[15]             
        self.ressiver = row_data[16]             
        self.imageName = row_data[17]             
        self.currency = row_data[18]             
     def to_dict(self):
        return{"id": self.id,
               "compressorManufacturer": self.compressorManufacturer,               
               "compressorModel": self.compressorModel,
               "compressorEnginePower": self.compressorEnginePower,
               "fullName": self.fullName,
               "fullNameEN": self.fullNameEN,
               "compressorVolume": self.compressorVolume,
               "compressorCapacity": self.compressorCapacity,
               "compressorPressure": self.compressorPressure,
               "compressorVoltage": self.compressorVoltage,
               "compressorHz": self.compressorHz,
               "compressorPhase": self.compressorPhase,
               "compressorMass": self.compressorMass,
               "compressorPrice": self.compressorPrice,
               "desiccant": self.desiccant,
               "filter": self.filter,
               "ressiver": self.ressiver,
               "imageName": self.imageName,
               "currency": self.currency}
list_Kompressor = []

class KompressorType:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.compressor = row_data[1]
        self.seria = row_data[2]
        self.infoTitle = row_data[3]
        self.description = row_data[4]
        self.description_seria = row_data[5]
        self.option = row_data[6]
    def to_dict(self):
        return{"id": self.id,
               "compressor": self.compressor,  
               "seria": self.seria,                 
               "infoTitle": self.infoTitle,
               "description": self.description,
               "description_seria": self.description_seria,
               "option": self.option
        }
list_KompressorType = []

class Price:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.name = row_data[1]
        self.price = row_data[2]
        self.priceNDS = row_data[3]                     
        self.priceExport = row_data[4]             
         
    def to_dict(self):
        return{"id": self.id,
               "name": self.name,               
               "price": self.price,
               "priceNDS": self.priceNDS,               
               "priceExport": self.priceExport}
list_Price = []

class Product:
    def __init__(self, ID, nameProduct, k):
        self.ID = ID
        self.nameProduct = nameProduct
        self.k = k
    def to_dict(self):
        return {"ID": self.ID,
                "nameProduct": self.nameProduct,
                "k": self.k}
list_product = []

class Conditions:
    def __init__(self, row_data):
        self.termsOfPayment = row_data[0]
        self.priceIncludes = row_data[1]
        self.Commissioning = row_data[2]
        self.guarantee = row_data[3]
        self.delivery = row_data[4]
    def to_dict(self):
        return {"termsOfPayment": self.termsOfPayment,
                "priceIncludes": self.priceIncludes,
                "Commissioning": self.Commissioning,
                "guarantee": self.guarantee,
                "delivery": self.delivery}
list_Conditions = []

class Aspiration:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.type = row_data[1]
        self.lotok = row_data[2]
        self.name = row_data[3]                     
        self.price = row_data[4]             
         
    def to_dict(self):
        return{"id": self.id,
               "type": self.type,               
               "lotok": self.lotok,
               "name": self.name,               
               "price": self.price}
list_Aspiration = []

class Bunker:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.type = row_data[1]
        self.lotok = row_data[2]
        self.name = row_data[3]                     
        self.price = row_data[4]             
         
    def to_dict(self):
        return{"id": self.id,
               "type": self.type,               
               "lotok": self.lotok,
               "name": self.name,               
               "price": self.price}
list_Bunker = []

class Complect:
    def __init__(self, row_data):
        self.RU = row_data[0]
        self.EN = row_data[1]
        self.price = row_data[2]
        self.vault = row_data[3]           
         
    def to_dict(self):
        return{"RU": self.RU,
               "EN": self.EN,               
               "price": self.price,
               "vault": self.vault}
list_Complect = []

class Lift:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.mass = row_data[7]
        self.size = row_data[9]                  
        self.price = row_data[10]  
    def to_dict(self):
        return{"id": self.id,
               "mass": self.mass,              
               "size": self.size,              
               "price": self.price}    
list_Lift = []

class Import:
    def __init__(self, row_data):
        self.id = row_data[0]
        self.Model = row_data[1]
        self.Voltage = row_data[2]
        self.kW = row_data[3]
        self.mass = row_data[4]
        self.Capacity = row_data[5]
        self.imageName = row_data[6]
        self.sizeWidth = row_data[7]
        self.sizeHeight = row_data[8]
        self.sizeDeep = row_data[9]
        self.price = row_data[10]
        self.description = row_data[11]
        self.descriptionEn = row_data[12]
    def to_dict(self):
        return{"id": self.id,
               "Model": self.Model,
               "Voltage": self.Voltage,
               "kW": self.kW,
               "mass": self.mass,
               "Capacity": self.Capacity,
               "imageName": self.imageName,
               "sizeWidth": self.sizeWidth,              
               "sizeHeight": self.sizeHeight,              
               "sizeDeep": self.sizeDeep,              
               "price": self.price,              
               "description": self.description,
               "descriptionEn": self.descriptionEn}   
list_Import = []

def load_CO_Data():
    Apparat_Range = ["Model!A3:L", "Main!A3:R", "Configuration!A3:G", "Kompressor!A3:S", "KompressorType!A3:G", "Price!A3:F", "Conditions!B3:F", "Aspiration!A2:E", "Bunker!A2:E", "Complect!A2:D", "Lift!A3:K", "Import!A3:M"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=Separation, ranges = Apparat_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])# массив всех таблиц Separation
#                        (нулевой элемент массива таблицы Separation)

    #формирование массивов данных для каждой таблицы
    Model_Value = valueRanges[0].get('values', [])
    Main_Value = valueRanges[1].get('values', [])
    Configuration_Value = valueRanges[2].get('values', [])
    Kompressor_Value = valueRanges[3].get('values', [])
    KompressorType_Value = valueRanges[4].get('values', [])
    Price_Value = valueRanges[5].get('values', [])
    Conditions_Value = valueRanges[6].get('values', [])
    Aspiration_Value = valueRanges[7].get('values', [])
    Bunker_Value = valueRanges[8].get('values', [])
    Complect_Value = valueRanges[9].get('values', [])
    Lift_Value = valueRanges[10].get('values', [])
    Import_Value = valueRanges[11].get('values', [])
    

    #Заполнение массива одной таблицы
    for row in Model_Value:       
        list_Model.append(Model(row))
        
    for row in Main_Value:       
        list_Main.append(Main(row))
        
    for row in Configuration_Value:
        list_Configuration.append(Configuration(row))

    for row in Kompressor_Value:
        list_Kompressor.append(Kompressor(row))
        
    for row in KompressorType_Value:
        list_KompressorType.append(KompressorType(row))
    
    for row in Price_Value:
        list_Price.append(Price(row))

    for row in Conditions_Value:
        list_Conditions.append(Conditions(row))
    
    for row in Aspiration_Value:         
      list_Aspiration.append(Aspiration(row))

    for row in Bunker_Value:       
        list_Bunker.append(Bunker(row))
        
    for row in Complect_Value:
        list_Complect.append(Complect(row))  

    for row in Lift_Value:
        list_Lift.append(Lift(row))
    
    for row in Import_Value:
        list_Import.append(Import(row))
        
        
def search_Elevator(id_deal, id_CO):
    Elevator_date = ['ModelCSZE!A3:AW', 'ModelCSE!A3:AN', 'ModelCSCC!A3:AQ']
    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=NoriaStat, ranges = Elevator_date, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
        
    CSZE_Value = valueRanges[0].get('values', [])
    CSE_Value = valueRanges[1].get('values', [])    
    CSCC_Value = valueRanges[2].get('values', [])
      
    list_Elevator = []    
    
    for row in CSZE_Value:
        if str(row[0]) == str(id_deal) and str(row[3]) == str(id_CO):
            list_Elevator.append(row)

    for row in CSE_Value:
        if str(row[0]) == str(id_deal) and str(row[3]) == str(id_CO):
            list_Elevator.append(row)
                      
    for row in CSCC_Value:
        if str(row[0]) == str(id_deal) and str(row[3]) == str(id_CO):
            list_Elevator.append(row)
            
    CSort_2_Noria = ['ModelCSZE!A3:AX', 'ModelCSE!A3:AO', 'ModelCSCC!A3:AR']
    result = sheet.values().batchGet(spreadsheetId=CSort_2, ranges = CSort_2_Noria, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
        
    CSZE_Value = valueRanges[0].get('values', [])
    CSE_Value = valueRanges[1].get('values', [])    
    CSCC_Value = valueRanges[2].get('values', [])

    for row in CSZE_Value:
        if str(row[0]) == str(id_deal) and str(row[3]) == str(id_CO):
            row.pop(7)
            list_Elevator.append(row)

    for row in CSE_Value:
        if str(row[0]) == str(id_deal) and str(row[3]) == str(id_CO):
            row.pop(7)
            list_Elevator.append(row)
                      
    for row in CSCC_Value:
        if str(row[0]) == str(id_deal) and str(row[3]) == str(id_CO):
            row.pop(7)
            list_Elevator.append(row)
                      
    return list_Elevator

def product_k():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=ProductTableID,
                                range=product_Range).execute()
    values = result.get('values', [])
  
    for row in values:        
        list_product.append(Product(row[0], row[1], row[3]))
        
#Получение информации по элементам комерческого предложения если оно существует
def load_CO_Elements(id_task, id_offer,economicModel):
    EconomicModel = []
    list_ColorSorter = []
    list_Compressor = []
    list_Elevator = []
    list_Protocol = []
    list_Other = []
    list_Lift = []
    list_Import = []
    
    #работа с таблицей
    CommercialOffer_Range = ["Offer!A2:H", "ColorSorter!A2:H", "Compressor!A2:H", "Elevator!A2:I", "Protocol!A2:F", "Other!A2:H", "Lift!A2:H", "Import!A2:H"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=CommercialOffer, ranges = CommercialOffer_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    
    Offer_Value = valueRanges[0].get('values', [])
    ColorSorter_Value = valueRanges[1].get('values', [])
    Compressor_Value = valueRanges[2].get('values', [])
    Elevator_Value = valueRanges[3].get('values', [])
    Protocol_Value = valueRanges[4].get('values', [])
    Other_Value = valueRanges[5].get('values', [])
    lift_Value = valueRanges[6].get('values', [])
    Import_Value = valueRanges[7].get('values', [])
    
    for row in Offer_Value:
        if row[0] == id_task and row[1] == id_offer and row[7] == "TRUE":
            if row[6] != economicModel:
                EconomicModel.append(0)
            else:
                EconomicModel.append(1) 
    for row in ColorSorter_Value:
        if row[0] == id_task and row[1] == id_offer and row[7] == "TRUE":
            list_ColorSorter.append(row);    
    for row in Compressor_Value:
        if row[0] == id_task and row[1] == id_offer and row[7] == "TRUE":
            list_Compressor.append(row);   
    for row in Elevator_Value:
        if row[0] == id_task and row[1] == id_offer and row[8] == "TRUE":
            list_Elevator.append(row);    
    for row in Protocol_Value:
        if row[0] == id_task and row[1] == id_offer and row[5] == "TRUE":
            list_Protocol.append(row);   
    for row in Other_Value:
        if row[0] == id_task and row[1] == id_offer and row[7] == "TRUE":
            list_Other.append(row)
    for row in lift_Value:
        if row[0] == id_task and row[1] == id_offer and row[7] == "TRUE":
            list_Lift.append(row)
    for row in Import_Value:
        if row[0] == id_task and row[1] == id_offer and row[7] == "TRUE":
            list_Import.append(row)
            
    return {"economic_model": EconomicModel,
            "list_ColorSorter": list_ColorSorter,
            "list_Compressor": list_Compressor,
            "list_Elevator": list_Elevator,
            "list_Protocol": list_Protocol,
            "list_Other": list_Other,
            "list_Lift": list_Lift,
            "list_Import": list_Import}
    

#Работа с сохранением комерческих предложений
def write_statictic(write_data, managerName, managerDistrict):
    list_ColorSorter = []
    list_Compressor = []
    list_Elevator = []
    list_Protocol = []
    list_Other = []
    list_Lift = []
    list_Import = []

    id_task = None
    id_offer = None
    price = 0.00
    discount = 0.00
    data = None

    for row in write_data:
        if row[1].split(": ")[1] == "ColorSorter":
            id_task = row[5].split(": ")[1]
            id_offer = row[4].split(": ")[1]
            price = price + (float(row[7].split(": " )[1]) * float(row[0].split(": ")[1]))
            discount = discount + float(row[3].split(": " )[1])
            data = row[2].split(": ")[1]
            list_ColorSorter.append([row[5].split(": ")[1], row[4].split(": ")[1], row[6].split(": ")[1], row[0].split(": ")[1], row[7].split(": " )[1], row[3].split(": " )[1], row[2].split(": " )[1], row[8].split(": " )[1]])
        if row[1].split(": ")[1] == "Compressor":
            id_task = row[5].split(": ")[1]
            id_offer = row[4].split(": ")[1]
            price = price + (float(row[7].split(": " )[1]) * float(row[0].split(": ")[1]))
            discount = discount + float(row[3].split(": " )[1])
            data = row[2].split(": ")[1]
            list_Compressor.append([row[5].split(": ")[1], row[4].split(": ")[1], row[6].split(": ")[1], row[0].split(": ")[1], row[7].split(": " )[1], row[3].split(": " )[1], row[2].split(": " )[1], row[8].split(": " )[1]])
        if row[1].split(": ")[1] == "Elevator":
            id_task = row[6].split(": ")[1]
            id_offer = row[5].split(": ")[1]
            price = price + (float(row[8].split(": " )[1]) * float(row[0].split(": ")[1]))
            discount = discount + float(row[3].split(": ")[1])
            data = row[2].split(": ")[1]
            list_Elevator.append([row[6].split(": ")[1], row[5].split(": ")[1], row[4].split(": ")[1], row[7].split(": ")[1], row[0].split(": " )[1], row[8].split(": ")[1], row[3].split(": " )[1], row[2].split(": " )[1], row[9].split(": " )[1]])
        if row[0].split(": ")[1] == "Protocol":
            id_task = row[4].split(": ")[1]
            id_offer = row[2].split(": ")[1]
            data = row[1].split(": ")[1]
            list_Protocol.append([row[4].split(": ")[1], row[2].split(": ")[1], row[3].split(": ")[1], row[5].split(": ")[1], row[1].split(": ")[1], row[6].split(": ")[1]])
        if row[1].split(": ")[1] == "Other":
            id_task = row[5].split(": ")[1]
            id_offer = row[4].split(": ")[1]
            price = price + (float(row[7].split(": " )[1]) * float(row[0].split(": ")[1]))
            discount = discount + float(row[3].split(": " )[1])
            data = row[2].split(": ")[1]
            list_Other.append([row[5].split(": ")[1], row[4].split(": ")[1], row[6].split(": ")[1], row[0].split(": " )[1], row[7].split(": ")[1], row[3].split(": ")[1], row[2].split(": ")[1], row[8].split(": ")[1]])
        # расшифровка аякс части для лифтов
        if row[1].split(": ")[1] == "Lift":
            id_task = row[5].split(": ")[1]
            id_offer = row[4].split(": ")[1]
            price = price + (float(row[7].split(": " )[1]) * float(row[0].split(": ")[1]))
            discount = discount + float(row[3].split(": " )[1])
            data = row[2].split(": ")[1]
            list_Lift.append([row[5].split(": ")[1], row[4].split(": ")[1], row[6].split(": ")[1], row[0].split(": " )[1], row[7].split(": ")[1], row[3].split(": ")[1], row[2].split(": ")[1], row[8].split(": ")[1]])
        if row[1].split(": ")[1] == "Import":
            print(row)
            id_task = row[5].split(": ")[1]
            id_offer = row[4].split(": ")[1]
            price = price + (float(row[7].split(": " )[1]) * float(row[0].split(": ")[1]))
            discount = discount + float(row[3].split(": " )[1])
            data = row[2].split(": ")[1]
            list_Import.append([row[5].split(": ")[1], row[4].split(": ")[1], row[6].split(": ")[1], row[0].split(": " )[1], row[7].split(": ")[1], row[3].split(": ")[1], row[2].split(": ")[1], row[8].split(": ")[1]])
             
    #работа с таблицей
    CommercialOffer_Range = ["Offer!A2:H", "ColorSorter!A2:H", "Compressor!A2:H", "Elevator!A2:I", "Protocol!A2:F", "Other!A2:H", "Lift!A2:H", "Import!A2:H"]

    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=CommercialOffer, ranges = CommercialOffer_Range, valueRenderOption="FORMATTED_VALUE", dateTimeRenderOption="FORMATTED_STRING").execute()
    valueRanges = result.get('valueRanges', [])
    
    Offer_Value = valueRanges[0].get('values', [])
    ColorSorter_Value = valueRanges[1].get('values', [])
    Compressor_Value = valueRanges[2].get('values', [])
    Elevator_Value = valueRanges[3].get('values', [])
    Protocol_Value = valueRanges[4].get('values', [])
    Other_Value = valueRanges[5].get('values', [])
    lift_Value = valueRanges[6].get('values', [])
    Import_Value = valueRanges[7].get('values', [])

    for row in Offer_Value:
        if row[0] == id_task and row[1] == id_offer:
            row[7] = False    
    for row in ColorSorter_Value:
        if row[0] == id_task and row[1] == id_offer:
            row[7] = False    
    for row in Compressor_Value:
        if row[0] == id_task and row[1] == id_offer:
            row[7] = False    
    for row in Elevator_Value:
        if row[0] == id_task and row[1] == id_offer:
            row[8] = False    
    for row in Protocol_Value:
        if row[0] == id_task and row[1] == id_offer:
            row[5] = False    
    for row in Other_Value:
        if row[0] == id_task and row[1] == id_offer:
            row[7] = False
    for row in lift_Value:
        if row[0] == id_task and row[1] == id_offer:
            row[7] = False
    for row in Import_Value:
        if row[0] == id_task and row[1] == id_offer:
            row[7] = False

    list_offer = [id_task, id_offer, price, discount, data,  managerName, managerDistrict, True]
    
    JoinOffer = Offer_Value + [list_offer]
    service.spreadsheets().values().update(
		spreadsheetId=CommercialOffer, range="Offer!A2:H",
    valueInputOption="USER_ENTERED", body= {'values': JoinOffer}).execute() 
    
    JoinColorSorter = ColorSorter_Value + list_ColorSorter
    service.spreadsheets().values().update(
		spreadsheetId=CommercialOffer, range="ColorSorter!A2:H",
    valueInputOption="USER_ENTERED", body={'values': JoinColorSorter}).execute()    
    
    JoinCompressor = Compressor_Value + list_Compressor
    service.spreadsheets().values().update(
		spreadsheetId=CommercialOffer, range="Compressor!A2:H",
    valueInputOption="USER_ENTERED", body={'values': JoinCompressor}).execute()    
    
    JoinElevator = Elevator_Value + list_Elevator
    service.spreadsheets().values().update(
		spreadsheetId=CommercialOffer, range="Elevator!A2:I",
    valueInputOption="USER_ENTERED", body={'values': JoinElevator}).execute()    
    
    JoinProtocol = Protocol_Value + list_Protocol
    service.spreadsheets().values().update(
		spreadsheetId=CommercialOffer, range="Protocol!A2:F",
    valueInputOption="USER_ENTERED", body={'values': JoinProtocol}).execute()
    
    JoinOther = Other_Value + list_Other
    service.spreadsheets().values().update(
		spreadsheetId=CommercialOffer, range="Other!A2:H",
    valueInputOption="USER_ENTERED", body={'values': JoinOther}).execute()

    JoinOther = lift_Value + list_Lift
    service.spreadsheets().values().update(
		spreadsheetId=CommercialOffer, range="Lift!A2:H",
    valueInputOption="USER_ENTERED", body={'values': JoinOther}).execute()

    JoinOther = Import_Value + list_Import
    service.spreadsheets().values().update(
		spreadsheetId=CommercialOffer, range="Import!A2:H",
    valueInputOption="USER_ENTERED", body={'values': JoinOther}).execute()
    
    return list_offer
    
#Общая функция загрузки таблиц
def upload_google_table():
    load_CO_Data()
    product_k()
     
#Генерация массива массивов
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() )
    return list_of_objects    
#append-добавление элемента в список массива
