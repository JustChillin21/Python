#age = 5 # first lessons with declared age
age = float(input('Enter your Age: '))#Getting the user to input the age - second stage
#Variable Declarations
days = 365
hours = 24
minutes = 60
seconds = 60
#Calculation - Age in seconds)
ageinseconds = age * days * hours * minutes * seconds
#output
print ("If you are {person_age} years old, you have lived for {person_ageinseconds} seconds.".format(person_age=age,person_ageinseconds=int(ageinseconds)))#format converts variables to strings for display

