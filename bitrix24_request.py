# -*- coding: utf-8 -*-
import requests
import json

example = {
		"cmd": {
			"user": "user.get?ID=1"
		}
	}



def get_deal(data):
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.deal.get.json?"
    req = requests.post(webhook, json=data) 
    
    jsonData = json.loads(req.text)
    
    
    return jsonData

def update_deal(data):
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.deal.update.json?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData 
    
def create_deal(data):
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.deal.add"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData
    
def set_deal_product(data):
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.deal.productrows.set?"
    req = requests.post(webhook, json=data)
    
    jsonData = json.loads(req.text)
    
    return jsonData
    
def set_deal_product(data):
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.deal.productrows.set?"
    req = requests.post(webhook, json=data)
    
    jsonData = json.loads(req.text)
    
    return jsonData
    
def get_deal_product(data):
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.deal.productrows.get?"
    req = requests.post(webhook, json=data)
    
    jsonData = json.loads(req.text)
    
    return jsonData

def get_user(user_id):
    data = {
		"cmd": {
			"user": "user.get?ID="+user_id
		}
	}
    
    #print(data)


    webhook = "https://csort24.bitrix24.ru/rest/13/fvgbmufwxfwua58t/batch.json?"
    req = requests.post(webhook, json=data)
    jsonData = json.loads(req.text)
    #print(jsonData)
    
    return jsonData["result"]["result"]["user"][0]
    
def get_smart(item_id):
    data = {
        "entityTypeId": 129,
        "id":item_id
    }
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.get?"
    req = requests.post(webhook, json=data)
    
    jsonData = json.loads(req.text)
    
    return jsonData["result"]["item"]    

def update_smart(item_id,fields):
    data = {
        "entityTypeId": 129,
        "id":item_id,
        "fields": fields
    }
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.update?"
    req = requests.post(webhook, json=data)
    
    jsonData = json.loads(req.text)
    
    return jsonData["result"]["item"]

def get_contact(contact_id):
    data = {
        "id":contact_id
    }


    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.contact.get?"
    req = requests.post(webhook, json=data)
    
    jsonData = json.loads(req.text)
    
    return jsonData["result"]
    
def get_company(company_id):
    data = {
        "id":company_id
    }
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.company.get?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]


def get_enum():
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.enum.ownertype?"
    req = requests.post(webhook)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]

def add_smart_product(item_id, product):
    data = {        
        "fields":{
            "ownerId": item_id,
            "ownerType": "T81",
            "productName": product["productName"],
            "price": product["price"],
            "discountTypeId": product["discountTypeId"],
			"taxRate": product["taxRate"],
			"taxIncluded": product["taxIncluded"],
			"quantity": product["quantity"],
			"measureCode": product["measureCode"],
			"measureName": product["measureName"]
            }
    }
    
    if product["discountTypeId"] == 1:
        data["fields"]["discountSum"] = product["discountSum"]
    else:
        data["fields"]["discountRate"] = product["discountRate"]
    
    #data["productRows"].append({
    #    "productName": "54548",
    #    "price": 1000,
    #    "discountTypeId": 1,
    #    "taxRate" : 20,
    #    "taxIncluded": "Y"
    #})

    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.productrow.add?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]
    
def set_smart_product(item_id, productRows):
    data = {
        "ownerId": item_id,
        "ownerType": "T81",
        "productRows": productRows
    }
    
    #data["productRows"].append({
    #    "productName": "54548",
    #    "price": 1000,
    #    "discountTypeId": 1,
    #    "taxRate" : 20,
    #    "taxIncluded": "Y"
    #})

    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.productrow.set?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]

def list_smart_product(item_id):
    data = {
        "filter": {
            "=ownerType": "T81",
            "=ownerId": item_id
        }
    }

    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.productrow.list?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]

#Работа со счетами
def create_smart_invoice(fields):
    data = {
        "entityTypeId": 31,
        "fields": fields
    } 
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.add?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]["item"]

