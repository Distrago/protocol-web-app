# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import api_google

from apiclient.http import MediaFileUpload

#Folder protocol_IMG
MainProtocolFoldre = "1EB0uN252l8ITM1i8kOnv0yAkAvBeV6Jl"
Template_IMG = "12M4IfIKTUbO-QKCPA57dEIJAF3xIl3VJ"

service_drive = api_google.service_drive


def create_new_folder(folderName):
    folder_metadata = {
        'name': folderName,
        'parents': [MainProtocolFoldre],
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = service_drive.files().create(body=folder_metadata,
                                        fields="id").execute()
    return folder['id']
    
    
def upload_img(img_name, folder):
    
    file_metadata = {
    'name': img_name,
    'parents': [folder]
    }
    media = MediaFileUpload('static/img/save_img/'+img_name+'.png',
                        mimetype='image/jpeg',
                        resumable=True)
                        
    file = service_drive.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    return file['id']