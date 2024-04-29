# -*- coding: utf-8 -*-
#Flask api
from flask import Flask, jsonify, render_template, request, send_from_directory

#Google api
import api_google
import googlesheet_calendarDnD
import googlesheet_protocol
import googlesheet_classifier_sort
import googlesheet_classifier
import googlesheet_requirements
import googlesheet_user_manager
import googlesheet_statistic
import googlesheet_competitor
import googlesheet_economic
import googlesheet_dealer
import client_queue
import search_img
import load_company

import googlesheet_translate_PR

#для комерческих предложений
import googlesheet_apparatus
import bitrix24_request
import googlesheet_translate
import googlesheet_translate_Product


#Img Save Img base64
import base64
from io import BytesIO
from PIL import Image

import io
import os
MYDIR = os.path.dirname(__file__)

import time
import random

from datetime import datetime
from datetime import timedelta

import shutil
import requests
import json

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300
app.config['JSON_AS_ASCII'] = False
app.debug = True


@app.route('/favicon.ico')
def fav():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/cache/crb/daily_json')
def daily_json():
    file_mod_date = datetime.fromtimestamp(os.path.getmtime(MYDIR+'/static/daily_json.js')).isoformat()[0:10]
    today_date = str(datetime.now().date())[0:10]
    
    #print(file_mod_date, today_date)
    if today_date != file_mod_date:
        req = requests.get("https://www.cbr-xml-daily.ru/daily_json.js", verify=False)
        with io.open(MYDIR+'/static/daily_json.js', 'w', encoding='utf8') as file:
            data = json.dumps(req.json(), ensure_ascii=False)
            file.write( (data))
    #file.close()
    
    return send_from_directory(os.path.join(app.root_path, 'static'),'daily_json.js')

@app.route('/')
def hello_world():
	return 'Hello World!'
    
@app.route('/request')
def web_template_request():
	return render_template('request.html')

@app.route('/result')
def web_template_result():
	return render_template('result.html', last_updated=dir_last_updated(MYDIR+'/static'))
    
@app.route('/protocol')
def web_template_protocol():    
    return render_template('protocol.html', last_updated=dir_last_updated(MYDIR+'/static'))

@app.route('/mainco')
def web_template_kpApparat():
    now = datetime.now()
    datestring = now.strftime("%d") + "." + now.strftime("%m") + "." + now.strftime("%Y")
    return render_template('mainco.html', last_updated=dir_last_updated(MYDIR+'/static'), datestring = datestring)

@app.route('/test/classifier')
def web_template_test_classifier():
    return render_template('classifier.html', last_updated=dir_last_updated(MYDIR+'/static'))

@app.route('/company')
def web_template_test_TestClassifier():
    return render_template('TestClassifier.html', last_updated=dir_last_updated(MYDIR+'/static'))

@app.route('/constructor')
def web_template_constructor():
    return render_template('constructor.html', last_updated=dir_last_updated(MYDIR+'/static'))

@app.route('/edit_json')
def web_template_edit_json():
    now = datetime.now()
    datestring = now.strftime("%d") + "." + now.strftime("%m") + "." + now.strftime("%Y")
    return render_template('edit_json.html', last_updated=dir_last_updated(MYDIR+'/static'), datestring = datestring)

@app.route('/econom')
def web_template_econom():
    return render_template('econom.html')

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                   for root_path, dirs, files in os.walk(folder)
                   for f in files))
    
"""Подключение таблиц с данными и страниц для передачи информации"""
@app.route('/request/product_name')
def req_product_name():	
	results = [table.to_dict() for table in googlesheet_request.list_product_name]
	return jsonify(result=results)
@app.route('/request/product_description')
def req_product_description():	
	results = [table.to_dict() for table in googlesheet_request.list_product_description]

	return jsonify(result=results)
@app.route('/request/weed_name')
def req_weed_name():	
	results = [table.to_dict() for table in googlesheet_request.list_weed_name]

	return jsonify(result=results)
@app.route('/request/weed_description')
def req_weed_description():	
	results = [table.to_dict() for table in googlesheet_request.list_weed_description]

	return jsonify(result=results)
@app.route('/request/patern_product')
def req_patern_product():	
	results = [table.to_dict() for table in googlesheet_request.list_patern_product]

	return jsonify(result=results)
@app.route('/request/patern_product_purpose')
def req_patern_product_purpose():	
	results = [table.to_dict() for table in googlesheet_request.list_patern_product_purpose]

	return jsonify(result=results)

@app.route('/request/requirements')
def req_requirements_write():
    id_protocol = request.args.get('id_protocol')
    name_product = request.args.get('name_product')
    purpose_product = request.args.get('purpose_product')
    main_product_percent = request.args.get('main_product_percent')
    photo_product = request.args.get('photo_product')
    capacity = request.args.get('capacity')
    fraction_count = request.args.get('fraction_count')
    companent_count = request.args.get('companent_count')
    comment = request.args.get('comment')
    
    id_requirements = googlesheet_request.write_requirements_request(
        id_protocol,
        name_product, 
        purpose_product, 
        main_product_percent, 
        photo_product, 
        capacity, 
        fraction_count, 
        companent_count, 
        comment)
    
    return jsonify(result=id_requirements)
    
@app.route('/request/fraction')
def req_fraction_write():
    id_requirements = request.args.get('id_requirements')
    id_fraction = request.args.get('id_fraction')
    id_valid_itemBlock = request.args.get('id_valid_itemBlock')
    fraction_name = request.args.get('fraction_name')
    selection = request.args.get('selection')
    exit = request.args.get('exit')
    purity_percent = request.args.get('purity_percent')
    capacity = request.args.get('capacity')
    comment = request.args.get('comment')
    photo_fraction = request.args.get('photo_fraction')
    
    googlesheet_request.write_fractions_request(
        id_requirements, 
        id_fraction, 
        id_valid_itemBlock, 
        fraction_name, 
        selection, 
        exit, 
        purity_percent, 
        capacity, 
        comment, 
        photo_fraction)
    
    return jsonify(result= ("Таблица фракций обновлена!", 'cp1251'))

@app.route('/request/companent_mainInfo')
def req_write_companent_mainInfo():
    id_requirements = request.args.get('id_requirements')
    id_companent = request.args.get('id_companent')
    companent_name = request.args.get('companent_name')
    companent_description = request.args.get('companent_description')
    companent_value = request.args.get('companent_value')
    unit_type = request.args.get('unit_type')
    companent_valid_check = request.args.get('companent_valid_check')
    companent_photo = request.args.get('companent_photo')
    
    googlesheet_request.write_companent_mainInfo_request(
        id_requirements, 
        id_companent, 
        companent_name, 
        companent_description, 
        companent_value, 
        unit_type, 
        companent_valid_check, 
        companent_photo)
    
    return jsonify(result= ("Таблица компанетов обновлена!", 'cp1251'))

@app.route('/request/companent_addInfo')
def req_write_companent_addInfo():
    id_fraction = request.args.get('id_fraction')
    str_number = request.args.get('str_number')
    companent_value = request.args.get('companent_value')
    unit_type = request.args.get('unit_type')
    companent_valid_check = request.args.get('companent_valid_check')
    companent_warnin_check = request.args.get('companent_warnin_check')
    
    
    googlesheet_request.write_component_fractionInfo_request(
        id_fraction, 
        str_number, 
        companent_value, 
        unit_type, 
        companent_valid_check, 
        companent_warnin_check)
    
    return jsonify(result= ("Таблица компанетов обновлена!", 'cp1251'))
 
#Попытка загрузить изображение
@app.route('/request/upload', methods = ['POST'])
def upload_base64_file():
    img_name = request.form['img_name']
    base64_img = request.form['base64_img']
    
    convert_and_save(base64_img,img_name)
    
    return jsonify(result=[img_name,base64_img])

def convert_and_save(b64_string, img_name):
    image_data = bytes(b64_string)
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    im.save(os.path.join(MYDIR, "static/img/save_img/"+img_name+".png"))  

def upload_base64_Folder(id_protocol, photoFolder, base64_images, images_name):
    if os.path.exists(MYDIR + "/static/img/save_img/protocol_"+id_protocol) == False:
        os.mkdir(MYDIR + "/static/img/save_img/protocol_"+id_protocol)
    if os.path.exists(MYDIR + "/static/img/save_img/protocol_"+id_protocol+"/"+photoFolder) == False:
        os.mkdir(MYDIR + "/static/img/save_img/protocol_"+id_protocol+"/"+photoFolder)
    
    length = len(images_name)

    for id in range(length):
        if base64_images[id][:6] != "static":
            image_data = bytes(base64_images[id])
            im = Image.open(BytesIO(base64.b64decode(image_data)))
            im.save(os.path.join(MYDIR, "static/img/save_img/protocol_"+id_protocol+"/"+photoFolder+"/"+images_name[id]+".png"))
        elif str(base64_images[id]) != str("static/img/save_img/protocol_"+id_protocol+"/"+photoFolder+"/"+images_name[id]+".png"):
            #shutil.copy2(str(MYDIR + "/" +base64_images[id]), str(MYDIR +"/static/img/save_img/protocol_"+id_protocol+"/"+photoFolder+"/"+images_name[id]+".png")) #Для сервера
            shutil.copy2(str(base64_images[id]), str("static/img/save_img/protocol_"+id_protocol+"/"+photoFolder+"/"+images_name[id]+".png"))
            
