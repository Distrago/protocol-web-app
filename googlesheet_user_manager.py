# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google
service = api_google.service_sheets

#Manager table work
Manager_technicianID = "17uxerDvEqqpN8ksIHmFOxjlT0_tgpJ1GyztUvcejhfs"
#Table Range
Manager_Range = "Manager!A2:G"

class Manager:
    def __init__ (self, id_user, name, mail, phone, rank_position, district, photo):
        self.id_user = id_user
        self.name = name
        self.mail = mail
        self.phone = phone
        self.rank_position = rank_position
        self.district = district
        self.photo = photo
    def to_dict(self):
        return {"id_user": self.id_user,
               "name": self.name,
               "mail": self.mail,
               "phone": self.phone,
               "rank_position": self.rank_position,
               "district": self.district,
               "photo": self.photo}
list_manager = []

def read_manager():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=Manager_technicianID,
                                range=Manager_Range).execute()
    values = result.get('values', [])

    for row in values:
        list_manager.append(Manager(row [0], row[1], row[2], row[3], row[4], row[5], row[6]))
    print(('������� ���������� ����������!', 'cp1251'))

def upload_google_table():
    read_manager()