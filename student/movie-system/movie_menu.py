#Load
#Save
#Add
#Delete
#Print
#Show Watched
#Exit
import json
import os
from user import User


def menu():
    name=getUserName()
    user=checkFileStatus(name)
    filename=user.name+".txt"
    use_menu=True
    while use_menu:
        user_input=input("Please select an option:"
              "\n\t(a)Add a movie"
              "\n\t(s)See List of movies"
              "\n\t\t(w)Toggle Watched Status"
              "\n\t\t(d)Delete a movie"
              "\n\t(l)See list of watched movie"
              "\n\t(q)Quit"
              "\n\tSelection:".format(user.name)
              ).upper()
        if user_input== 'A':
            add_more=True
            while add_more:#Could do one question seperating by colon#
                user.add_movie(input("Please enter movie name: "),input("Please enter movie genre: "))
                if (input("Would you like to add another movie?: ").upper())!="Y":
                    add_more=False
            user.save_to_file(filename)
        elif user_input=='S':
            for movie in user.movies:
                #print("Name: {:15} Genre: {:10} Watched: {:5}".format(movie.name, movie.genre, movie.watched))
                print_movies(movie)
            user.save_to_file(filename)
        elif user_input == 'W':
            user.change_watched_status()
            user.save_to_file(filename)
        elif user_input == 'D':
            user.delete_movie(input("What movie would you like to delete? {}".format(user.movies)))
        elif user_input == 'L':
            print(user.watched_movies())
        elif user_input == 'Q':
            use_menu=False
            #user.save_to_file(user.name+".txt")
            print ("\nThank you for using the Movie Library. Goodbye.")
            return 0
        else:
            print("Please try a valid option")
    #ask for the users name
    #check if a file exists fot that user
    #if it exists, load the data
    #if not, create a user object

    #give a list of options
    #Add a movie
    #@See list of movies
        #Set a movie as watched
        #Delete a movie by name
    #See list of watched movies
    #Save and Exit

def getUserName():
    return input("Please enter your name: ")

def checkFileStatus(name):
    print("Please wait while we look up your account".format(name))
    filename="{}.txt".format(name)
    if file_exists(filename):
        print("Welcome Back {}.".format(name))
        return load_file(filename)
    else:
        print("Welcome {}, Please wait while we create your account.".format(name))
        return create_User(name)

def file_exists(filename):
    return os.path.isfile(filename)

def create_User(name):
    print("No file exists for {}. Creating a new file.".format(name))
    user = User(name)
    return user

def load_file(filename):
    with open(filename, 'r') as f: json_data = json.load(f)
    return User.from_json(json_data)
    #return user

def print_movies(movie):
    print("Name: {:15} Genre: {:10} Watched: {:5}".format(movie.name, movie.genre, movie.watched))

menu()
