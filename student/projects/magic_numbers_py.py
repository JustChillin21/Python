import random
start_num=0
end_num=9
magic_numbers = [random.randint(start_num,end_num)]

def ask_user_and_check_number():
    user_prompt="Please enter a number between {}-{}: ".format(start_num, end_num)
    user_number = int(input(user_prompt))
    if user_number in magic_numbers:
        return "You guessed right!"
    else:
        return "You got it wrong! Try again"

def run_program_x_times(chances):
    for attempt in range(chances):
        print("This is Attempt: {chance}".format(chance=attempt))
        print(ask_user_and_check_number())
      #  if ask_user_and_check_number=="You guessed right!":
      #      exit
        
user_attempts = int(input("How many chances would you like? "))
run_program_x_times(user_attempts)
print("Game over! The numbers was {}".format(magic_numbers))
