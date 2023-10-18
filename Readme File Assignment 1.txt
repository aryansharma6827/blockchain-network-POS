Group No. 14-
1.Aryan Sharma(2021A4PS2551H)
2.Abhishek Kochar(2021A4PS2495H) 
3.Kushagra Patni(2021A3PS2985H)
4.Harshwardhan Bhardwaj(2021A8PS3000H)
Consensus Algorithm Assigned-Proof of Stake
notes:-
The manufacturer must always transfer the product to the distributor before the distributor makes a transaaction to the client 
Transaction pool must contain atleast 2 transactions before mining the block
genesis block is already been decleared so the first transaction gets added to the first block


The description of the code is as follows-
Feature 1-To register new clients, distributors and a manufacturer (only one) to the system,
with the client and distributor depositing a security amount to a trusted third party.
Implemented through the account and acc class (The manufacturer has already been added by us)

Functions-
1.adddistaccount-To add the distributor
2.addclientaccount-To add the client
3.stake_provider-To input the stake of the required party
Feature 2-POS algorithm
Implemented through the blockmining class
Functions-
1.stake_verifyer-Determines the block miner


Feature 3-Merkle Tree
Implemented through the block class
Functions-
1.build_merkle_tree and merk-Generates and then returns the merkle root of all transactions.
Feature 4-QR CODE
Implemented through the QRGENERATOR class
 Functions-
1. Generator-generates the QR using the png and qrcode libraries
The corresponding QR is displayed in the MYQRCODE1.png file,this QR gives the information about the last added block to the blockchain. The QR can be scanned to check the mentioned feature.
Feature 5- Once the transaction is confirmed by both the distributor and the consumer, then only the next delivery can be taken by him/her.
Implemented in the account class and mentioned with a comment  Implementation of 5th feature 
Feature 6-To resolve the mentioned issue and make deductions accordingly 
Implemented in the main class using if else statement commented as the "Implementation of the sixth feature" 




