#Типы договоров
#1559 - Фотосепаратор
#1561 - Компрессор
#1563 - Элеватор
#2243 - Фотосепаратор Импортный
def get_smart_invoice(item_id):
    data = {
        "entityTypeId": 31,
        "id":item_id
    }
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.get?"
    req = requests.post(webhook, json=data)
    
    jsonData = json.loads(req.text)
    
    return jsonData["result"]["item"]
    
def update_smart_invoice(item_id,fields):
    data = {
        "entityTypeId": 31,
        "id":item_id,
        "fields": fields
    } 
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.update?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]["item"]
    
def delete_smart_invoice(item_id):
    data = {
        "entityTypeId": 31,
        "id":item_id
    }
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.delete?"
    req = requests.post(webhook, json=data)
    
    jsonData = json.loads(req.text)
    
    return jsonData["result"]   
    
def add_smart_invoice_product(item_id, product):
    data = {
        "fields":{
            "ownerId": item_id,
            "ownerType": "SI",
            "productName": product["productName"],
            "price": product["price"],
            "discountTypeId": product["discountTypeId"],
			"taxRate": product["taxRate"],
			"taxIncluded": product["taxIncluded"],
			"quantity": product["quantity"],
			"measureCode": product["measureCode"],
			"measureName": product["measureName"]
            }
    }
    
    if product["discountTypeId"] == 1:
        data["fields"]["discountSum"] = product["discountSum"]
    else:
        data["fields"]["discountRate"] = product["discountRate"]
        
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.productrow.add?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]
    
def set_smart_invoice_product(item_id, productRows):
    data = {
        "ownerId": item_id,
        "ownerType": "SI",
        "productRows": productRows
    }

    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.productrow.set?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]

def list_smart_invoice_product(item_id):
    data = {
        "filter": {
            "=ownerType": "SI",
            "=ownerId": item_id
        }
    }

    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.item.productrow.list?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]
    
def catalog_list():
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.catalog.list?"
    req = requests.post(webhook)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]    

def catalog_get(item_id):
    data = {
        "id" : item_id
    }


    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.catalog.get?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]
    
def get_product_list(CATALOG_ID, SECTION_ID):
    data = {
        "order": { "NAME": "ASC" },
        "filter": { "CATALOG_ID": CATALOG_ID, "SECTION_ID": SECTION_ID},
        "select": [ "ID", "NAME", "DESCRIPTION", "PROPERTY_1069"]
    }
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.product.list?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]
    
def get_product_full_list(CATALOG_ID):
    data = {
        "order": { "NAME": "ASC" },
        "filter": { "CATALOG_ID": CATALOG_ID},
        "select": [ "ID", "NAME", "DESCRIPTION"]
    }
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.product.list?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]
    
def get_product(item_id):
    data ={
        "ID": item_id
    }
    
    webhook = "https://csort24.bitrix24.ru/rest/15/dwnnhv6hs0bkufsi/crm.product.get?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]

def get_element_list(list_id):
    data = {
        "IBLOCK_TYPE_ID": 'lists',
        "IBLOCK_ID": list_id
    }
    
    webhook = "https://csort24.bitrix24.ru/rest/13/fvgbmufwxfwua58t/lists.element.get?"
    req = requests.post(webhook, json=data)
   
    jsonData = json.loads(req.text)
    
    return jsonData["result"]

if __name__ == "__main__":
    data = {
        "ID": 22311
    }

    # req = get_deal(data)["result"]["UF_CRM_1679467146"]
    # print(req)
    # print("------------")
    # req = get_element_list(161)
    # print(req)
    # print("------------")

    req = get_product_list("25","59")
    print(req)
    print("------------")
    list_req = []

    for element in req:
        req2 = get_product(element["ID"])
        list_req.append(req2)
        print(req2)
    print("------------")
    print(list_req)