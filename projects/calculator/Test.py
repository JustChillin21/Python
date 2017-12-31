from timesheet import TimeSheet
from timesheet import MinDailyFee
from show import Show
from datetime import datetime
import time
work=[]
work=Show("Supernatural")
Categories=[]
print(work.name)
#start=timedelta(hours=int(tstart[0]),minutes=int(tstart[1]))##Make a time conversion method
#wrap=timedelta(hours=int(twrap[0]),minutes=int(twrap[1]))
#date=("2/6/2017", "3/6/2017")
date=(datetime.strptime("2017-06-02", '%Y-%m-%d'),datetime.strptime("2017-06-03", '%Y-%m-%d'))
#Input Year Month Date
#date=("2017-06-02","2017-06-03")
#print("total time:{}".format((wrap-start)))
start=("09:00","07:30")#.split(':')
crew_call=("08:00","8:30")
wrap=("26:00","19:36")#.split(':')
ndb=("y",'n')#.split(':')
lunch1_start=("14:00","15:00")#.split(':')
lunch1_end=("14:30","16:00")#.split(':')
lunch2_start=("0:00","0:00")#.split(':')
lunch2_end=("0:00","0:00")#.split(':')
work.add_workdate(date[0],start[0], crew_call[0],wrap[0], ndb[0], lunch1_start[0], lunch1_end[0], lunch2_start[0], lunch2_end[0])
#work.timesheets[0].append(work.timesheets[0].calctime)
#work.append(Show('iZombie'))
work.add_workdate(date[1],start[1], crew_call[1],wrap[1], ndb[1], lunch1_start[1], lunch1_end[1], lunch2_start[1], lunch2_end[1])
#work.timesheets[0].calctime
#work.timesheets[0].total_time()
#Work[0].add_date(start)
#print(work[0].start)
#print(work.timesheets[0].calctime, work.timesheets[0].start)
#print(work.timesheets[0].convert_time())
#print(work.timesheets[0].all)
#print(work.timesheets[0].wrap)
#work.timesheets[0].repl_date(work.timesheets[0].all)
print(work.timesheets[0].calctime,work.timesheets[0].totaltime)
print(work.timesheets[1].calctime,work.timesheets[1].totaltime)

#print(work.timesheets[0].json())
#print(work.timesheets)#Work[0].display_details()
#for wdate in work.timesheet:
#    print(work.timesheet[wdate])

work.save_to_file('timesheet.txt')
#Categories.append(MinDailyFee("2017","General Background Performer",190.83,23.85))
#print(Categories[0].year)
#print("{} {}".format(Categories[0].category,Work[0].calculate_wage(Categories[0].hourlyrate)))
#print(Work)
#print(Work[0].convert_time())
#Work[0].calculate_wage(24.51)
#print(Work.total_time())
