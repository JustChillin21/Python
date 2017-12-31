from datetime import datetime
from datetime import timedelta
import time
import math


class TimeSheet:
    def __init__(self, date, start, crewcall, wrap, ndb, lunch1start, lunch1end, lunch2start, lunch2end,totaltime=0,calctime=0):
        self.date = date#.strftime('%Y-%m-%d')
        self.category = "Category"  # Category needs to be a class
        self.start = self.check_type(start)
        self.crewcall= self.check_type(crewcall)
        self.wrap = self.check_type(wrap)
        self.lunch1start = self.check_type(lunch1start)
        self.lunch1end = self.check_type(lunch1end)
        self.lunch2start = self.check_type(lunch2start)
        self.lunch2end = self.check_type(lunch2end)
        self.lunch1end = self.check_type(lunch1end)
        self.lunch2start = self.check_type(lunch2start)
        self.lunch2end = self.check_type(lunch2end)
        self.ndb = ndb.upper()
        self.totaltime=self.total_time()
        self.calctime = self.convert_time()
        self.all=(self.start,self.crewcall,self.wrap,self.lunch1start,self.lunch1end,self.lunch2start,self.lunch2end)


    def total_time(self,show=0):
         #if totaltime==0:
            if self.ndb == 'Y':
                if show!=0 : print("Total Work Time with NDB for {}".format(self.date))
                totaltime=(self.lunch1start - self.crewcall) + (self.lunch2start - self.lunch1end) + (self.wrap - self.lunch2end)
                return totaltime
            else:
                if show != 0: print("Total Work Time without NDB")
                totaltime=(self.lunch1start - self.start) + (self.lunch2start - self.lunch1end) + (self.wrap - self.lunch2end)
                return totaltime
         #else:
         #    return totaltime

    def repl_date(self, item,add_days=0,show=0):
        new_item = item.replace(year=self.date.year, month=self.date.month, day=self.date.day)
        self.item = new_item+timedelta(days=add_days)
        if show!=0: print("Old: {} ==> New: {} ==> Self: {}".format(item, new_item, self.item ))
        return self.item

    def check_time(self, time='24:00',show=0):
        #print(type(time))
        #print(time)
        if type(time) is datetime:
            #print("We are in Checktime "+datetime.date(time, '%Y-%m-%d %H:%M'))
            return time
        else:
            #print("We are in the Else statement of checktime".format(time))
            stime=time.split(':')
            wtime=time
            ntime=int(stime[0])
            if ntime>23:
                ntime-=24
                add_days = 1
                stime=str(ntime)+":"+str(self.roundtime(int(stime[1])))
                if len(stime)<5: stime="0"+stime
                wtime=stime
                if show!=0: print(wtime)
                #print("Change time span: {}".format(wtime))
                item=self.repl_date((datetime.strptime(wtime,'%H:%M')),add_days)###FINISH THIS LINE
            else:
                #print("No Change: {} Type: {}".format(wtime, type(wtime)))
                item=self.repl_date(datetime.strptime(wtime,'%H:%M'))###FINISH THIS LINE
            if show != 0: print('Check Time results: {} becomes {}'.format(time,item))
            return item

    def check_type(self,item,show=0):
        if type(item) is not datetime.date:
            self.item = self.check_time(item)
            if show!=0: print ("Have to Convert {}".format(item))
        else:
            self.item = item
        return self.item

    def meal_penalty(self):
        print("Meal Penalty Calculation")

    def __repr__(self):
        return("\nCall Time:{}\tNDB:{}\t\tEnd:{}\n"
               "Lunch 1 Start:{}\tLunch 1 End:{}\n"
               "Lunch 2 Start:{}\tLunch 2 End:{}\n"
               "Calculated_Time={}\tTotal Time:{}\n".format(self.start, self.ndb, self.wrap, self.lunch1start, self.lunch1end, self.lunch2start, self.lunch2end,self.calctime,self.totaltime))

    def roundtime(self, x, base=6):  # Rounds time up to the nearest 6 minute interval
        #print("Round Time to Nearest {}th".format(base))
        return int(math.ceil(x / base)) * base

    def convert_time(self):
        #if calctime==0:
            return (self.totaltime.seconds / 60) / 60
        #else:
        #    return calctime
        # print("Temp time:{}".format(float(temp_time)*22.51))

    def calculate_wage(self, rate):
        # change rate to category later
        return float(self.convert_time()) * rate
        # print("Day Rate: {}".format(day_wage))

    def json(self):
        return{
            'Date':self.date.strftime('%Y-%m-%d'),
            'Call_Time':self.start.strftime('%Y-%m-%d %H:%M'),
            'Crew_Call': self.crewcall.strftime('%Y-%m-%d %H:%M'),
            'NDB':self.ndb,
            'Wrap_Time':self.wrap.strftime('%Y-%m-%d %H:%M'),
            'Lunch1_Start':self.lunch1start.strftime('%Y-%m-%d %H:%M'),
            'Lunch1_End':self.lunch1end.strftime('%Y-%m-%d %H:%M'),
            'Lunch2_Start':self.lunch2start.strftime('%Y-%m-%d %H:%M'),
            'Lunch2_End':self.lunch2end.strftime('%Y-%m-%d %H:%M'),
            'Total_Time':str(self.totaltime),
            'Calculated_Time':self.calctime
        }


    @classmethod
    def from_json(cls,json_data):
        return TimeSheet(datetime.strptime(json_data['Date'],'%Y-%m-%d'),
                         datetime.strptime(json_data['Call_Time'],'%Y-%m-%d %H:%M'),
                         datetime.strptime(json_data['Crew_Call'],'%Y-%m-%d %H:%M'),
                         datetime.strptime(json_data['Wrap_Time'],'%Y-%m-%d %H:%M'),
                        json_data['NDB'],
                        datetime.strptime(json_data['Lunch1_Start'],'%Y-%m-%d %H:%M'),
                        datetime.strptime(json_data['Lunch1_End'],'%Y-%m-%d %H:%M'),
                        datetime.strptime(json_data['Lunch2_Start'],'%Y-%m-%d %H:%M'),
                        datetime.strptime(json_data['Lunch2_End'],'%Y-%m-%d %H:%M'),
                        datetime.strptime(json_data['Total_Time'],'%H:%M:%S'),
                        json_data['Calculated_Time'])
        #return TimeSheet(**json_data)  # Need to figure out how to format once taking out of file


class ShowInfo:  # Details of Production
    def __init__(self, name, casting, ccontact, contract, poffice, urep):
        # include show info (Production Office #, Union Rep and #, Type (Film, TV, Commercial), Casting
        self.Name = name  # Show Name
        # Sign Name
        self.Casting = casting
        self.Contract = contract
        self.Casting_Contact = ccontact
        self.POffice = poffice  # ("Address", "Number")
        self.Urep = urep  # ("Name", "Number")
        # self.Type


class MinDailyFee:
    def __init__(self, year, category, dailyfee, hourlyrate):
        self.year = year
        self.category = category
        self.dailyfee = dailyfee
        self.hourlyrate = hourlyrate
        self.overtimeratex15 = self.hourlyrate * 1.5
        self.overtimeratex2 = self.hourlyrate * 2



