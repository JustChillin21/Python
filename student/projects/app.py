student_list=[]

def create_student(stud_num):
    name = input("Please enter the new student's name: ")
    student_data=[]
    return {"student_number":stud_num,"name": name,"marks":student_data,"avg_mark":student_data}

def add_mark(student, mark=0):
    #append a mark to the student dictionary
    if mark==0:
        another=True
        while another:
            mark=int(input("Please enter mark for {}: ".format(student['name'])))
            if mark<=100:
                student['marks'].append(mark)
            else:
                mark = int(input("Invalid Entry. Please enter mark between 0 and 100 for {}: ".format(student['name'])))
            choice=input("Would you like to add another mark for {}:".format(student['name']))
            if choice.upper()=='N':
                print("{}'s marks have been updated.".format(student['name']))
                another=False

def calculate_average_mark(student):
    if len(student['marks'])>0:
        student['avg_mark']=(sum(student['marks'])/len(student['marks']))
    else:
        student['avg_mark']=0
    return student['avg_mark']

def print_student_details(students):
    #print out a string that tells the user important information about this student
    print("\nStudent Name\tAverage Mark")
    for i, student in enumerate(students):
        print('{}\t\t\t{}'.format(student['name'], int(calculate_average_mark(student))))

def display_stud(students, item):
    for i, student in enumerate(students):
        print("{}: {}".format(i, student[item]))

def print_student_list(students):
    for student in students:
        print(print_student_details(student))

def menu():
    x=0
    choice=True
    while choice:
        option = input("Please enter an Option \n(1)Add a student\n(2)Add a mark\n(3)Print a Student List\n(4)Exit\n>")
        if option=='1':
            print("Add Student Record")
            student_list.append(create_student(x))
            print("{} was added.".format(student_list[x]['name']))
            x=+1
        elif option=='2':
            print("Add Marks to Student Record")
            stud_num = int(input("Which student to add marks to?:".format(display_stud(student_list, 'name'))))
            add_mark(student_list[stud_num])
        elif option=='3':
            print("List all Students")
            print_student_details(student_list)
        else:
            choice=False
            print("Goodbye")
            break

menu()
#student = create_student()
#add_mark(student,70) #(Passing by reference (dictionary), pass by value(numbers)
#add_mark(student,80)
#average=calculate_average_mark(student)
##print("{} Average Mark: {}".format(student['name'], calculate_average_mark(student)))
#print_student_details(student)
#print_students(student_list)

