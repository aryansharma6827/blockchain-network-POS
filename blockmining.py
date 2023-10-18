from account import accounts
import copy
import hashlib
import time
import json
import math
from utils import BlockchainUnits
from hashlib import sha256
import random
import pprint








class mineblock():
    def __init__(self,acc):
        self.nodes =  [*(acc.distributer), *(acc.client), acc.manufacturer]
    
    def stake_distributor(self):
       for node in self.nodes:
          node.stake_provider(round(random.random()*1000))
    def stake_verifyer(self,number):
        mindiff = 100
        selected_node = self.nodes[0]
        for node in self.nodes:
            s1 = int(node.stake)
            while s1 > 0:
                r1 = random.randint(0,100)
                if number -r1 < 0:
                    check = -(number-r1)
                    s1 = s1-1
                else:
                    check = (number-r1)
                    s1 = s1-1
                if check < mindiff:
                    mindiff = check
                    selected_node = node
        return selected_node

   
    def print_stakes(self):
        print('stakes of different nodes are: \n')
        for node in self.nodes:
            print('{name}: {stake}'.format(name = node.name,stake = node.stake))    

                  
    
    def mine(self,blockchain,pool):
      lasthash = BlockchainUnits.hash(blockchain.blocks[-1].payload()).hexdigest()
      blockcount = blockchain.blocks[-1].blockcount+1
      transaction=[]
      transaction.append(pool.transactions[0])
      transaction.append(pool.transactions[1])
      pool.transactions.pop(0)
      pool.transactions.pop(0)
      number = random.randint(1,100)
      miner  = self.stake_verifyer(number)
      print('The node with highest stake is: {name}'.format(name = miner.name))
      block = miner.wallet.creatblock(transaction,lasthash,blockcount)
      block.merk(block.build_merkle_tree())
      if blockchain.blockcountvalid(block) and blockchain.lastblockvalid(block):
         blockchain.addblock(block)
      print(block.printb())
      return block       