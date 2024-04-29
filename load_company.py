#from logging import exception
import io
import os
import json
# import os.path
import api_google

from datetime import datetime
from datetime import timedelta

web_path = 'https://csort-request.ru/static/web_data/'
local_path = 'https://127.0.0.1:5000/static/web_data/'
#Google API service
service = api_google.service_sheets
requestStat = '1N1uVaydScxLqON1A-ft_JcA2FLNGDHqIt24wN7KnUDY'
#Table_RANGE
Model_Range = "stat!A3:R"

MYDIR = os.path.dirname(__file__)
# id+	data+	number	type+	sort+	product	weed+	original_percent+	product_percent+ 	weed_percent+	exit+	capacity+

def create_Data(idDoc):
    motherMassive = []

    data = open_file(MYDIR + "/static/web_data/" + idDoc + "/" + idDoc + ".json")
    file_mod_date = datetime.fromtimestamp(os.path.getmtime(MYDIR + "/static/web_data/" + idDoc + "/" + idDoc + ".json")).isoformat()[0:10]    
    motherMassive = motherMassive + prepare_dataReq(file_mod_date, data)      
    motherMassive = motherMassive + prepare_dataProt(file_mod_date, data)      
    motherMassive = motherMassive + prepare_dataSort(file_mod_date, data)
    # print(motherMassive)
    return motherMassive
  
def open_file(F):
    print(F)
    with io.open(F,'r',encoding='utf-8') as data_file:
        data_loaded = json.load(data_file)    
    return data_loaded

def prepare_dataReq(file_mod_date, data):
    if "requirements" in data:
        req_count = 0
        req_list = []
        for req in data['requirements']:
            load_data = []
            req_count = req_count +1
            load_data.append(str(data["id_document"]))    
            load_data.append(str(file_mod_date))
            load_data.append('requirements') 
            load_data.append(str(req_count))  
            load_data.append('1')
            
            mainFraction_percent = float(req['requirementsTable']['mainFractionData']['purity'])
            suitableFraction_percent = float(req['requirementsTable']['suitableFraction']['purity'])
            weedFraction_percent = float(req['requirementsTable']['weedFraction']['purity'])
            suitableFraction_mass = float(req['requirementsTable']['suitableFraction']['mass'])
            mainFraction_mass = float(req['requirementsTable']['mainFractionData']['mass'])
            
            ph_1 = os.path.exists(MYDIR + "/static/web_data/" + str(data["id_document"]) + '/' + 'TRASH_Source_1_' + str(req_count) + '_0.jpg')
            ph_2 = os.path.exists(MYDIR + "/static/web_data/" + str(data["id_document"]) + '/' + 'TRASH_Source_2_' + str(req_count) + '_0.jpg')
            ph_3 = os.path.exists(MYDIR + "/static/web_data/" + str(data["id_document"]) + '/' + 'TRASH_Source_3_' + str(req_count) + '_0.jpg')

            if ph_1:
                photo_source = web_path + str(data["id_document"]) + '/' + 'TRASH_Source_1_' + str(req_count) + '_0.jpg'
            else:
                photo_source = '-'
            if ph_2:
                photo_accept = web_path + str(data["id_document"]) + '/' + 'TRASH_Source_2_' + str(req_count) + '_0.jpg'
            else:
               photo_accept = '-'
            
            if ph_3:
                photo_reject = web_path + str(data["id_document"]) + '/' + 'TRASH_Source_3_' + str(req_count) + '_0.jpg'
            else:
               photo_reject = '-'
            
            input_date = '-'
            input_user = '-'
           
            __good = ""
            __bad = ""
            
            for comp in req['componentRow']:                                   
                if comp['mainFractionData']['acceptRejectToggle']:
                    __good = __good + ' '.join(comp['SearchProductResult']) + ","
                else:
                    __bad = __bad + ' '.join(comp['SearchProductResult']) + ","
                    
            while len(__good) > 0 and __good[len(__good)-1] == ",":
                __good = __good[:-1]        
            
            while len(__bad) > 0 and __bad[len(__bad)-1] == ",":
                __bad = __bad[:-1]

            load_data.append(str(__good.encode('utf-8')))
            load_data.append(str(__bad.encode('utf-8')))
            load_data.append(str(mainFraction_percent))
            load_data.append(str(suitableFraction_percent))
            load_data.append(str(weedFraction_percent))
            load_data.append(str(suitableFraction_mass))
            load_data.append(str(mainFraction_mass))
            load_data.append("Y")
            load_data.append(photo_source)
            load_data.append(photo_accept)
            load_data.append(photo_reject)
            load_data.append(input_date)
            load_data.append(input_user)
            

            req_list.append(load_data)

    return req_list

