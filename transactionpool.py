

class Transactionpool():
    def __init__(self):
        self.transactions=[]
    def addtransaction(self,transaction):
        self.transactions.append(transaction)
        # check if it already exist
    def transactionexist(self,transaction):
        for pooltran in self.transactions:
            if pooltran.equals(transaction):
                return True
            
        return False
    def prin(self):
        print(self.transactions)
        print(self.transactions[1].amount)
        