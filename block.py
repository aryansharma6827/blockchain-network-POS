import copy
import hashlib
import time
import jsonmerge
import json
import math
from utils import BlockchainUnits
from hashlib import sha256
class Block():

    def __init__(self,transactions,lasthash,forger,blockcount):
        self.transactions=transactions
        self.lasthash=lasthash
        self.forger=forger
        self.blockcount=blockcount
        self.timestamp =time.time()
        self.signature=''
        self.merkleroot=0
        self.transactionhashes=[]

    @staticmethod
    def genesis():
        genesisblock=Block([],'genesishash','genesis',0)
        genesisblock.timestamp=0
        return genesisblock

    
    def printb(self):
        data={}
        data['lastHash']=self.lasthash
        data['forger']=self.forger
        data['blockcount']=self.blockcount
        data['timestamp']=self.timestamp
        data['merkleroot']=self.merkleroot
        data['sign']=self.signature
        jsontransaction =[]
        for transaction in self.transactions:
            jsontransaction.append(transaction.__dict__)
        data['transaction']=jsontransaction
        return data
    
    def payload(self):
        jsonRepresentation=copy.deepcopy(self.printb())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    def sign(self,signature):
        self.signature=signature

    def hashgen(self):
        for tran in self.transactions:
            self.transactionhashes.append(str((BlockchainUnits.hash(tran.__dict__))))
        return self.transactionhashes

    def build_merkle_tree(self):
        
        transaction_hashes = []
        for tx in self.transactions:
             hashstr = '{}'.format(tx)
             transaction_hashes.append((sha256((hashstr).encode('utf-8')))) 
        if len(transaction_hashes) % 2 != 0: # If odd number of transactions, duplicate last transaction to make it even
            transaction_hashes.append(transaction_hashes[-1]) # merkle tree requires even number of leaf nodes
        kk = math.log2(len(transaction_hashes))
        while kk >= 1:
            new_hashes = [] # pair up adjacent hashes to make a new hash , until only one reamins
            for i in range(0, len(transaction_hashes), 2):
                concatenated_hash = '{}{}'.format(transaction_hashes[i], transaction_hashes[i+1])
                new_hashes.append(hashlib.sha256((concatenated_hash).encode('utf-8')).hexdigest())
                transaction_hashes = new_hashes
            kk = kk - 1
            if (len(transaction_hashes)) % 2 != 0:
                transaction_hashes.append(transaction_hashes[-1])
        return transaction_hashes[0]

    def merk(self,hash):
        self.merkleroot=hash




# jsonmerge.merge(transaction_hashes[i].__dict__,transaction_hashes[i+1].__dict__)