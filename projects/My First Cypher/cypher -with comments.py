import string
import random

def encryption(incoming):
    encrypted=[]
    cypher_letters='vhjgscoeliytxzqrdpbufwmkan'
#Randomize Punctuation : ''.join(random.sample(string.punctuation,len(string.punctuation)))
    #punc='+)<&"\',/-\\.[>%`{(;]^?=:!}~$*|@_#,' #Change so it's a random character using the above
    #random punctuation allotment.
    punc=''.join(random.sample(string.punctuation+string.whitespace,len(string.punctuation+string.whitespace)))
    cypher=list(cypher_letters+cypher_letters.upper()+punc)
    
    for i in range(0,len(incoming)):
   #toencrypt[i] in cypher
       #encrypted[i]=cypher[original.index(incoming[i])]
       print(cypher[original.index(incoming[i])])
       #print(encrypted)

cypher_letters='vhjgscoeliytxzqrdpbufwmkan'
#Randomize Punctuation : ''.join(random.sample(string.punctuation,len(string.punctuation)))
##punc='+)<&"\',/-\\.[>%`{(;]^?=:!}~$*|@_#,' #Change so it's a random character using the above
##punc=''.join(random.sample(string.punctuation,len(string.punctuation)))
#original=list(enumerate(string.ascii_letters))
original=list(string.ascii_letters+string.punctuation+string.whitespace)
#cypher=list(enumerate(cypher_letters+cypher_letters.upper()))original=list(enumerate(string.ascii_letters))
##cypher=list(cypher_letters+cypher_letters.upper()+punc)
print(original)
#print(cypher)
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