def upload_base64_Folder_requirement(id_requirement, photoFolder, base64_images, images_name):
    if os.path.exists(MYDIR + "/static/img/save_img/requirement_"+id_requirement) == False:
        os.mkdir(MYDIR + "/static/img/save_img/requirement_"+id_requirement)
    if os.path.exists(MYDIR + "/static/img/save_img/requirement_"+id_requirement+"/"+photoFolder) == False:
        os.mkdir(MYDIR + "/static/img/save_img/requirement_"+id_requirement+"/"+photoFolder)
    
    length = len(images_name)

    for id in range(length):
        if base64_images[id] != "static":
            image_data = bytes(base64_images[id])
            im = Image.open(BytesIO(base64.b64decode(image_data)))
            im.save(os.path.join(MYDIR, "static/img/save_img/requirement_"+id_requirement+"/"+photoFolder+"/"+images_name[id]+".png"))
"""
@app.route('/blob_image', methods = ['POST'])
def upload_blob_image():
    blob = request.files['image'].read()
    img = Image.open(BytesIO(blob))
    img.save(os.path.join(MYDIR, "static/img/save_img/"+img+".png")) 
"""
"""Временно не требуеться 
@app.route('/reques/upload_to_google', methods = ['POST'])
def upload_to_google():
    protocolID = request.form['protocolID']
    fraction = request.form['fraction_coint']
    add_companents = request.form['add_companents']
    
    folder = googledrive_request_result.create_new_folder(protocolID)
    results = []
    
    #Отправление отправка изображения исходного продукта
    results.append(googledrive_request_result.upload_img(protocolID+"_source_product", folder))
    #Отправка изображений по фракциям
    fraction_id=1
    while fraction_id<=int(fraction):
        if fraction_id < 10:
            results.append(googledrive_request_result.upload_img(protocolID+"_fraction_0"+str(fraction_id), folder))
        else:
            results.append(googledrive_request_result.upload_img(protocolID+"_fraction_"+str(fraction_id), folder))
        fraction_id = fraction_id +1
    
    #Отвравка изображения по продуктам
    results.append(googledrive_request_result.upload_img(protocolID+"_main_product", folder))
    
    comp_id=1
    if comp_id<=int(add_companents):
        while comp_id<=int(add_companents):
            results.append(googledrive_request_result.upload_img(protocolID+"_itemBlock_"+str(comp_id)+"_product", folder))
            comp_id = comp_id +1

    results.append(googledrive_request_result.upload_img(protocolID+"_other_product", folder))

    return jsonify(result=results)


@app.route('/result/requirements')
def res_requirements():
    id_protocol = request.args.get('id_protocol')
    
    results  = [googlesheet_request.get_requirements_result(id_protocol)]
    
    return jsonify(result=results)

@app.route('/result/fraction')
def res_fraction():
    data = googlesheet_request.requirements
    
    results = [table.to_dict() for table in googlesheet_request.requirements_fraction]
    
    return jsonify(result=results)
    
@app.route('/result/companent')
def res_companent():
    results = []
    for id in range(len(googlesheet_request.requirements_companent)):
        results.append(googlesheet_request.requirements_companent[id])
    
    return jsonify(result=results)
"""

@app.route('/calendarD&D/Project_Stage')
def get_calendar_Stage():	
	results = [table.to_dict() for table in googlesheet_calendarDnD.list_Project_Stage]

	return jsonify(result=results)
    
@app.route('/calendarD&D/Project_SubStage')
def get_calendar_More():	
	results = [table.to_dict() for table in googlesheet_calendarDnD.list_Project_SubStage]

	return jsonify(result=results) 

@app.route('/calendarD&D/Project_Date')
def get_calendar_Date():
    googlesheet_calendarDnD.refresh_Data_Project()
    results = [table.to_dict() for table in googlesheet_calendarDnD.list_Project_Date]
    
    return jsonify(result=results)

@app.route('/calendarD&D/update_calendar', methods = ['POST'])
def set_update_calendar():
    first_list = []
    second_list = []
    
    for key, value in request.form.items('write_data'):
        second_list.append(value)
    
    list = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    first_list = (list(second_list,8))
    first_list.sort(key = lambda x: int(x[0]))
    
    #Удаление значения приоритета
    for list in first_list:
        list.pop(0)
    
    return jsonify(result=googlesheet_calendarDnD.update_calendar(first_list))


#Сохранение протоколов
@app.route('/protocol/write_mainInfo', methods = ['POST'])
def protocol_write_mainInfo():

    id_protocol = request.form['id_protocol']
    id_requirements = request.form['id_requirements']
    write_type = request.form['write_type']
    equipment = request.form['equipment']
    configuration = request.form['configuration']
    sortingValue = request.form['sortingValue']
    componentValue = request.form['componentValue']
    
    id_return = googlesheet_protocol.write_protocol(id_protocol, 
        id_requirements,
        write_type,
        equipment,
        configuration,
        sortingValue,
        componentValue)
    
    return jsonify(result=[id_return,id_requirements,write_type,equipment,configuration,sortingValue,componentValue])

@app.route('/protocol/write_sourceProduct', methods = ['POST'])
def protocol_write_sourceProduct():
    id_protocol = request.form['id_protocol']
    id_requirements = request.form['id_requirements']
    id_product = request.form['id_product']
    productName = request.form['productName']
    purpose = request.form['purpose']
    purity = request.form['purity']
    capacity = request.form['capacity']
    capacity_type = request.form['capacity_type']
    selection = request.form['selection']
    selection_type = request.form['selection_type']
    photoFolder = request.form['photoFolder']
    id_mainPhoto = request.form['id_mainPhoto']
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')
    
    upload_base64_Folder(id_protocol, photoFolder, base64_images, images_name)
    googlesheet_protocol.write_product(id_protocol,
        id_requirements,
        id_product,
        productName,
        purpose,
        purity,
        capacity,
        capacity_type,
        selection,
        selection_type,
        photoFolder,
        id_mainPhoto)
    
    return jsonify(result=[id_protocol, id_requirements, id_product, productName, purpose, purity, capacity, capacity_type, selection, selection_type, photoFolder, id_mainPhoto])

@app.route('/protocol/write_sorting', methods = ['POST'])
def protocol_write_sorting():
    id_protocol = request.form['id_protocol']
    id_sorting = request.form['id_sorting']
    inbox_fraction = request.form['inbox_fraction']
    purity = request.form['purity']
    capacity = request.form['capacity']
    capacity_type = request.form['capacity_type']
    programFolder = request.form['programFolder']
    
    googlesheet_protocol.write_sorting(id_protocol,
        id_sorting,
        inbox_fraction,
        purity,
        capacity,
        capacity_type,
        programFolder)
    
    return jsonify(result=[id_protocol, id_sorting, inbox_fraction, purity, capacity, capacity_type, programFolder])
    
@app.route('/protocol/write_accept', methods=['POST'])
def protocol_write_accept():
    id_protocol = request.form['id_protocol']
    id_sorting = request.form['id_sorting']
    fractionName = request.form['fractionName']
    selection = request.form['selection']
    selection_type = request.form['selection_type']
    exit = request.form['exit']
    purity = request.form['purity']
    capacity = request.form['capacity']
    photoFolder = request.form['photoFolder']
    id_mainPhoto = request.form['id_mainPhoto']
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')
    
    upload_base64_Folder(id_protocol, photoFolder, base64_images, images_name)
    googlesheet_protocol.write_accept(id_protocol, 
        id_sorting, 
        fractionName, 
        selection, 
        selection_type, 
        exit, 
        purity, 
        capacity, 
        photoFolder,
        id_mainPhoto)
    
    return jsonify(result=[id_protocol, id_sorting, fractionName, selection, selection_type, exit, purity, capacity, photoFolder, id_mainPhoto])    

@app.route('/protocol/write_reject', methods=['POST'])
def protocol_write_reject():
    id_protocol = request.form['id_protocol']
    id_sorting = request.form['id_sorting']
    fractionName = request.form['fractionName']
    selection = request.form['selection']
    selection_type = request.form['selection_type']
    exit = request.form['exit']
    purity = request.form['purity']
    capacity = request.form['capacity']
    photoFolder = request.form['photoFolder']
    id_mainPhoto = request.form['id_mainPhoto']
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')
    
    upload_base64_Folder(id_protocol, photoFolder, base64_images, images_name)
    googlesheet_protocol.write_reject(id_protocol, 
        id_sorting, 
        fractionName, 
        selection, 
        selection_type, 
        exit, 
        purity, 
        capacity, 
        photoFolder, 
        id_mainPhoto)
    
    return jsonify(result=[id_protocol, id_sorting, fractionName, selection, selection_type, exit, purity, capacity, photoFolder, id_mainPhoto])

