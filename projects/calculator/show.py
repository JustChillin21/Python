import json

from timesheet import TimeSheet
import time

class Show:
    def __init__(self, name):
        self.name = name
        self.timesheets = []

    def __repr__(self): #represent, so you can format what it looks like when it's printed.
         return "<User: {}, {}>".format(self.name,self.timesheets)

   

    def add_workdate(self, date, swork, ccall, wend, ndb, slunch1, elunch1, slunch2, elunch2):
        self.timesheets.append(TimeSheet(date, swork, ccall, wend, ndb, slunch1, elunch1, slunch2, elunch2))
##Change format

    def json(self):
        return{
            'name':self.name,
            'timesheet':[
                timesheet.json() for timesheet in self.timesheets
            ]
        }

    def save_to_file(self,name='timesheet.txt'):
        # create a new file with name and movies
        with open(name, 'w') as f:
            json.dump(self.json(),f)
                
    @classmethod  # runs method on the userclass
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            print("Loading from : {}".format(filename))
            content = f.readlines()
            username = content[0]
            timesheets = []
            for line in content[1:]:
                #print(line)
                timesheet_data = line.split(",")  # ['name','genre','watched']
                #print(timesheet_data)
                timesheets.append(TimeSheet(timesheet_data[0],timesheet_data[1],timesheet_data[2], timesheet_data[3], timesheet_data[4],timesheet_data[5], timesheet_data[6], timesheet_data[7],timesheet_data[8]))
                #print(timesheets)
            work = cls(username)
            work.timesheets = timesheets
            return work

    @classmethod
    def from_json(cls, json_data):
        #print(json_data['name'])
        show=Show(json_data['name'])
        timesheets=[]
        for timesheet in json_data['timesheet']:
            #print(timesheet)
            timesheets.append(TimeSheet.from_json(timesheet))
        show.timesheets=timesheets
        return show

  ####Shoule be workable Method
    # show=Show(json_data['name'])
    # timesheets=[]
    # for timesheet in json_data['timesheet']:
    #     print(timesheet)
    #     timesheets.append(TimeSheet.from_json(timesheet))
    #     print(timesheet['Total_Time'])
    # show.timesheets = timesheets
    ####Shoule be workable Method