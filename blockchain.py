from block import Block
from utils import BlockchainUnits
class Blockchain():
    def __init__(self):
        self.blocks=[Block.genesis()]

    def addblock(self,block):
        self.blocks.append(block)
    
    def toJson(self):
        data={}
        jsonBlocks=[]
        for block in self.blocks:
            jsonBlocks.append(block.printb())
        data['blocks']=jsonBlocks
        return data

    def blockcountvalid(self,block):
        if self.blocks[-1].blockcount==block.blockcount-1:
            return True
        else:
         return False
        
    def lastblockvalid(self,block):
         latestblockchainblockhash=BlockchainUnits.hash(self.blocks[-1].payload()).hexdigest()
         if latestblockchainblockhash == block.lasthash:
            return True
         else:
            return False

