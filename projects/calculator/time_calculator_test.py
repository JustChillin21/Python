import datetime
import math

def setup(start=('8:00'), end=(23,12), dlunch1=(int('00'),30)): #Pass Default Vaules for Test
    #start=(8,00)
    start1=[int(time) for time in start.split(":")]
    end=(23,12)
    dlunch1=(int('00'),30)
    slunch1=(14,int('00'))
    elunch1=(14,30)
    Time_Card=timeCard(start1, end, dlunch1, slunch1, elunch1)
    return Time_Card

def main():
    start=start_time() #Ideally digital clock to choose time. Limit out of range.
    end=wrap_time()
    dlunch1=lunch_calc()
    disp_results(timeCard(start, end, dlunch1))

def timeCard(start, end, dlunch1=0, slunch1=0, elunch1=0, dlunch2=0, slunch2=0, elunch2=0, ndb=0):
    return {"Start":start,"End":end,"Dur_Lunch1":dlunch1,"START_Lunch1":slunch1,"END_Lunch1":elunch1,"Dur_Lunch2":dlunch2,"START_Lunch2":slunch2,"END_Lunch2":elunch2}

def test(start=('8:00'), end=(23,12), dlunch1=(1,00)):#Allow Sample values for test
    Time_Card=setup(start,end,dlunch1)
    disp_results(Time_Card)

def timeworked(timecard):
    hours_worked=list((timecard['End'][0]-timecard['Dur_Lunch1'][0]-timecard['Start'][0],timecard['End'][1]-timecard['Dur_Lunch1'][1]-timecard['Start'][1]))
    hours=int(hours_worked[0])
    minutes=int(hours_worked[1])
    if hours_worked[1]<0:hours_worked=(hours-1,60+minutes)
    return hours_worked

def disp_results(timeCard):
    print("Start: {}".format(timeCard['Start']))
    print("End: {}".format(timeCard['End']))
    print("Lunch Period from {}".format(timeCard['Dur_Lunch1']))
    print("Hours Worked: {}".format(timeworked(timeCard)))
    print("Payed Time: {}".format(converttime(timeworked(timeCard))))
    
def roundtime(x,base=6): #Rounds time up to the nearest 6 minute interval
    return int(math.ceil(x / base)) *base

def converttime(x): #Fraction of hour for pay calculation
    return x[0]+roundtime(x[1])/60

def changetime(x):
    return datetime.timedelta(hours=x[0],minutes=x[1])

def checktime(tocheck):
    if len(tocheck)<2 : tocheck.append(int("00"))
    while (tocheck[1]>59):
        tocheck=[int(time) for time in input("Please Enter a Valid time [00:00]: ").split(":")]
    if (tocheck[1]%6)>0:tocheck[1]=roundtime(tocheck[1])
    if (tocheck[1]>=60):
        tocheck[0]+=1
        tocheck[1]=int("00")
    return tocheck
        
def start_time():
    start=[int(time) for time in input("What time did you start: ").split(":")]
    #start=datetime.timedelta(hours=start_temp[0],minutes=start_temp[1])#Trying to keep it in the time
    return checktime(start)
    #return start

def wrap_time():
    end=[int(time) for time in input("What time was wrap: ").split(":")]
    return checktime(end)

## for Meal Penalty Calculation
def ndb_calc():
	if (input("Was there an NDB (non deductable breakfast): ").upper()=="Y"):
	    ndb_time=[int(time) for time in input("What time was NDB: ").split(":")]
	return ndb_time

def lunch_start():
    #lunch Start
    lunch_start=[int(time) for time in input("What time did lunch start: ").split(":")]
    if len(lunch_start)<2 : lunch_start.append(int("00"))
    return lunch_start
    
def lunch_end(start):
    #lunch End
    lunch_end=[int(time) for time in input("What time did lunch end: ").split(":")]
    if len(lunch_end)<2 : lunch_end.append(int("00"))
    if lunch_end<start:lunch_end=[int(time) for time in input("Please enter a time after the start [{}:{}]: ".format(start[0],start[1])).split(":")]
    return lunch_end
    
def lunch_calc():
        lunch_min=30
        if (input("Was there lunch: ").upper()=="Y"): #figure out french hours#
            start=lunch_start()
            ##lunch End
            end=lunch_end(start)
            #lunch Duration
            lunch=(end[0]-start[0],end[1]-start[1])
            if lunch[1]<30:  #If Lunchbreak is less tha 30 Mins set to minimum of 30
                if lunch[0]==0:
                    print("Minimum {} minute lunch".format(lunch_min))
                    lunch=(0,lunch_min)
        else:
            lunch=(0,0)
        return lunch  #maybe return in a dictionary

#mealpenalty(start/lunch1_end, lunch1_start/wrap)
#   if ndb then lunch_start - ndb
#   if lunch_start-nsb (or start) >6.5
#   if wrap-lunch1_end or wrap-lunch2_end >6.5

##def total_day(day):
##    #if(day["START_Lunch2"]>0) and (day["START_Lunch1"]>0):
##    total_time=day["End"]
##    #total_time=(day["End"]-day["END_Lunch2"])+(day['START_Lunch2']-day["END_Lunch1"])+(day["START_Lunch1"]-day["Start"])
##    #else:
##    #total_time=int(day["End"]-day["END_Lunch2"])+(day['START_Lunch2']-day["END_Lunch1"])+(day["START_Lunch1"]-day["Start"])
##    #total_time=datetime.timedelta(day["End"]-day["END_Lunch2"])
##    print('Falls within category {}'.format(total_time))
##    return total_time

    
