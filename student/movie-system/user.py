from movie import Movie
import json



class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self): #represent, so you can format what it looks like when it's printed.
        return "<User: {}>".format(self.name)

    def add_movie(self, name, genre):
        self.movies.append(Movie(name, genre, False))

    def delete_movie(self,name):
        # self.movies.remove(name)
       self.movies=list(filter(lambda movie: movie.name != name, self.movies))

    def change_watched_status(self):
        print(self.movies)
        name=input("Which movie to toggle watched status?")
        for movie in self.movies:
            if name==movie.name:
                movie.watched=not(movie.watched)
        return movie.watched

    def watched_movies(self):
        watched=list(filter(lambda movie: movie.watched, self.movies)) #filtering out and returning a list.
        if len(watched)<1: print("You haven't watched any movies.")
        return watched

    def json(self):
        return{
            'name':self.name,
            'movie':[
                movie.json() for movie in self.movies
            ]
        }

    def save_to_file(self, filename='my_movie.txt',action='w'):
        with open(filename, action) as f:
            json.dump(self.json(), f)
        print("Progress Saved to file {}".format(filename))

    @classmethod
    def load_from_file(cls,filename,action='r'):
        with open(filename, 'r') as f:
            json_data = json.load(f)
            user = User.from_json(json_data)
            print(user)
            #user=User(json_data['name'])
        return user


    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        ## maybe a for user in json_data['name'] to iterate through names for multiple users
        for movie_data in json_data['movie']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies
        return user
