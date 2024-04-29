# -*- coding: utf-8 -*-
import time

#Чило клиетов
class Client:
    def __init__(self, queueSave, queueUpload):
        self.queueSave = queueSave
        self.queueUpload = queueUpload
    def queSavePush(self, value):
        self.queueSave += value
        return self.queueSave
    def queUploadPush(self, value):
        self.queueUpload += value
        return self.queueUpload
    def queSaveRemove(self, value):
        self.queueSave -= value
        return self.queueSave
    def queUploadRemove(self, value):
        self.queueUpload -= value
        return self.queueUpload
                
clientQueue = None

def setup_clientQueue():
    global clientQueue
    clientQueue = Client(0,0)
    print("Queue Setup!")