@app.route('/protocol/write_components_1', methods=['POST'])
def protocol_write_components_1():
    id_protocol = request.form['id_protocol']
    id_component = request.form['id_component']
    component_number = request.form['component_number']
    component_name = request.form['component_name']
    component_value = request.form['component_value']
    component_type = request.form['component_type']
    component_valid_check = request.form['component_valid_check']
    component_remove_check = request.form['component_remove_check']
    photoFolder = request.form['photoFolder']
    id_mainPhoto = request.form['id_mainPhoto']
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')
    
    upload_base64_Folder(id_protocol, photoFolder, base64_images, images_name)
    googlesheet_protocol.write_component_mainInfo(id_protocol, 
        id_component, 
        component_number, 
        component_name, 
        component_value, 
        component_type, 
        component_valid_check, 
        component_remove_check, 
        photoFolder,
        id_mainPhoto)
    
    return jsonify(result=[id_protocol, id_component, component_number, component_name, component_value, component_type, component_valid_check, component_remove_check, photoFolder, id_mainPhoto])

@app.route('/protocol/write_components_2', methods=['POST'])
def protocol_write_components_2():
    id_AcceptReject = request.form['id_AcceptReject']
    str_number = request.form['str_number']
    component_value = request.form['component_value']
    component_type = request.form['component_type']
    component_valid_check = request.form['component_valid_check']
    component_warnin_check = request.form['component_warnin_check']
    
    googlesheet_protocol.write_component_sortingInfo(id_AcceptReject, 
        str_number, 
        component_value, 
        component_type, 
        component_valid_check, 
        component_warnin_check)
    
    return jsonify(result=[id_AcceptReject, str_number, component_value, component_type, component_valid_check, component_warnin_check])           

#Получение/Чтение протокола для резалта
@app.route('/protocol/get_protocol_result', methods=['POST'])
def get_protocol_result():
    del googlesheet_protocol.list_protocol[:]
    del googlesheet_protocol.list_product[:]
    del googlesheet_protocol.list_sorting[:]
    del googlesheet_protocol.list_accept[:]
    del googlesheet_protocol.list_reject[:]
    del googlesheet_protocol.list_components[:]
    
    id_protocol = request.form['id_protocol']
    
    googlesheet_protocol.get_protocol_result(id_protocol)
    
    results = [table.to_dict() for table in googlesheet_protocol.list_protocol]
    return jsonify(result=results)

#Получение/Чтение протоколов()
@app.route('/protocol/search_protocol', methods=['POST'])
def search_protocol():
    del googlesheet_protocol.list_protocol[:]
    del googlesheet_protocol.list_product[:]
    del googlesheet_protocol.list_sorting[:]
    del googlesheet_protocol.list_accept[:]
    del googlesheet_protocol.list_reject[:]
    del googlesheet_protocol.list_components[:]
    
    del googlesheet_requirements.list_fraction[:]
    
    #Параметры поиска
    productName = request.form['productName']
    equipment = request.form['equipment']
    configuration = request.form['configuration']
    
    googlesheet_protocol.search_protocol(productName, equipment, configuration)
    
    results = [table.to_dict() for table in googlesheet_protocol.list_protocol]
    return jsonify(result=results)
    
@app.route('/protocol/get_protocol', methods=['POST'])
def get_protocol_mainInfo():
    del googlesheet_protocol.list_protocol[:]
    del googlesheet_protocol.list_product[:]
    del googlesheet_protocol.list_sorting[:]
    del googlesheet_protocol.list_accept[:]
    del googlesheet_protocol.list_reject[:]
    del googlesheet_protocol.list_components[:]
    
    id_requirements = request.form['id_requirements']
    
    googlesheet_protocol.get_protocol(id_requirements)
    
    results = [table.to_dict() for table in googlesheet_protocol.list_protocol]
    return jsonify(result=results)
    
@app.route('/protocol/get_product')
def get_protocol_product():
    results = [table.to_dict() for table in googlesheet_protocol.list_product]
    return jsonify(result=results)
    
@app.route('/protocol/get_sorting')
def get_protocol_sorting():
    results = [table.to_dict() for table in googlesheet_protocol.list_sorting]
    return jsonify(result=results)
        
@app.route('/protocol/get_accept')
def get_protocol_accept():
    results = [table.to_dict() for table in googlesheet_protocol.list_accept]
    return jsonify(result=results)
         
@app.route('/protocol/get_reject')
def get_protocol_reject():
    results = [table.to_dict() for table in googlesheet_protocol.list_reject]
    return jsonify(result=results)

@app.route('/protocol/get_component')
def get_protocol_component():
    results = []
    for id in range(len(googlesheet_protocol.list_components)):
        results.append(googlesheet_protocol.list_components[id])
        
    return jsonify(result=results)

#Новый способ получить протокола
@app.route('/protocol/new_get_protocol', methods = ['POST'])
def new_get_protocol():
    id_protocol = request.form['id_protocol']
    protocol = googlesheet_protocol.new_get_protocol_result(id_protocol)  
    
    id_requirement = protocol["ProtocolData"]["protocol"][0]["ID_Requirements"]
    requirements = googlesheet_requirements.new_get_requirements(id_requirement)
    
    results = dict(protocol.items() + requirements.items())
    
    return jsonify(result=results)

#Получение списка топа по продуктам протокола
@app.route('/protocol/get_TopComponent')
def get_top_component():
    results = googlesheet_protocol.protocolTopProduct()
    
    return jsonify(result=results)

#Редактировнание прототоколов
@app.route('/protocol/edit_protocol', methods = ['POST'])
def edit_protocol():
    first_list = []
    
    id_protocol = request.form['id_protocol']
    id_requirements = request.form['id_requirements']
    
    _id_protocol = googlesheet_protocol.get_protocol_id(id_requirements, id_protocol)
    first_list.append(_id_protocol)
    
    for key, value in request.form.items('write_data'):
        if key != "id_protocol" and key != "id_requirements":
            first_list.append(value)         
    
    googlesheet_protocol.edit_protocol(first_list[0], first_list)
    
    return jsonify(result=first_list)

@app.route('/protocol/edit_sourceProduct', methods = ['POST'])
def edit_protocol_sourceProduct():
    first_list = []
        
    for key, value in request.form.items('write_data'):
        if key != "images_name[]" and key != "base64_images[]":
            first_list.append(value)  
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')
    
    upload_base64_Folder(first_list[0], first_list[10], base64_images, images_name)
    googlesheet_protocol.edit_sourceProduct(first_list[0], first_list)
    
    return jsonify(result=first_list)

@app.route('/protocol/edit_sorting', methods = ['POST'])
def edit_protocol_sorting():
    first_list = []
    second_list = []
    
    for key, value in request.form.items('write_data'):
        second_list.append(value)  
    
    list = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    first_list = (list(second_list, 8))
    first_list.sort(key = lambda x: int(x[1]))
    
    googlesheet_protocol.edit_sorting(second_list[0], len(first_list), first_list)
    
    return jsonify(result=first_list)

@app.route('/protocol/edit_accept', methods = ['POST'])
def edit_protocol_accept():
    first_list = []
    second_list = []
    
    for key, value in request.form.items('write_data'):
        if key != "images_name[]" and key != "base64_images[]":
            second_list.append(value)
    
    list = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    first_list = (list(second_list, 11))
    first_list.sort(key = lambda x: int(x[1]))
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')    
    
    image_list = []
    name_list = []
    for id in range(len(first_list)):
        del image_list[:]
        del name_list[:]
        if int(first_list[id][10]) == 0:
            image_list.append(base64_images[0])
            name_list.append(images_name[0])
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][10]) == 1:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            image_list.append(base64_images[1])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][10]) == 2:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            image_list.append(base64_images[2])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            name_list.append(images_name[2])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            
        upload_base64_Folder(first_list[id][0], first_list[id][9], image_list, name_list)
    
    googlesheet_protocol.edit_accept(second_list[0], len(first_list), first_list)
    
    return jsonify(result=first_list)
    
@app.route('/protocol/edit_reject', methods = ['POST'])
def edit_protocol_reject():
    first_list = []
    second_list = []
    
    for key, value in request.form.items('write_data'):
        if key != "images_name[]" and key != "base64_images[]":
            second_list.append(value)
    
    list = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    first_list = (list(second_list, 11))
    first_list.sort(key = lambda x: int(x[1]))
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')    
    
    image_list = []
    name_list = []
    for id in range(len(first_list)):
        del image_list[:]
        del name_list[:]
        if int(first_list[id][10]) == 0:
            image_list.append(base64_images[0])
            name_list.append(images_name[0])
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][10]) == 1:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            image_list.append(base64_images[1])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][10]) == 2:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            image_list.append(base64_images[2])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            name_list.append(images_name[2])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            
        upload_base64_Folder(first_list[id][0], first_list[id][9], image_list, name_list)
    
    googlesheet_protocol.edit_reject(second_list[0], len(first_list), first_list)
    
    return jsonify(result=first_list)   
    
