import random
numbers = 10
max_number=100
min_number=max_number
for attempt in range(numbers):
    new_number=random.randint(0,max_number)
    print("Minimum Number is {min} : New Number is {new}".format(min=min_number,new=new_number))
    if min_number > new_number:
        min_number = new_number
print("The lowest number was {min}".format(min=min_number))
        
