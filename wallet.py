from Crypto.PublicKey import RSA 
from utils import BlockchainUnits
from Crypto.Signature import PKCS1_v1_5
from block import Block
from transaction import Transaction
import uuid
class Wallet():
      
    def __init__(self):
      self.keypair=RSA.generate(2048)
      self.dist = {}
      self.customer= {}

    def sign(self,data):
      datahash=BlockchainUnits.hash(data)
      signatureSchemeObject=PKCS1_v1_5.new(self.keypair)
      signature = signatureSchemeObject.sign(datahash)
      return signature.hex()

    @staticmethod

    def signaturevalid(data,signature,publickeystring):
      signature=bytes.fromhex(signature)
      datahash=BlockchainUnits.hash(data)
      publickey=RSA.importKey(publickeystring)
      signatureSchemeObject=PKCS1_v1_5.new(publickey)
      signaturevalid=signatureSchemeObject.verify(datahash,signature)
      return signaturevalid


    def publickeystring(self):
      publickeystring=self.keypair.publickey().exportKey('PEM').decode('utf-8')
      return publickeystring 


    def creattransaction(self,reciever,amount,name):
      transaction =Transaction(self.publickeystring(),reciever,amount,name)
      signature=self.sign(transaction.payload())
      transaction.sign(signature)
      return transaction

    def creatblock(self,transactions,lasthash,blockcount):
      block=Block(transactions,lasthash,self.publickeystring(),blockcount)
      signature=self.sign(block.payload())
      block.sign(signature)
      return block
    
    



 

#  for every object of class wallet new key pair will be generated