def prepare_dataProt(file_mod_date, data):
    if "protocol" in data:
        prot_counter = 0
        prot_list = []
        for prot in data['protocol']:
            load_data = []
            prot_counter = prot_counter +1
            load_data.append(str(data["id_document"]))    
            load_data.append(str(file_mod_date))
            load_data.append('protocol') 
            load_data.append(str(prot_counter))  
            load_data.append('1')
            
            mainFraction_percent = float(prot['requirementsTable']['mainFractionData']['purity'])
            suitableFraction_percent = float(prot['requirementsTable']['suitableFraction']['purity'])
            weedFraction_percent = float(prot['requirementsTable']['weedFraction']['purity'])
            suitableFraction_mass = float(prot['requirementsTable']['suitableFraction']['mass'])
            mainFraction_mass = float(prot['requirementsTable']['mainFractionData']['mass'])
           
            ph_1 = os.path.exists(MYDIR + "/static/web_data/" + str(data["id_document"]) + '/' + 'TRASH_Source_1_' + str(prot_counter) + '_P_0.jpg')
            ph_2 = os.path.exists(MYDIR + "/static/web_data/" + str(data["id_document"]) + '/' + 'TRASH_Source_2_' + str(prot_counter) + '_P_0.jpg')
            ph_3 = os.path.exists(MYDIR + "/static/web_data/" + str(data["id_document"]) + '/' + 'TRASH_Source_3_' + str(prot_counter) + '_P_0.jpg')

            if ph_1:
                photo_source = web_path + str(data["id_document"]) + '/' + 'TRASH_Source_1_' + str(prot_counter) + '_P_0.jpg'
            else:
                photo_source = '-'
            if ph_2:
                photo_accept = web_path + str(data["id_document"]) + '/' + 'TRASH_Source_2_' + str(prot_counter) + '_P_0.jpg'
            else:
                photo_accept = '-'
            
            if ph_3:
                photo_reject = web_path + str(data["id_document"]) + '/' + 'TRASH_Source_3_' + str(prot_counter) + '_P_0.jpg'
            else:
                photo_reject = '-'
            

            input_date = str(prot['Sustatment']['TitleTable']['createDateProtocol'].encode('utf-8'))
            input_user = str(prot['Sustatment']['TitleTable']['userManagerName'].encode('utf-8'))
            
            __good = ""
            __bad = ""
            # print(prot['ProtocolRow'])
            for comp in prot['ProtocolRow']:    
                if comp['mainFractionData']['acceptRejectToggle']:
                    __good = __good + ' '.join(comp['SearchProductResult']) + ","
                else:
                    __bad = __bad + ' '.join(comp['SearchProductResult']) + ","
            
            while len(__good) > 0 and __good[len(__good)-1] == ",":
                __good = __good[:-1]        
            
            while len(__bad) > 0 and __bad[len(__bad)-1] == ",":
                __bad = __bad[:-1]

            load_data.append(str(__good.encode('utf-8')))
            load_data.append(str(__bad.encode('utf-8')))
            load_data.append(str(mainFraction_percent))
            load_data.append(str(suitableFraction_percent))
            load_data.append(str(weedFraction_percent))
            load_data.append(str(suitableFraction_mass))
            load_data.append(str(mainFraction_mass))
            load_data.append("Y")
            load_data.append(photo_source)
            load_data.append(photo_accept)
            load_data.append(photo_reject)
            load_data.append(input_date)
            load_data.append(input_user)

            prot_list.append(load_data)


    return prot_list

