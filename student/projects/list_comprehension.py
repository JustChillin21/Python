user_input = input("Please enter your numbers seperated by a comma: ")
user_numbers= user_input.split(',')
numbers_as_int=[int(number) for number in user_numbers]
print(numbers_as_int)
