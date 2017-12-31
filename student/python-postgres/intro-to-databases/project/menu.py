from user import User

class Menu:
    @staticmethod
    def create(): ##Find a way to have it select how many table names there are....
        first_name = input("Please enter first name: ")
        last_name = input("Please enter last name: ")
        email = input("Please enter email address: ")
        save_details = input('Would you like to save this user? ([Y]/N): ')
        if save_details.upper() != 'N':
            try:
                User.load_from_db_by_email(email)
                print("User {} already exists.".format(email.upper()))
            except TypeError:
                new_user = User(email, first_name, last_name)
                new_user.save_to_db()
                print(User.load_from_db_by_email(email))
        else:
            print('Record not saved.')

    @staticmethod
    def search():
        email = input("Please enter email address to search for: ").lower()
        try:
            print(User.load_from_db_by_email(email))
        except TypeError:
            print("{} Does not have and existing record.".format(email.upper()))

    @staticmethod
    def modify():
        email = input("Please enter email for record to modify: ").lower()
        try:
            modify = input(
                '[{}]\n Is this the record you want to modify? ([Y]/N): '.format(User.load_from_db_by_email(email)))
            if modify.upper() != 'N':
               print("Modifying Record")
               User.modify_record_in_db(email)
            else:
                print("Nothing Changing")
        except TypeError:
            print("{} Does not have and existing record.".format(email.upper()))
        pass

    @staticmethod
    def delete():
        email=input("Please enter email for record to delete: ").lower()
        try:
            print()
            delete = input('[{}]\n Is this the record you want to delete? ([Y]/N): '.format(User.load_from_db_by_email(email)))
            if delete.upper() != 'N':
                print("Deleting... {}".format(email))
                User.delete_from_db(email)
            else:
                print("Skipping Delete")
        except TypeError:
            print("{} Does not have and existing record.".format(email.upper()))

    @staticmethod
    def print():
        User.print_all_from_db()

    def select():
        print('\n[C]reate New Record\n'
              '[S]earch for Existing Record\n'
              '[M]odify Existing Record\n'
              '[D]elete Existing Record\n'
              '[P]rint All Records\n'
              '[Q]uit\n')
        selection = (input('Please enter Selection: ')).upper()
        return selection

