from timesheet import TimeSheet
from show import Show
from timesheet import MinDailyFee
import json

#work=User.load_from_file("timesheet1.txt")
with open('timesheet.txt','r') as f:
    json_data = json.load(f)
    #show=Show.from_json(json_data)
    print(Show.from_json(json_data))
    #print(show.json())
#print(show.timesheets)
#print(show.timesheets[0].totaltime)
