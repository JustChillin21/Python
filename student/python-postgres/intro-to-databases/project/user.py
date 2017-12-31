#from database import connection_pool
from database import CursorFromConnectionFromPool


class User:
    def __init__(self,email, first_name,last_name, id=None):
        self.email=email
        self.first_name=first_name
        self.last_name=last_name
        self.id=id


    def __repr__(self):
        return "<User[{}] {} {}: {}>".format(self.id,self.first_name, self.last_name, self.email)

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            query = """INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)"""
            values = (self.email, self.first_name, self.last_name)
            # cursor.execute('INSERT INTO users(email, first_name, last_name) VALUES(%s, %s, %s)',
            #                (self.email, self.first_name, self.last_name))
            cursor.execute(query,values)
            print("Record Saved: {}".format(self.email))

    @classmethod
    def delete_from_db(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            #cursor.execute('DELETE FROM users WHERE email=%s',(email,))
            query = """
            DELETE FROM users WHERE email=%s
            """
            values=(email,)
            cursor.execute(query, values)
            print("Record Deleted: {}".format(email))

    @classmethod
    def view_column_names(cls):##Returns Column Headers from table
        with CursorFromConnectionFromPool() as cursor:
            query = """
            SELECT 
            * 
            FROM 
            users
            LIMIT
            0
            """
            cursor.execute(query,)
            ###
            col_names = []
            for header in cursor.description:
                col_names.append(header[0])
        return "Columns: {} {} {}".format(col_names[1],col_names[2],col_names[3])

    @classmethod #Modify a record in the Database
    def modify_record_in_db(cls, email):
        tmp=cls.load_from_db_by_email(email)
        print('\nModify\n(F)irst Name: {}\n(L)ast Name: {}\n(E)mail Address: {}\n'.format(tmp.first_name,tmp.last_name,tmp.email))
        choice=input('What would you like to modify?').lower()
        if choice=='f':
            newvalue = input('Please enter new First Name for {}: '.format(tmp.first_name))
            record_type="First Name"
            with CursorFromConnectionFromPool() as cursor:
                #cursor.execute('UPDATE users SET first_name=%s WHERE email=%s', (newvalue, email,))
                query = """
                UPDATE users SET first_name=%s WHERE email=%s
                """
                values = (newvalue, email)
                cursor.execute(query, values,)
        if choice=='l':
            newvalue = input('Please enter new Last Name for {}: '.format(tmp.last_name))
            record_type = "Last Name"
            with CursorFromConnectionFromPool() as cursor:
                #cursor.execute('UPDATE users SET last_name=%s WHERE email=%s', (newvalue, email,))
                query = """
                UPDATE users SET last_name=%s WHERE email=%s
                """
                values = (newvalue, email)
                cursor.execute(query, values)
        if choice=='e':
            newvalue = input('Please enter new Email Address for {}: '.format(tmp.email))
            record_type = "Email Address"
            with CursorFromConnectionFromPool() as cursor:
                #cursor.execute('UPDATE users SET email=%s WHERE email=%s', (newvalue, email,))
                query = """
                UPDATE users SET email=%s WHERE email = %s
                """
                values = (newvalue, email)
                cursor.execute(query, values)
        else:
            print("Nothing to Change")
        print('{} has been updated for {}'.format(record_type,email))

    @classmethod
    def print_all_from_db(cls):
        cls.view_column_names()
        with CursorFromConnectionFromPool() as cursor:
            #cursor.execute("SELECT * FROM users ORDER BY id")
            query="""
            SELECT * FROM users ORDER BY id
            """
            #values=(sort)
            cursor.execute(query)#, values)
            rows = cursor.fetchall()

            print('{:4} {:20} {:25}'.format('id','Name','Email'))
            for row in rows:
                id = row[0]
                name = row[2] + ' ' + row[3]
                email = row[1]
                print('[{:2}] {:20} {:20}'.format(id,name,email))


    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            query = """
            SELECT 
              * 
            FROM 
              users 
            WHERE 
              email = %s
            """
            values=(email,)
            #cursor.execute('SELECT * FROM users WHERE email=%s',(email,))
            cursor.execute(query, values)
            user_data = cursor.fetchone()
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3],id=user_data[0])

    # @classmethod
    # def load_from_db_by_id(cls, id):
    #     with CursorFromConnectionFromPool() as cursor:
    #         with cursor.cursor() as cursor:
    #             cursor.execute('SELECT * FROM users WHERE id=%s', (id,))
    #             user_data = cursor.fetchone()
    #             return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])