@app.route('/protocol/edit_components', methods = ['POST'])
def edit_protocol_components():
    first_list = []
    second_list = []
    
    for key, value in request.form.items('write_data'):
        if key != "accept_reject_count" and key != "images_name[]" and key != "base64_images[]":
            second_list.append(value)
    
    accept_reject_count = request.form['accept_reject_count']
    
    list = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    first_list = (list(second_list,(6 + (int(accept_reject_count) + 1)*4)))
    first_list.sort(key = lambda x: int(x[2]))
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')    
    
    image_list = []
    name_list = []
    for id in range(len(first_list)):
        del image_list[:]
        del name_list[:]
        if int(first_list[id][9]) == 0:
            image_list.append(base64_images[0])
            name_list.append(images_name[0])
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][9]) == 1:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            image_list.append(base64_images[1])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][9]) == 2:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            image_list.append(base64_images[2])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            name_list.append(images_name[2])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            
        upload_base64_Folder(first_list[id][0], first_list[id][8], image_list, name_list)
    
    googlesheet_protocol.edit_component(second_list[0], len(first_list), accept_reject_count, first_list)
    
    return jsonify(result=first_list)

#Получение таблиц для классификатора
@app.route('/protocol/classifier/industry')
def get_classifier_industy():
    results = [table.to_dict() for table in googlesheet_classifier.list_industry]
    return jsonify(result=results)   

@app.route('/protocol/classifier/productGroup')
def get_classifier_productGroup():
    results = [table.to_dict() for table in googlesheet_classifier.list_productGroup]
    return jsonify(result=results)   

@app.route('/protocol/classifier/product')
def get_classifier_product():
    results = [table.to_dict() for table in googlesheet_classifier.list_product]
    return jsonify(result=results)   

@app.route('/protocol/classifier/productType')
def get_classifier_productType():
    results = [table.to_dict() for table in googlesheet_classifier.list_productType]
    return jsonify(result=results)   

@app.route('/protocol/classifier/purpose')
def get_classifier_purpose():
    results = [table.to_dict() for table in googlesheet_classifier.list_purpose]
    return jsonify(result=results) 

@app.route('/protocol/classifier/gost')
def get_classifier_gost():
    results = [table.to_dict() for table in googlesheet_classifier.list_gost]
    return jsonify(result=results)    

@app.route('/protocol/classifier/segment')
def get_classifier_segment():
    results = [table.to_dict() for table in googlesheet_classifier.list_segment]
    return jsonify(result=results)   

@app.route('/protocol/classifier/region')
def get_classifier_region():
    results = [table.to_dict() for table in googlesheet_classifier.list_region]
    return jsonify(result=results)   

@app.route('/protocol/classifier/category')
def get_classifier_category():
    results = [table.to_dict() for table in googlesheet_classifier.list_category]
    return jsonify(result=results)
    
@app.route('/protocol/classifier/classWeed')
def get_classifier_classWeed():
    results = [table.to_dict() for table in googlesheet_classifier.list_classWeed]
    return jsonify(result=results)
    
@app.route('/protocol/classifier/weed')
def get_classifier_weed():
    results = [table.to_dict() for table in googlesheet_classifier.list_weed]
    return jsonify(result=results)
    
@app.route('/protocol/classifier/descriptionWeed')
def get_classifier_descriptionWeed():
    results = [table.to_dict() for table in googlesheet_classifier.list_description]
    return jsonify(result=results)
    
@app.route('/protocol/classifier/machine')
def get_classifier_machine():
    results = [table.to_dict() for table in googlesheet_classifier.list_machine]
    return jsonify(result=results)
    
@app.route('/protocol/classifier/configuration')
def get_classifier_configuration():
    results = [table.to_dict() for table in googlesheet_classifier.list_configuration]
    return jsonify(result=results) 

@app.route('/protocol/classifier/productPart')
def get_classifier_productPart():
    results = [table.to_dict() for table in googlesheet_classifier.list_productPart]
    return jsonify(result=results)   

@app.route('/protocol/classifier/productStatus')
def get_classifier_productStatus():
    results = [table.to_dict() for table in googlesheet_classifier.list_productStatus]
    return jsonify(result=results)   

@app.route('/protocol/classifier/productColor')
def get_classifier_productColor():
    results = [table.to_dict() for table in googlesheet_classifier.list_productColor]
    return jsonify(result=results)   
    
#Получение таблицы сортов
@app.route('/protocol/sort/Sort')
def get_sort_sort():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Sort]
    return jsonify(result=results)   

@app.route('/protocol/sort/Grainfeed')
def get_sort_grainfeed():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Grainfeed]
    return jsonify(result=results)   

@app.route('/protocol/sort/Cereal')
def get_sort_cereal():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Cereal]
    return jsonify(result=results)   

@app.route('/protocol/sort/Legumes')
def get_sort_legumes():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Legumes]
    return jsonify(result=results)   

@app.route('/protocol/sort/Corn')
def get_sort_corn():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Corn]
    return jsonify(result=results)   

@app.route('/protocol/sort/Foragelegumes')
def get_sort_foragelegumes():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Foragelegumes]
    return jsonify(result=results)   

@app.route('/protocol/sort/Legumesherbs')
def get_sort_legumesherbs():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Legumesherbs]
    return jsonify(result=results)   

@app.route('/protocol/sort/Cerealherbs')
def get_sort_cerealherbs():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Cerealherbs]
    return jsonify(result=results)   

@app.route('/protocol/sort/Silo')
def get_sort_silo():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Silo]
    return jsonify(result=results)   

@app.route('/protocol/sort/Arid')
def get_sort_arid():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Arid]
    return jsonify(result=results)   

@app.route('/protocol/sort/Oilseeds')
def get_sort_oilseeds():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Oilseeds]
    return jsonify(result=results)   

@app.route('/protocol/sort/Technical')
def get_sort_technical():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Technical]
    return jsonify(result=results)   

@app.route('/protocol/sort/Spinning')
def get_sort_spinning():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Spinning]
    return jsonify(result=results)   

@app.route('/protocol/sort/Essentialoil')
def get_sort_essentialoil():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Essentialoil]
    return jsonify(result=results)   

@app.route('/protocol/sort/Medicinal')
def get_sort_medicinal():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Medicinal]
    return jsonify(result=results)   

@app.route('/protocol/sort/Melliferous')
def get_sort_melliferous():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Melliferous]
    return jsonify(result=results)   

@app.route('/protocol/sort/Potatoes')
def get_sort_potatoes():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Potatoes]
    return jsonify(result=results)   

@app.route('/protocol/sort/Vegetable')
def get_sort_vegetable():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Vegetable]
    return jsonify(result=results)   

@app.route('/protocol/sort/Melons')
def get_sort_melons():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Melons]
    return jsonify(result=results)   

@app.route('/protocol/sort/Mushrooms')
def get_sort_mushrooms():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Mushrooms]
    return jsonify(result=results)   

@app.route('/protocol/sort/Fruitpomefruits')
def get_sort_fruitpomefruits():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Fruitpomefruits]
    return jsonify(result=results)   

@app.route('/protocol/sort/Fruitstonefruits')
def get_sort_fruitstonefruits():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Fruitstonefruits]
    return jsonify(result=results)   

@app.route('/protocol/sort/Berry')
def get_sort_berry():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Berry]
    return jsonify(result=results)   

@app.route('/protocol/sort/Grapes')
def get_sort_grapes():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Grapes]
    return jsonify(result=results)   

@app.route('/protocol/sort/Citrusandsubtropical')
def get_sort_citrusandsubtropical():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Citrusandsubtropical]
    return jsonify(result=results)   

@app.route('/protocol/sort/Floraldecorative')
def get_sort_floraldecorative():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Floraldecorative]
    return jsonify(result=results)   

@app.route('/protocol/sort/Forest')
def get_sort_forest():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Forest]
    return jsonify(result=results)   

@app.route('/protocol/sort/Fodderrootcrops')
def get_sort_fodderrootcrops():
    results = [table.to_dict() for table in googlesheet_classifier_sort.list_Fodderrootcrops]
    return jsonify(result=results)   

#Сохранение требований прототоколов
@app.route('/protocol/requirements/write_requirement', methods=['POST'])
def write_requirement():
    id_requirements = request.form['id_requirements']
    equipment = request.form['equipment']
    configuration = request.form['configuration']
    program = request.form['program']
    productName = request.form['productName']
    id_product = request.form['id_product']
    photoFolder = request.form['photoFolder']
    id_mainPhoto = request.form['id_mainPhoto']
    capacity_value = request.form['capacity_value']
    capacity_type = request.form['capacity_type']
    fraction_count = request.form['fraction_count']
    companent_count = request.form['companent_count']
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')
    
    upload_base64_Folder_requirement(id_requirements, photoFolder, base64_images, images_name)
    googlesheet_requirements.write_requirements_protocol(
        id_requirements,
        equipment,
        configuration,
        program,
        productName,
        id_product,
        photoFolder,
        id_mainPhoto,
        capacity_value,
        capacity_type,
        fraction_count,
        companent_count)

    return jsonify(result=[id_requirements, equipment, configuration, program, productName, id_product, photoFolder, id_mainPhoto, capacity_value, capacity_type, fraction_count, companent_count])

