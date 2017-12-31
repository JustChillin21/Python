from psycopg2 import pool
import psycopg2 as pq
import getpass as gp
#import psycopg2
#

# minconn=1
# maxconn=10
#control when connection pool gets executed
class Database:
    __connection_pool = None

    @classmethod
    def initialize(cls, **kwargs):
        # choice=input("Would you like to change default database settings? (Y/[N]) ").upper()
        # if choice != "Y":
        #     d_user='y2venom'
        #     d_name='learning'
        #     maxconn=10
        # else:
        #     d_user = input('Which User Would you like to connect to the database?').lower()
        #     d_name = input('Which Database would you like to connect to? ')
        #     # d_password=gp.getpass('Please enter password: ')
        #     maxconn = int(input('How many connections would you like available in the pool? '))

        #cls.__connection_pool = pq.pool.SimpleConnectionPool(minconn, maxconn, user=d_user,
        #                                                     password='jun34u2I', database=d_name,
        #                                                     host='SpiderVault')
        cls.__connection_pool = pq.pool.SimpleConnectionPool(**kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        return cls.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
            Database.return_connection(self.connection)
