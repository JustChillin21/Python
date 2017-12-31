"""
This program is from Udemy Learning Python - Not the snake Course where you take
some variables from the user and after some calculations return their age.
variables - first_name - string
            first_num - int,
            second_num - int
            num1 = storage for first set of calculations
            num2 = storage for second set of calculations
"""
print "Hello, what is your first name?"
first_name = str(raw_input(">>"))
print "So %s, I will now guess your age!!" % first_name
print"But I need to ask some questions:"
print"What is the first number of your age?"
first_num=int(raw_input(">>"))
num1=first_num*5
print"Okay, %s, I will multiply that by 5 = %s" % (str(first_name),str(num1))
num1=num1+3
print"Next, I will add 3 to the number = %s" % str(num1)
num1=num1*2
print"Next, I will double the number = %s" % str(num1)
print"Now I will need the second number of your age!!"
second_num=int(raw_input(">>"))
num1=num1+second_num
num2=num1
print"Thanks! I will add that number to our running total%s + %s = %s" % (str(num1),str(second_num),str(num2))
num1=num1-6
print"Ant the last thing I will do is subtract 6 [%s - 6] = %s"% (str(num2),str(num1))
print"Wow!!!, So Jay your AGE is = %s" % str(num1)