@app.route('/protocol/requirements/write_fraction', methods=['POST'])
def write_requirement_fraction():
    id_requirements = request.form['id_requirements']
    id_fraction = request.form['id_fraction']
    fraction_name = request.form['fraction_name']
    main_fraction = request.form['main_fraction']
    purpose = request.form['purpose']
    exit = request.form['exit']
    purity = request.form['purity']
    capacity = request.form['capacity']
    comment = request.form['comment']
    photoFolder = request.form['photoFolder']
    id_mainPhoto = request.form['id_mainPhoto']
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')
    
    upload_base64_Folder_requirement(id_requirements, photoFolder, base64_images, images_name)
    googlesheet_requirements.write_fraction_requirements_protocol(
        id_requirements,
        id_fraction,
        fraction_name,
        main_fraction,
        purpose,
        exit,
        purity,
        capacity,
        comment,
        photoFolder,
        id_mainPhoto)
    
    return jsonify(result=[id_requirements, id_fraction, fraction_name, purpose, exit, purity, capacity, comment, photoFolder, id_mainPhoto])
    
@app.route('/protocol/requirements/write_components_1', methods=['POST'])
def write_requirements_components_1():
    id_requirements = request.form['id_requirements']
    component_number = request.form['component_number']
    companent_name = request.form['companent_name']
    id_companent = request.form['id_companent']
    component_value = request.form['component_value']
    component_type = request.form['component_type']
    component_valid_check = request.form['component_valid_check']
    component_remove_check = request.form['component_remove_check']
    photoFolder = request.form['photoFolder']
    id_mainPhoto = request.form['id_mainPhoto']
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')
    
    upload_base64_Folder_requirement(id_requirements, photoFolder, base64_images, images_name)
    googlesheet_requirements.write_component_mainInfo(
        id_requirements,
        component_number,
        companent_name,
        id_companent,
        component_value, 
        component_type,
        component_valid_check,
        component_remove_check,
        photoFolder,
        id_mainPhoto)
    
    return jsonify(result=[id_requirements, component_number, companent_name, id_companent, component_value, component_type, component_valid_check, component_remove_check, photoFolder, id_mainPhoto])

@app.route('/protocol/requirements/write_components_2', methods=['POST'])
def write_requirements_components_2():
    id_fraction = request.form['id_fraction']
    str_number = request.form['str_number']
    component_value = request.form['component_value']
    component_type = request.form['component_type']
    component_valid_check = request.form['component_valid_check']
    component_warnin_check = request.form['component_warnin_check']
    
    googlesheet_requirements.write_companent_fractionInfo(id_fraction, 
        str_number, 
        component_value, 
        component_type, 
        component_valid_check, 
        component_warnin_check)
    
    return jsonify(result=[id_fraction, str_number, component_value, component_type, component_valid_check, component_warnin_check])  

@app.route('/protocol/requirements/get_requirements', methods=['POST'])
def get_requirements():
    del googlesheet_requirements.list_requirements[:]
    del googlesheet_requirements.list_fraction[:]
    del googlesheet_requirements.list_components[:]
    
    id_requirements = request.form['id_requirements']
    googlesheet_requirements.get_requirements(id_requirements)
    
    results = [table.to_dict() for table in googlesheet_requirements.list_requirements]
    return jsonify(result=results)

@app.route('/protocol/requirements/get_fraction')   
def get_requirements_fraction():
    results = [table.to_dict() for table in googlesheet_requirements.list_fraction]
    return jsonify(result=results)

@app.route('/protocol/requirements/search_fraction')
def search_requirements_fraction():
    results = [table.to_dict() for table in googlesheet_requirements.list_fraction]
    return jsonify(result=results) 
 
@app.route('/protocol/requirements/get_component')   
def get_requirements_components():
    results = []
    for id in range(len(googlesheet_requirements.list_components)):
        results.append(googlesheet_requirements.list_components[id])
    return jsonify(result=results)

#Редактировнание требований
@app.route('/protocol/requirements/edit_requirements', methods=['POST'])
def edit_requirements():
    first_list = []
    for key, value in request.form.items('write_data'):
        if key !="id_requirements" and key !="images_name[]" and key !="base64_images[]":
            first_list.append(value)
    
    id_requirements = request.form['id_requirements']

    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')
    upload_base64_Folder_requirement(id_requirements, first_list[10], base64_images, images_name)
    googlesheet_requirements.edit_requirements(id_requirements, first_list)

    return jsonify(result=first_list)
    
@app.route('/protocol/requirements/edit_fraction', methods=['POST'])
def edit_fraction():
    first_list = []
    second_list = []
    id_value = 0;
    for key, value in request.form.items('write_data[][]'):
        if key !="id_requirements" and key !="images_name[]" and key !="base64_images[]" and key !="fraction_count":
            second_list.append(value)
    
    list = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    first_list = (list(second_list, 11))
    first_list.sort(key = lambda x: int(x[1]))
    
    id_requirements = request.form['id_requirements']
    fraction_count = request.form['fraction_count']
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')    
    
    image_list = []
    name_list = []
    for id in range(len(first_list)):
        del image_list[:]
        del name_list[:]
        if int(first_list[id][10]) == 0:
            image_list.append(base64_images[0])
            name_list.append(images_name[0])
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][10]) == 1:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            image_list.append(base64_images[1])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][10]) == 2:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            image_list.append(base64_images[2])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            name_list.append(images_name[2])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            
        upload_base64_Folder_requirement(id_requirements, first_list[id][9], image_list, name_list)       
            
    googlesheet_requirements.edit_fraction(id_requirements, int(fraction_count), first_list)

    return jsonify(result=first_list)
    
@app.route('/protocol/requirements/edit_components', methods=['POST'])
def edit_requirements_components():
    first_list = []
    second_list = []
    
    id_requirements = request.form['id_requirements']
    fraction_count = request.form['fraction_count']
    component_count = request.form['component_count']
    
    for key, value in request.form.items('write_data[][]'):
        if key !="id_requirements" and key !="images_name[]" and key !="base64_images[]" and key !="fraction_count" and key !="component_count":
            second_list.append(value)
    
    list = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    first_list = (list(second_list,(6 + (int(fraction_count) + 1)*4)))
    
    
    first_list.sort(key = lambda x: int(x[1]))
    
    images_name = request.form.getlist('images_name[]')
    base64_images = request.form.getlist('base64_images[]')    
    
    image_list = []
    name_list = []
    displacement = 0
    for id in range(len(first_list)):
        del image_list[:]
        del name_list[:]
        if int(first_list[id][9]) == 0:
            image_list.append(base64_images[0])
            name_list.append(images_name[0])
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][9]) == 1:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
        if int(first_list[id][9]) == 2:
            image_list.append(base64_images[0])
            image_list.append(base64_images[1])
            image_list.append(base64_images[2])
            name_list.append(images_name[0])
            name_list.append(images_name[1])
            name_list.append(images_name[2])
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            del images_name[0]
            del base64_images[0]
            
        upload_base64_Folder_requirement(id_requirements, first_list[id][8], image_list, name_list)       
            
    googlesheet_requirements.edit_component(id_requirements, int(component_count), int(fraction_count), first_list)

    return jsonify(result=first_list)
#Добавление новых классификаторов для требований
@app.route('/protocol/classifierTemp', methods=['POST'])
def set_classifierTemp():
    first_list = []
    second_list = []
    
    for key, value in request.form.items('write_data[][]'):
        second_list.append(value)
        
    list = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    first_list = (list(second_list, 15))
    
    googlesheet_classifier.classifier_useADD(first_list, len(first_list))

    return jsonify(result=first_list)
    
@app.route('/protocol/get_classifierTemp', methods=['POST'])
def get_classifierTemp():
    list = []
    for key, value in request.form.items('id_list'):
        list.append(value) 
        
    results = googlesheet_classifier.classifier_getADD(list)
    
    return jsonify(result=results)

# Добавление таблицы конкурентов
@app.route('/protocol/competitor_Model')
def get_competitor_Model():
    results = [table.to_dict() for table in googlesheet_competitor.list_Model]
    return jsonify(result=results) 

@app.route('/protocol/competitor_Dillers')
def get_competitor_Diller():
    results = [table.to_dict() for table in googlesheet_competitor.list_Dillers]
    return jsonify(result=results)

#Классификаторы для экономики
@app.route('/protocol/economic_classifierRow')
def get_economic_classifierRow():
    results = [table.to_dict() for table in googlesheet_economic.list_classifierRow]
    return jsonify(result=results)

#Добавление новых данных в таблицу статистики
@app.route('/protocol/write_statistics', methods=['POST'])
def set_statistic():
    list = []
    for key, value in request.form.items('write_data'):
        list.append(value)    
    
    googlesheet_statistic.write_statictic(list)
    
    return jsonify(result=list)
    
#Таблица пользователей менеджеров
@app.route('/protocol/user/manager')
def get_user_manager():
   results = [table.to_dict() for table in googlesheet_user_manager.list_manager]
   return jsonify(result=results)  

#Вызовы для очереи
@app.route('/clientForSaveCheck', methods=['GET'])
def get_clienForSave_Check():
    results = client_queue.clientQueue.queueSave
    time.sleep(random.uniform(0.3, 1.2))
    return jsonify(result=results)

@app.route('/clientForUploadCheck', methods=['GET'])
def get_clienForUpload_Check():
    results = client_queue.clientQueue.queueUpload
    time.sleep(random.uniform(0.3, 1.2))
    return jsonify(result=results)
    
@app.route('/clientForSavePush', methods=['GET'])
def get_clienForSave_Push():
    results = client_queue.clientQueue.queSavePush(1)
    time.sleep(random.uniform(0.3, 1.2))
    return jsonify(result=results)

