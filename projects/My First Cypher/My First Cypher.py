import string
import random

def createCypher():
    cypher_letters='vhjgscoeliytxzqrdpbufwmkan'
    #punctuation_cypher- save cypher for punctuation in an array to recall later
    #change cypher so that the order item changes, but is also saved in an array (0,1,2,3)
    #random punctuation allotment.
    punc=''.join(random.sample(string.punctuation+string.whitespace,len(string.punctuation+string.whitespace)))
    numbers=str(string.digits)
    cypher=list(punc+cypher_letters+cypher_letters.upper()+numbers)
    return cypher
    
def encryption(incoming,times=1):
    #print(cypher)
    encrypted=[]
    #for i in range(0,len(incoming)):
    for i in incoming:
        encrypted.insert(i,cypher[original.index(incoming[i])])
        #print(cypher[original.index(incoming[i])])
        completed="".join(encrypted)
    return completed

def decryption(scrambled,times=1):
    decrypted=[]
    for i in range(0,len(scrambled)):
        decrypted.insert(i,original[cypher.index(scrambled[i])])
        #print(cypher[original.index(incoming[i])])
        completed="".join(decrypted)
    return completed

       
original=list(string.printable)
#print(original)
encrypttext=input("What would you like to encrypt? ")
toencrypt=list(encrypttext)
encrypted=[]
cypher=createCypher()

work=encryption(toencrypt,2)
print(work)
#Would you like to decrypt option
print(decryption(work))




#store the number in a list
#replace the new character with the corresponding number
#print encrypted message
#add multiple encryption/decryption
