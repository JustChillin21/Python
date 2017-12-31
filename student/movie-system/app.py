from movie import Movie
from user import User
import json

user = User("Bill")
user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The Thing","Horror")
user.add_movie("Constantine","Thriller")
user.save_to_file()
user.change_watched_status()
user.watched_movies()
#user.load_from_file('my_movie.txt')
#user.delete_movie("The Matrix")
#print(user)
#print(user.json())
#print(user.movies)
#user.save_to_file()
#user=User.load_from_file("users.txt")
#print(user.name)
#print(user.movies)
