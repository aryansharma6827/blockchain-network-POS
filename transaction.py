import uuid
import time
import copy

class Transaction():
    def __init__(self,senderpublickey,recieverpublickey,amount,name):
        self.senderpublickey=senderpublickey
        self.recieverpublickey=recieverpublickey
        self.amount=amount
        self.name=name
        self.id=uuid.uuid1().hex
        self.timestamp=time.time()
        self.signature=''
        
        
    def sign(self,signature):
        self.signature=signature
    def payload(self):
        jsonRepresentation=copy.deepcopy(self.__dict__)
        jsonRepresentation['signature'] = ''
        return jsonRepresentation
    
    def equals(self,transaction):
        if self.id == transaction.id:
            return True
        else:
            return False
