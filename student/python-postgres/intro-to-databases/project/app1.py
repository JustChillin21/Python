from user import User
from database import Database
#my_user = User("blaforge@email.com","Bill","LaForge",None)
#my_user.save_to_db()

print(Database.__connection_pool)
Database.initialize()
print(Database.__connection_pool)

