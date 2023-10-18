from transaction import Transaction
from transactionpool import Transactionpool
from wallet import Wallet
import copy
from qr import qrgenerator
from product import product
import json
from account import accounts
from utils import BlockchainUnits
from blockchain import Blockchain
from blockmining import mineblock
from block import Block
if __name__=='__main__':
    name='Transfer'
    amount=1
    acc=accounts()
    pool =Transactionpool()
    wallet=Wallet()
    blockchain =Blockchain()
    
    # This is a menu driven program which has 9 options each indicated with it's purpose in the print statement 
    #
    while True:  
      print("\nMENU")  
      print("1. To add distributor account\n")  
      print("2. To add client account\n")  
      print("3. To print the distributors and clients\n")  
      print("4. For transaction distributor to client\n")
      print("5. For transaction manufacturer to distributor\n")   
      print("6. For block mining and printing\n")  
      print("7. For QR\n")  
      print("8. transaction issue")
      print("0. Exit\n")  
      choice = int(input("\nEnter the Choice: ")) 
      if(choice==1): 
        acc.adddistaccount()
      elif(choice==2):
        acc.addclientaccount()
      elif(choice==3):
        print(acc.pri(acc.distributer))
        print(acc.pri(acc.client))
      elif(choice==4):
        n=int(input('Enter the distributer number'))
        m=int(input('Enter the client number'))
        if acc.distributer[n-1].flag==False:
          print('manufacturer dont have any product')
          continue
        name=acc.distributer[n-1].name
        reciever = acc.client[m-1].wallet.publickeystring()
        acc.client[m-1].pdi = pdt.uid
        transaction =acc.distributer[n-1].wallet.creattransaction(reciever,amount,name)
        if pool.transactionexist(transaction)== False:
          pool.addtransaction(transaction)
        acc.distributer[n-1].flag=False
      elif(choice==5):
        n=int(input('Enter the distributer number'))
        name='manufacturer'
        if acc.distributer[n-1].flag==True:
          acc.distributer[n-1].pdi=0
          print("distributor already has the product cannot recieve another")
          continue
        reciever = acc.distributer[n-1].wallet.publickeystring()
        transaction =acc.manufacturer.wallet.creattransaction(reciever,amount,name)
        pdt=product()
        acc.distributer[n-1].pdi=pdt.uid
        acc.distributer[n-1].flag=True
        if pool.transactionexist(transaction)== False:
          pool.addtransaction(transaction)

      elif(choice==6):
        miner=mineblock(acc)
        block=miner.mine(blockchain,pool) 
      elif(choice==7):
        d=qrgenerator.blockreducer(block)
        qrgenerator.generateqr(d)
      elif(choice ==8):
        a = int(input("customer number\n"))
        b = int(input("distuber number\n"))
        k = input("customer recive y/n\n")
        m = input("distuber send y/n\n")
        # Implementation of the sixth feature
        if acc.client[a-1].pdi == acc.distributer[b-1].pdi == pdt.uid:       #Verifies whether every user in the transaction has the same product ID
          if k == 'n' and m == 'y':                    #If all the parties have the same product ID then the transaction has occured and the hence the lier is found  
            print('customer is lying')
            acc.client[a-1].stake=0              #Accordingly the guilty party is fined for lying and the stake is made zero      
          else:
            print('distrubter is lying')
            acc.distributer[b-1].stake=0
      else:
        break
    

    


      


    
    

    # reciever = acc.client[0].wallet.publickeystring()
    
    

    # transaction =wallet.creattransaction(reciever,amount1,type)
    # if pool.transactionexist(transaction)== False:
    #   pool.addtransaction(transaction)


 
    # print(transaction.__dict__)
    # pool.prin()   
    
    # block =Block(pool.transactions,'lasthash','forger',1)

    # print(block.printb())

    # print(transaction.__dict__)
    # signaturevalid=wallet.signaturevalid(transaction.payload(),transaction.signature,wallet.publickeystring())
    # print(signaturevalid)

    
 # fraudwallet =Wallet() if we check its validity bu sending fraudwallet.publickey then false comes

















# blockchain.addblock(block)
# print(blockchain.toJson())


# i am going to make pull request again why is this not working







   




# this is the new branch repo
# new brNCH    in github