@app.route('/clientForUploadPush', methods=['GET'])
def get_clienForUpload_Push():
    results = client_queue.clientQueue.queUploadPush(1)
    time.sleep(random.uniform(0.3, 1.2))
    return jsonify(result=[results])   
    
@app.route('/clientForSaveRemove', methods=['GET'])
def get_clienForSave_Remove():
    results = client_queue.clientQueue.queSaveRemove(1)
    time.sleep(random.uniform(0.3, 1.3))
    return jsonify(result=results)

@app.route('/clientForUploadRemove', methods=['GET'])
def get_clienForUpload_Remove():
    results = client_queue.clientQueue.queUploadRemove(1)
    time.sleep(random.uniform(0.3, 1.2))
    return jsonify(result=[results])

@app.route('/checkClientQueue')
def return_queue():
    if client_queue.clientQueue is None:
        results = jsonify(result=[False])
    else:
        results = jsonify(result=[True])
    return results

@app.route('/errorMessageLogger', methods=['POST'])
def errorMessageLogger():
    errorMassage = request.form['errorText']
    print('Error Log: ' + '"' + errorMassage + '"')
    client_queue.clientQueue.queSaveRemove(1)
    return jsonify(result="Error Log Added")

#для аппаратов(commercial_offer_main)
@app.route('/commercial_offer_main/separation/model')
def get_separation_model():
    results = [table.to_dict() for table in googlesheet_apparatus.list_Model]
    return jsonify(result=results)

@app.route('/commercial_offer_main/separation/main')
def get_separation_main():
    results = [table.to_dict() for table in googlesheet_apparatus.list_Main]
    return jsonify(result=results)

@app.route('/commercial_offer_main/separation/configuration')
def get_separation_configuration():
    results = [table.to_dict() for table in googlesheet_apparatus.list_Configuration]
    return jsonify(result=results)

@app.route('/commercial_offer_main/separation/Kompressor')
def get_separation_Kompressor():
    results = [table.to_dict() for table in googlesheet_apparatus.list_Kompressor]
    return jsonify(result=results)
    
@app.route('/commercial_offer_main/separation/KompressorType')
def get_separation_KompressorType():
    results = [table.to_dict() for table in googlesheet_apparatus.list_KompressorType]
    return jsonify(result=results)

@app.route('/commercial_offer_main/separation/Price')
def get_separation_Price():
    results = [table.to_dict() for table in googlesheet_apparatus.list_Price]
    return jsonify(result=results)

@app.route('/commercial_offer_main/separation/Conditions')
def get_separation_Conditions():
    results = [table.to_dict() for table in googlesheet_apparatus.list_Conditions]
    return jsonify(result=results)

@app.route('/commercial_offer_main/separation/CUBER')
def get_CUBER():
     results = [table.to_dict() for table in googlesheet_apparatus.list_Lift]
     return jsonify(result=results)

@app.route('/commercial_offer_main/separation/Import')
def get_Import():
     results = [table.to_dict() for table in googlesheet_apparatus.list_Import]
     return jsonify(result=results)

@app.route('/commercial_offer_main/elevator', methods = ['POST'])
def get_elevator():
    id_deal = request.form['id_deal']  
    id_CO = request.form['id_CO']
    version = request.form["version"]
    documentName = id_deal + "." + id_CO
    #list_Elevator = googlesheet_apparatus.search_Elevator(id_deal, id_CO)
    
    if version == "manager":
        pathfile = 'static/new_data/web_data/'
        req = requests.get("https://csort-transport.ru/" + pathfile + id_deal + "/" + documentName + ".json", verify=False).json()
    elif version == "dealer":
        pathfile = 'static/new_data/web_data/dealer/'
        req = requests.get("https://csort-transport.ru/" + pathfile + id_deal + "/" + documentName + ".json", verify=False).json()
    elif version == "old":
        list_Elevator = googlesheet_apparatus.search_Elevator(id_deal, id_CO)
        req = {"result" : list_Elevator}
        
    return jsonify(req)

@app.route('/commercial_offer_main/translate/Total')
def get_translate_Total():
    results = [table.to_dict() for table in googlesheet_translate.list_Total]
    return jsonify(result=results)

@app.route('/commercial_offer_main/translate/FirstPage')
def get_translate_FirstPage():
    results = [table.to_dict() for table in googlesheet_translate.list_FirstPage]
    return jsonify(result=results)

@app.route('/commercial_offer_main/translate/SpecifMenu')
def get_translate_SpecifMenu():
    results = [table.to_dict() for table in googlesheet_translate.list_SpecifMenu]
    return jsonify(result=results)

@app.route('/commercial_offer_main/translate/Specification')
def get_translate_Specification():
    results = [table.to_dict() for table in googlesheet_translate.list_Specification]
    return jsonify(result=results)

@app.route('/commercial_offer_main/translate/Delivery')
def get_translate_Delivery():
    results = [table.to_dict() for table in googlesheet_translate.list_Delivery]
    return jsonify(result=results)

@app.route('/commercial_offer_main/translate/SmartSort')
def get_translate_SmartSort():
    results = [table.to_dict() for table in googlesheet_translate.list_SmartSort]
    return jsonify(result=results)

@app.route('/commercial_offer_main/translate/Lift')
def get_translate_Lift():
    results = [table.to_dict() for table in googlesheet_translate.list_Lift]
    return jsonify(result=results)

@app.route('/commercial_offer_main/translate/Compressor')
def get_translate_Compressor():
    results = [table.to_dict() for table in googlesheet_translate.list_Compressor]
    return jsonify(result=results)

@app.route('/commercial_offer_main/translate/CompressorP')
def get_translate_CompressorP():
    results = [table.to_dict() for table in googlesheet_translate.list_CompressorP]
    return jsonify(result=results)
    
@app.route('/commercial_offer_main/translate/Elevators')
def get_translate_Elevators():
    results = [table.to_dict() for table in googlesheet_translate.list_Elevators]
    return jsonify(result=results)

@app.route('/commercial_offer_main/translate/Product_translate')
def get_Product_translate():
    results = [table.to_dict() for table in googlesheet_translate_Product.list_List]
    return jsonify(result=results)    


@app.route('/commercial_offer_main/product_k')
def get_product():
    results = [table.to_dict() for table in googlesheet_apparatus.list_product]        
    return jsonify(result=results)

@app.route('/commercial_offer_main/load_offer', methods=['POST'])
def load_offer():
    id_task = request.form['id_task']
    id_offer = request.form['id_offer']
    economicModel = request.form['economicModel']
    list_offer = googlesheet_apparatus.load_CO_Elements(id_task, id_offer, economicModel)    
    return jsonify(result=list_offer)

@app.route('/commercial_offer_main/save_offer', methods=['POST'])
def save_commercial_offer():  
    first_list = []
    for id_row in range(int(request.form['len'])):
        #print(id_row)
        second_list = []
        for key, value in request.form.items('write_data[][]'):
            row_key = key[11:][:1]
            if row_key == str(id_row):
                second_list.append(key[13:].split("[")[1].split("]")[0] +": "+ value)
        second_list.sort()
        first_list.append(second_list)

    managerName = request.form['managerName']
    managerDistrict = request.form['managerDistrict']
        
    return jsonify(result=googlesheet_apparatus.write_statictic(first_list, managerName, managerDistrict))

@app.route('/commercial_offer_main/Aspiration')
def get_separation_Aspiration():
    results = [table.to_dict() for table in googlesheet_apparatus.list_Aspiration]
    return jsonify(result=results)

@app.route('/commercial_offer_main/Bunker')
def get_separation_Bunker():
    results = [table.to_dict() for table in googlesheet_apparatus.list_Bunker]
    return jsonify(result=results)

@app.route('/commercial_offer_main/Complect')
def get_separation_Complect():
    results = [table.to_dict() for table in googlesheet_apparatus.list_Complect]
    return jsonify(result=results)

@app.route('/commercial_offer_main/dealer_info')
def get_dealer_info():
    results = [table.to_dict() for table in googlesheet_dealer.list_dealerInfo]
    return jsonify(result=results)

@app.route('/search_blob_img', methods = ['POST'])
def search_blob_img():
    b64_string = request.data

    image_data = bytes(b64_string)
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    im.save(os.path.join(MYDIR, "static/TestClassifier/img/search_img/search.png")) 
    
    last_updated=dir_last_updated(MYDIR+'/static')
    results = search_img.search_img(MYDIR + "/static/TestClassifier/img/search_img/search.png");
    #URL = "https://yandex.ru/images/search?source=collections&rpt=imageview&url=https://csort-request.ru/static/TestClassifier/img/search_img/search.png?u="+last_updated;
    #print(URL)
    #results = search_img.parce_URL(URL)
    
    return jsonify(result=results)
    
@app.route('/search_pageContent', methods=['POST'])    
def search_pageContent():
    textContent = request.data
    
    results = search_img.parce_textContent(textContent)
    
    return jsonify(result=results)
    
