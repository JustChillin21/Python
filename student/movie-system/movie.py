class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "\tMovie: {:15} \t Genre: {:10} \t Watched:{:6}\n".format(self.name, self.genre, self.watched)


    def json(self):
        return {
            'name':self.name,
            'genre':self.genre,
            'watched':self.watched
        }

    @classmethod
    def from_json(cls, json_data):
        #return Movie(name=json_data['name'],genre=json_data['genre'], watched=json_data['watched'])
        return Movie(**json_data)#Dictionary you are passing as a bunch of named paramaters