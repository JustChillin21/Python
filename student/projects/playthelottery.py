# User can pick 6 numbers
#lottery calculates 6 random numbers between 1 and 20
#Then we match the user numbers to the lottery numbers
#Calculate the winnings based on how many numbers the user matched
import random
import math

def nCr(n,r):
    f = math.factorial
    probab = f(n) / f(r) / f(n-r)
    print(probab)
    return probab

def winnings(matching):
    amount=(5.2*nCr(max_lotto,matching))
    return amount
                           
def menu():
    print("Welcome to the Lotto 6/{}".format(max_lotto))
    #Ask Player for number
    user_num=get_player_numbers()
    #Calculate lottery numbers
    lottery_num=create_lottery_numbers()
    #print out the winnings
   print("You've won ${}".format(winnings(len(check_winning_numbers(user_num,lottery_num)))))

    
def get_player_numbers():
    number_csv = input("Enter your 6 numbers, seperated by commas: ")
    number_list=number_csv.split(',')
    
    player_number=set([int(number) for number in number_list])
    
    # Now, I want to create a set of integers from this number_csv
    #while number in player_number:
    print(len(player_number))
    if len(player_number)<6:
        print("You only chose {} unique numbers. We will add {} random ones for you".format(len(player_number),6-len(player_number)))
        while len(player_number)<6:
            player_number.add(random.randint(1,max_lotto))
    print(player_number)
    return player_number
    
def create_lottery_numbers():
    lottery_numbers=set()
    while len(lottery_numbers)<6:
        lottery_numbers.add(random.randint(1,max_lotto))
    print(lottery_numbers)
    return lottery_numbers

def check_winning_numbers(user_num, winning_num):
    match=user_num.intersection(winning_num)
    print("You've matched {} numbers. {}".format(len(match), match))
    return match

max_lotto=20   
menu()
