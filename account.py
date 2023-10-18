from Crypto.PublicKey import RSA 
from wallet import Wallet
import pprint
class accounts():
    def __init__(self):
        self.distributer=[]
        self.client=[]
        self.manufacturer=acc('manufacturer',0)
        

    def adddistaccount(self):
        name = input('input name of distributer\n')
        stake = input('enter your stake between 0 to 100')
        obj=acc(name,stake)
        self.distributer.append(obj)
        # print(self.distributer)


    
    def addclientaccount(self):
        name = input('input name of client\n')
        stake = input('enter your stake between 0 to 100')
        obj=acc(name,stake)
        self.client.append(obj)
        # print(self.client)

    def pri(self,n):
        names=[]
        keys=[]
        for i in n:
            names.append(i.name)
            names.append(i.wallet.publickeystring())
        pprint.pprint(names)
        pprint.pprint(keys)
            

        

    
# Implementation of the 5th feature
class acc():
    def __init__(self,name,stake):
        self.name=name
        self.amount=0
        self.wallet=Wallet()
        self.publickey=0
        self.pdi=0
        self.flag=False   #This variable is introduced for implementing the 5th feature 
        self.stake = stake #The variable flag is used like a tag onece the tag reaches the customer then only the next delivery can be initiated

    def stake_provider(self, stake):
        self.stake = stake    





