import png
import qrcode
from PIL import Image

class qrgenerator():
    # Import QRCode from pyqrcode
    @staticmethod
    def blockreducer(block):
        data={}
        # data['lastHash']=block.lasthash
        data['timestamp']=block.timestamp
        data['merkleroot']=block.merkleroot
        jsontransaction =[]
        for transaction in block.transactions:
            trans_dict = transaction
            del trans_dict.signature
            jsontransaction.append(trans_dict.__dict__)
        data['transaction']=jsontransaction
        return data

    @staticmethod
    def generateqr(qrstr):
        data = '{}'.format(qrstr)
        img = qrcode.make(data)
        img.save('MyQRCode1.png')
        img = Image.open("MyQRCode1.png")
        img.show()
              

        
        


  
  