def prepare_dataSort(file_mod_date, data):
    if "protocol" in data:   
        prot_counter = 0
        sort_list = []
        for prot in data['protocol']:
            prot_counter = prot_counter +1
            sort_counter = 1
            for sort in prot['pageSortRow']:
                sort_counter = sort_counter +1
                load_data = []
                load_data.append(str(data["id_document"]))    
                load_data.append(str(file_mod_date))
                load_data.append('protocol') 
                load_data.append(str(prot_counter))  
                load_data.append(str(sort_counter))
            
                mainFraction_percent = float(sort['requirementsTable']['mainFractionData']['purity'])
                suitableFraction_percent = float(sort['requirementsTable']['suitableFraction']['purity'])
                weedFraction_percent = float(sort['requirementsTable']['weedFraction']['purity'])
                suitableFraction_mass = float(sort['requirementsTable']['suitableFraction']['mass'])
                mainFraction_mass = float(sort['requirementsTable']['mainFractionData']['mass'])

                ph_1 = os.path.exists(MYDIR + "/static/web_data/" + str(data["id_document"]) + '/' + 'TRASH_Source_1_' + str(prot_counter) + '_S_' + str(sort_counter-1) + '_0.jpg')
                ph_2 = os.path.exists(MYDIR + "/static/web_data/" + str(data["id_document"]) + '/' + 'TRASH_Source_2_' + str(prot_counter) + '_S_' + str(sort_counter-1) + '_0.jpg')
                ph_3 = os.path.exists(MYDIR + "/static/web_data/" + str(data["id_document"]) + '/' + 'TRASH_Source_3_' + str(prot_counter) + '_S_' + str(sort_counter-1) + '_0.jpg')
                print(ph_1, ph_2, ph_3)
                if ph_1:
                    photo_source = web_path + str(data["id_document"]) + '/' + 'TRASH_Source_1_' + str(prot_counter) + '_S_' + str(sort_counter-1) + '_0.jpg'
                else:
                    photo_source = '-'
                if ph_2:
                    photo_accept = web_path + str(data["id_document"]) + '/' + 'TRASH_Source_2_' + str(prot_counter) + '_S_' + str(sort_counter-1) + '_0.jpg'
                else:
                    photo_accept = '-'
                
                if ph_3:
                    photo_reject = web_path + str(data["id_document"]) + '/' + 'TRASH_Source_3_' + str(prot_counter) + '_S_' + str(sort_counter-1) + '_0.jpg'
                else:
                    photo_reject = '-'
            
                input_date = str(sort['Sustatment']['TitleTable']['createDateProtocol'].encode('utf-8'))
                input_user = str(sort['Sustatment']['TitleTable']['userManagerName'].encode('utf-8'))

                __good = ""
                __bad = ""
                
                for comp in sort['ProtocolSort']:                   
                    if comp['mainFractionData']['acceptRejectToggle']:
                        __good = __good + ' '.join(comp['SearchProductResult']) + ","
                    else:
                        __bad = __bad + ' '.join(comp['SearchProductResult']) + ","

                while len(__good) > 0 and __good[len(__good)-1] == ",":
                    __good = __good[:-1]        
            
                while len(__bad) > 0 and __bad[len(__bad)-1] == ",":
                    __bad = __bad[:-1]

                load_data.append(str(__good.encode('utf-8')))
                load_data.append(str(__bad.encode('utf-8')))
                load_data.append(str(mainFraction_percent))
                load_data.append(str(suitableFraction_percent))
                load_data.append(str(weedFraction_percent))
                load_data.append(str(suitableFraction_mass))
                load_data.append(str(mainFraction_mass))
                load_data.append("Y")

                load_data.append(photo_source)
                load_data.append(photo_accept)
                load_data.append(photo_reject)
                load_data.append(input_date)
                load_data.append(input_user)

                sort_list.append(load_data)


    return sort_list

def load_Classifire_Data(idDoc):   
    result = {
		'values': create_Data(idDoc) 
	}
    gets = service.spreadsheets().values().get(spreadsheetId=requestStat,	range="stat!A3:A").execute()
    values = gets.get('values', [])
    id_row = len(values) + 3 # цифра это строки шапки а len это кол во строк
    rangeCompany = 'stat!A' + str(id_row) + ':R'



    service.spreadsheets().values().update(
		spreadsheetId= requestStat, range= rangeCompany,
    valueInputOption="USER_ENTERED", body= result).execute()

#transforn string date from table to date format 
def data_Converter(date):
    format = "%Y-%m-%d"
    _d = datetime.strptime(date, format)
    return _d

def KostyaEbniKnopku():
    gets = service.spreadsheets().values().get(spreadsheetId=requestStat,range=Model_Range).execute()
    values = gets.get('values', [])

    id_List = []
    date_list = []
    global_list = []
    new_values = []

    for row in values:
        id_List.append(row[0])
    id_List = list(dict.fromkeys(id_List))
    
    for id in id_List:
        date = ''
        for row in values:
            if id == row[0]:
                if date == "":
                    date = data_Converter(row[1])
                else:
                    if date < data_Converter(row[1]):
                        date = data_Converter(row[1])
        date_list.append(date)

    for i in range(len(id_List)):
        global_list.append({
            'id': id_List[i],
            'date': date_list[i]
        })
    
    for el in global_list:
        for row in values:
            if el['date'] == data_Converter(row[1]) and el['id'] == row[0]:
                new_values.append(row)

    bodyDeleat = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 0,
                        'dimension': 'ROWS',
                        'startIndex': int(2),
                        'endIndex': (int(len(values))+2)
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(spreadsheetId=requestStat, body=bodyDeleat).execute()
    
    result = {
		'values': new_values
	}
    service.spreadsheets().values().update(
		spreadsheetId= requestStat, range= "stat!A3:R",
    valueInputOption="USER_ENTERED", body= result).execute()   
    
    return new_values



def setYorN(ID_Doc):
    result = service.spreadsheets().values().get(
        spreadsheetId=requestStat, range='stat!A3:R').execute()
    arrData = result.get('values', [])

    for data in arrData:
        if data[0] == ID_Doc:
            data[12] = 'N'
        
    body = {
        "valueInputOption": "RAW", 
        "data": [
            {"range": 'stat!A3:R',
                "values": arrData} 
        ]
    }

    service.spreadsheets().values().batchUpdate(spreadsheetId = requestStat, body = body).execute()
 