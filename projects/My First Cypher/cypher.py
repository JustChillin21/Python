import string
import random

def encryption(incoming):
    cypher_letters='vhjgscoeliytxzqrdpbufwmkan'
   #random punctuation allotment.
    punc=''.join(random.sample(string.punctuation+string.whitespace,len(string.punctuation+string.whitespace)))
    numbers=str(string.digits)
    cypher=list(numbers+cypher_letters+cypher_letters.upper()+punc)
    print(cypher)
    for i in range(0,len(incoming)):
        encrypted.insert(i,cypher[original.index(incoming[i])])
        #print(cypher[original.index(incoming[i])])
    completed="".join(encrypted)
    print(completed)
       
original=list(string.printable)
encrypted=[]
print(original)
encrypttext=input("What would you like to encrypt? ")
toencrypt=list(encrypttext)
encryptlength=len(toencrypt)
print(toencrypt)
print(encryptlength)

#scan through and get the number for each character in original
encryption(toencrypt)



#store the number in a list
#replace the new character with the corresponding number
#print encrypted message
