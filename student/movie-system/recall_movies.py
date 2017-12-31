from user import User
import json


#with open('my_movie.txt','r') as f:
#     json_data = json.load(f)
#     user=User.from_json(json_data)
user=User.load_from_file('Joe.txt')
print(user.movies)

