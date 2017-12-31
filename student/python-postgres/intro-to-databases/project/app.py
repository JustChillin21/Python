#from user import User
from menu import Menu
from database import Database

Database.initialize(minconn=1, maxconn=10,user='y2venom', password='jun34u2I', database='learning', host='SpiderVault')

print('Welcome to the records entry system\nPlease select from the following options:')

choice=True
while choice:
    action=Menu.select()
    if action=='C':
        Menu.create()
    elif action=='S':
        Menu.search()
    elif action=='M':
        Menu.modify()
    elif action=='D':
        Menu.delete()
    elif action=='P':
        Menu.print()
    else:
        choice=False
        print('Thank You')