#Сохранение данных по новому образцу
@app.route('/test/save_web_data', methods=['POST'])
def save_web_data():
    documentName = request.json["id_document"]
    
    if os.path.exists(MYDIR + '/static/web_data/' + documentName) == False:
        os.mkdir(MYDIR + '/static/web_data/' + documentName)
    
    with io.open(MYDIR+'/static/web_data/'+documentName+'/'+documentName+".json", 'w', encoding='utf8') as file:
            data = json.dumps(request.json, ensure_ascii=False, indent=4) 
            file.write((data))
        
    return send_from_directory(os.path.join(app.root_path, 'static/web_data/'+documentName), documentName+'.json')
    
#Выгрузка данных по новому образцу
@app.route('/test/load_web_data', methods=['POST'])
def load_web_data():
    documentName = (request.data).decode('utf-8')
    print(documentName)
    
    return send_from_directory(os.path.join(app.root_path, 'static/web_data/'+documentName), documentName+'.json')
    
@app.route('/test/upload_file', methods = ['POST'])
def upload_file():
    print(request.files)
    files = request.files
    documentName = request.form['documentName']   
    
    if os.path.exists(MYDIR + '/static/web_data/' + documentName) == False:
        os.mkdir(MYDIR + '/static/web_data/' + documentName)
    for file in files:  
        print(file)

        path = os.path.join(MYDIR + '/static/web_data/' + documentName, files[file].filename)
        files[file].save(path)
    
    load_company.setYorN(documentName)        
    load_company.load_Classifire_Data(documentName)
    
    return jsonify(result='complete')

@app.route('/test/upload_knopka')
def upload_knopka():
    
    return jsonify(result=load_company.KostyaEbniKnopku())      

#Для работы с битриксом
@app.route('/bitrix/preload_data')
def bitrix_preload_data():
    tears_of_payment = bitrix24_request.get_element_list(161)
    
    list_tears_of_payment = []
    for element in tears_of_payment:
        
        if len(list(element["PROPERTY_1009"].values())) > 1:
            terms_contract = list(element["PROPERTY_1009"].values())[0] + "\n" + list(element["PROPERTY_1009"].values())[1],
        else:
            terms_contract = list(element["PROPERTY_1009"].values())[0]
        
        if len(list(element["PROPERTY_1029"].values())) > 1:
            terms_specification = list(element["PROPERTY_1029"].values())[0] + "\n" + list(element["PROPERTY_1029"].values())[1],
        else:
            terms_specification = list(element["PROPERTY_1029"].values())[0]
            
        list_tears_of_payment.append({
            "id": element["ID"],
            "name": element['NAME'],
            "terms_contract": terms_contract,
            "terms_specification": terms_specification,
        })
        
    __list_tears_of_payment = sorted(list_tears_of_payment, key=lambda d: d['name'])   
    
    results = {
        "tears_of_payment": __list_tears_of_payment
    }
    
    return jsonify(result=results)

@app.route('/bitrix/get_deal', methods = ['POST'])
def bitrix_get_deal():
    deal = bitrix24_request.get_deal(request.json)
    id_user = deal["result"]["ASSIGNED_BY_ID"]
    user_data = bitrix24_request.get_user(id_user)
    
    product = bitrix24_request.get_deal_product(request.json)
    productList = []
    for element in product["result"]:
        productList.append({
            "productName": element["PRODUCT_NAME"],
            "count": element["QUANTITY"],
            "price": element["PRICE"],
            "DISCOUNT_SUM": element["DISCOUNT_SUM"],
            "DISCOUNT_RATE": element["DISCOUNT_RATE"]
        })
    
    #print(deal)
    
    results = {
           "id_deal": deal["result"]["ID"],
           "id_manager": user_data["ID"],
           "managerName": user_data["NAME"],
           "managerLastName": user_data["LAST_NAME"],
           "managerSecondName": user_data["SECOND_NAME"],
           "managerEmail": user_data["EMAIL"],
           "managerPosition": user_data["WORK_POSITION"],
           "managerPhone": user_data["WORK_PHONE"],
           "managerImg": user_data["PERSONAL_PHOTO"],
           "managerDistrict": user_data["PERSONAL_CITY"],
           "productList": productList,
           #"titleDeal": deal["result"]["TITLE"],
           "comercialOfferElementIDs": deal["result"]["UF_CRM_1673438603"],
           "deliveryElementInfo": {
                "deliveryPrice": deal["result"]["UF_CRM_1679466250"],
                "deliveryAdress": deal["result"]["UF_CRM_1679466187"],
                "tearsOfPayment": deal["result"]["UF_CRM_1679467146"],
           },
           #"invoiceID": deal["result"]["UF_CRM_1676115654"]
    }
    
    return jsonify(result=results)
    
@app.route('/bitrix/update_deal', methods = ['POST'])
def bitrix_update_deal():    
    #print(request.json)
    entry = {
        "id": request.json["product"]["id"],
        "rows":[]
    }
    
    set_deal_product = bitrix24_request.set_deal_product(entry)#Обнуление списка продуктов
    set_deal_product = bitrix24_request.set_deal_product(request.json["product"])
    update_deal = bitrix24_request.update_deal(request.json["projectList"])
    
    #Работа со счетами сделки
    id_deal = request.json["projectList"]["id"]
    
    _data = {
        "ID": id_deal
    }
    
    get_deal = bitrix24_request.get_deal(_data)
    dealTitle = get_deal["result"]["TITLE"]
    invoicesID = get_deal["result"]["UF_CRM_1676115654"]
    print(invoicesID)
    
    ApparatInvoice = request.json["smartInInvoice"]["ApparatInvoice"]
    KompressorInvoice = request.json["smartInInvoice"]["KompressorInvoice"]
    ElevatorInvoice = request.json["smartInInvoice"]["ElevatorInvoice"]
    AddEquipmentInvoice = request.json["smartInInvoice"]["AddEquipmentInvoice"]
    ImportInvoice = request.json["smartInInvoice"]["ImportInvoice"]
    
    ElevatirModelList = list(set(ElevatorInvoice["ElevatirModelList"]))
    ApparatModelList = list(set(ApparatInvoice["ApparatModelList"]))
    ImportModelList = []
    
    #Вынесение исключений для списка моделей
    if "MiniSort" in ApparatModelList:
        ApparatModelList.remove("MiniSort")
        ImportModelList.append("MiniSort")
    
    _invoiceID = []
    
    #Обновление существующего списка счетов
    for ids in invoicesID:
        get_invoice = bitrix24_request.get_smart_invoice(ids)
        typeID = get_invoice["ufCrm_SMART_INVOICE_1676255170530"]
        
        
        if ApparatInvoice["active"] and typeID == ApparatInvoice["ufCrmSmartInvoice1676255170530"]:  
            fields = {
                "ufCrm_SMART_INVOICE_1681118850": ApparatModelList
            }
        
            bitrix24_request.set_smart_invoice_product(ids, [])
            
            for product in ApparatInvoice["productRows"]:
                bitrix24_request.add_smart_invoice_product(ids, product)
            
            
            update_invoice = bitrix24_request.update_smart_invoice(ids, fields)
            ApparatInvoice["active"] = False
            _invoiceID.append(ids)
            
        elif KompressorInvoice["active"] and typeID == KompressorInvoice["ufCrmSmartInvoice1676255170530"]:        
            
            bitrix24_request.set_smart_invoice_product(ids, [])
            
            for product in KompressorInvoice["productRows"]:
                update_invoice = bitrix24_request.add_smart_invoice_product(ids, product)
            
            KompressorInvoice["active"] = False
            _invoiceID.append(ids)
            
        elif ElevatorInvoice["active"] and typeID == ElevatorInvoice["ufCrmSmartInvoice1676255170530"]:        
            fields = {
                "ufCrm_SMART_INVOICE_1676255170530": "1563",
                "ufCrm_SMART_INVOICE_1681118850": ElevatirModelList
            }
            
            bitrix24_request.set_smart_invoice_product(ids, [])
            
            for product in ElevatorInvoice["productRows"]:
                bitrix24_request.add_smart_invoice_product(ids, product)
            
            update_invoice = bitrix24_request.update_smart_invoice(ids, fields)
            ElevatorInvoice["active"] = False
            _invoiceID.append(ids)
            
        elif AddEquipmentInvoice["active"] and typeID == AddEquipmentInvoice["ufCrmSmartInvoice1676255170530"]:        
            
            bitrix24_request.set_smart_invoice_product(ids, [])
            
            for product in AddEquipmentInvoice["productRows"]:
                bitrix24_request.add_smart_invoice_product(ids, product)
            
            AddEquipmentInvoice["active"] = False
            _invoiceID.append(ids)
            
        elif ImportInvoice["active"] and typeID == ImportInvoice["ufCrmSmartInvoice1676255170530"]:        
            
            bitrix24_request.set_smart_invoice_product(ids, [])
            
            for product in ImportInvoice["productRows"]:
                bitrix24_request.add_smart_invoice_product(ids, product)
            
            ImportInvoice["active"] = False
            _invoiceID.append(ids)
            
        else:
            delete_invoice = bitrix24_request.delete_smart_invoice(ids)
            
    #Создание недостающих типов счетов
    if ApparatInvoice["active"]:
        fields = {
            "ufCrm_SMART_INVOICE_1676255170530": ApparatInvoice["ufCrmSmartInvoice1676255170530"],
            "ufCrm_SMART_INVOICE_1681118850": ApparatModelList,
            "assignedById": ApparatInvoice["assignedById"],
            "parentId2": ApparatInvoice["parentId2"],
            "title": dealTitle + " ColorSorter",
        }
        
        create_invoice = bitrix24_request.create_smart_invoice(fields)
        for product in ApparatInvoice["productRows"]:
                bitrix24_request.add_smart_invoice_product(create_invoice["id"], product)
        
        _invoiceID.append(create_invoice["id"])
     
    if KompressorInvoice["active"]:
        fields = {
            "ufCrm_SMART_INVOICE_1676255170530": KompressorInvoice["ufCrmSmartInvoice1676255170530"],
            "assignedById": KompressorInvoice["assignedById"],
            "parentId2": KompressorInvoice["parentId2"],
            "title": dealTitle + " Compressor",
        }
        
        create_invoice = bitrix24_request.create_smart_invoice(fields)
        for product in KompressorInvoice["productRows"]:
                bitrix24_request.add_smart_invoice_product(create_invoice["id"], product)
        
        _invoiceID.append(create_invoice["id"])
     
    if ElevatorInvoice["active"]:
        fields = {
            "ufCrm_SMART_INVOICE_1676255170530": ElevatorInvoice["ufCrmSmartInvoice1676255170530"],
            "ufCrm_SMART_INVOICE_1681118850": ElevatirModelList,
            "assignedById": ElevatorInvoice["assignedById"],
            "parentId2": ElevatorInvoice["parentId2"],
            "title": dealTitle + " Elevator",
        }
        
        create_invoice = bitrix24_request.create_smart_invoice(fields)
        for product in ElevatorInvoice["productRows"]:
                bitrix24_request.add_smart_invoice_product(create_invoice["id"], product)
        
        _invoiceID.append(create_invoice["id"])
        
    if AddEquipmentInvoice["active"]:
        fields = {
            "ufCrm_SMART_INVOICE_1676255170530": AddEquipmentInvoice["ufCrmSmartInvoice1676255170530"],
            "assignedById": AddEquipmentInvoice["assignedById"],
            "parentId2": AddEquipmentInvoice["parentId2"],
            "title": dealTitle + " AddEquipment",
        }
        
        create_invoice = bitrix24_request.create_smart_invoice(fields)
        for product in AddEquipmentInvoice["productRows"]:
                bitrix24_request.add_smart_invoice_product(create_invoice["id"], product)
        
        _invoiceID.append(create_invoice["id"])
        
    if ImportInvoice["active"]:
        fields = {
            "ufCrm_SMART_INVOICE_1676255170530": ImportInvoice["ufCrmSmartInvoice1676255170530"],
            "assignedById": ImportInvoice["assignedById"],
            "parentId2": ImportInvoice["parentId2"],
            "title": dealTitle + " Import",
        }
        
        create_invoice = bitrix24_request.create_smart_invoice(fields)
        for product in ImportInvoice["productRows"]:
                bitrix24_request.add_smart_invoice_product(create_invoice["id"], product)
        
        _invoiceID.append(create_invoice["id"])
    
    __data = {
        "id": id_deal,
        "fields":{
            "UF_CRM_1676115654": _invoiceID
        } 
    }
    
    update_invoiceID = bitrix24_request.update_deal(__data)
            
    
    return jsonify(set_deal_product,update_deal,update_invoiceID)

@app.route('/bitrix/get_smart_deal', methods = ['POST'])
def bitrix_get_smart_deal():
    id_smart = request.json["ID"]
    smartDeal = bitrix24_request.get_smart(id_smart)
    id_dealer = smartDeal["ufCrm27_1671426538"]
    id_company = smartDeal["ufCrm27_1671604083"]
    dealer_data = bitrix24_request.get_contact(id_dealer)
    company_data = bitrix24_request.get_company(id_company)
    
    product = bitrix24_request.list_smart_product(id_smart)
    productList = []
    for element in product["productRows"]:
        productList.append({
            "productName": element["productName"],
            "count": element["quantity"],
            "price": element["price"],
            "DISCOUNT_SUM": element["discountSum"],
            "DISCOUNT_RATE": element["discountRate"]
        })
    
    
    results = {
            "id_smart": request.json["ID"],
            "id_dealer": id_dealer,
            "dealerCompany": company_data["TITLE"],
            "dealerName": dealer_data["NAME"],
            "dealerLastName": dealer_data["LAST_NAME"],
            "dealerSecondName": dealer_data["SECOND_NAME"],
            "dealerEmail": dealer_data["EMAIL"][0]["VALUE"],
            "dealerPosition": dealer_data["POST"],
            "dealerPhone": dealer_data["PHONE"][0]["VALUE"],
            "dealerImg": smartDeal["ufCrm27_1671529593"],
            "dealerLogoMain": smartDeal["ufCrm27_1671529612"],
            "dealerLogoADD": smartDeal["ufCrm27_1671529631"],
            "dealerDiscription": smartDeal["ufCrm27_1671428180"],
            "dealerTitleDiscription": smartDeal["ufCrm27_1672204199"],
            "telegramName": smartDeal["ufCrm27_1672203914"],
            "telegramURL": smartDeal["ufCrm27_1672204502"],
            "telegramQR": smartDeal["ufCrm27_1672202716"],
            "telegramDiscription": smartDeal["ufCrm27_1672203932"],
            "productList": productList,
            "comercialOfferElementIDs": smartDeal["ufCrm27_1694418527"]
            #ufCrm27_1694418608 Состав проекта
            #ufCrm27_1694418661 id счетов
    }
    
    return jsonify(result=results)

@app.route('/bitrix/update_smart_deal', methods = ['POST'])
def bitrix_update_smart_deal():
    id_smart = request.json["id"]
    productRows = request.json["productRows"]
    fields = request.json["projectList"]["fields"]
    
    set_smart_product = bitrix24_request.set_smart_product(id_smart, [])#Обнуление списка продуктов
    
    for product in productRows:
        bitrix24_request.add_smart_product(id_smart, product)
        
    update_smart = bitrix24_request.update_smart(id_smart, fields)
    
    return jsonify(set_smart_product, update_smart)

# сохранение данных в фотрмате джсон для кп

@app.route('/commercial_offer_main/save_mainCO_data', methods = ['POST'])
def mainCO_dataSave():    
    with io.open( MYDIR+'/static/web_data/mainCO_data/mainCO_data.json', 'w', encoding='utf8') as file:
        data = json.dumps(request.json, ensure_ascii=False, indent=4) 
        file.write( (data))
       
    return send_from_directory(os.path.join(app.root_path, 'static/web_data/mainCO_data'), 'mainCO_data.json')

@app.route('/commercial_offer_main/load_mainCO_data')
def mainCO_dataLoad():
    return send_from_directory(os.path.join(app.root_path, 'static/web_data/mainCO_data'), 'mainCO_data.json')

# для загрузки файлов джсон хранящих данные по объектам

@app.route('/edit_json/load', methods=['GET'])
def json_load():
    files = [name for name in os.listdir(MYDIR+'/static/editData/web_Data') if name.endswith('.json')]
    
    return jsonify(result=files)

@app.route('/edit_json/load_web_data_edit', methods=['POST'])
def load_web_data_edit():
    jsonElement = request.get_json()
    documentName = jsonElement["id_document"]
    print(documentName)
    return send_from_directory(os.path.join(app.root_path, 'static/editData/web_Data'), documentName + '.json')

@app.route('/edit_json/save_web_data_edit', methods = ['POST'])
def save_web_data_edit():
    id_document = request.json["documentName"]
    document_main = request.json["data"]
    with io.open( MYDIR+'/static/editData/web_data/'+ id_document +'.json', 'w', encoding='utf8') as file:
            data = json.dumps(document_main, ensure_ascii=False, indent=4) 
            file.write( (data))
       
    return send_from_directory(os.path.join(app.root_path, 'static/editData/web_data'), id_document +'.json')


@app.route('/test/translate')
def get_translate_company():
    results = {
        'Title': [table.to_dict() for table in googlesheet_translate_PR.list_Title],
        'Req':[table.to_dict() for table in googlesheet_translate_PR.list_Req],
        'Prot':[table.to_dict() for table in googlesheet_translate_PR.list_Prot],
        'Sort':[table.to_dict() for table in googlesheet_translate_PR.list_Sort],
        'Econom':[table.to_dict() for table in googlesheet_translate_PR.list_Econom]
    }
    return jsonify(result=results)


if __name__ == "__main__":
    googlesheet_classifier.upload_google_table()
    googlesheet_user_manager.upload_google_table()
    googlesheet_apparatus.upload_google_table()
    googlesheet_competitor.upload_google_table()
    googlesheet_economic.upload_google_table()
    googlesheet_dealer.upload_google_table()
    googlesheet_calendarDnD.load_data_calendar()
    googlesheet_translate.upload_google_table()
    googlesheet_translate_PR.upload_google_table()
    googlesheet_translate_Product.upload_google_table()
    #НАСТРОЙ КАРТИНКИ!!!!!
    #НАСТРОЙ Яндекс поиск!!!!!
    client_queue.setup_clientQueue()
    app.run()