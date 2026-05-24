# name = "clement"
# #name = input('please enter you name\n')
# if name == "clement":
#     print('No')
    
# else:
#     print(f"Hello,{name}")

# import calendar
# year = int(input("Enter Year: "))
# print(calendar.calendar(year, 1, 2, 5, 4))
from logging import exception


def validate_input(value):
    try:
        value = float(value)
        return value
    except exception as e:
        print(e)
        
fahranite = 3 #input("Farhanite value: ")
fahranite = validate_input(fahranite)

if fahranite:
    celsius = (fahranite - 32) *5/9
    print(f"Celcious value of {fahranite} Faharanite is celsius {celsius:2f}.")
else:
    print("Enter Valid input")
    

#Python Code Basics: Filter positive numbers from a list  
# Suppose you are getting a list of positive and negative numbers. 
# We can use : numbers = [-10, 4, 6, 8, -12] also for sample # But here we use, 
# random module to generate a list of # 10 random numbers between -8 to 8 
import random 
numbers = [random.randint(-8, 8) for i in range(10)] 
print(f"Numbers: {numbers}") 

#The famous FizzBuzz Problem With 3 different Methods.,
'''What is fizzbuzz Problem??
For a number 'n', display the string representations of all the numbers from 1 to n, where: - If the number is divisible by 3, the
output is 'Fizz'. If the number is divisible by 5, the output is 'Buzz'. - If the number is divisible by both 3 and 5, the output is 
'FizzBuzz'. - And display the number if the number cannot be divided by 3 or 5. '''
# • Method-1: Using normal function 
def fizzbuzz(n): 
    for number in range(1, 9): 
        if (number % 3 == 0) and (number % 5 == 0): 
            print("FizzBuzz", end='') 
        elif (number % 3 == 0): 
            print("Fizz", end='') 
        elif (number % 5 == 0): 
            print("Buzz", end='') 
        else: 
            print(number, end='') 
print(fizzbuzz(101)) 
# ■ Using Lambda Function 
print(list(map(lambda i: 'Fizz'*(not i % 3)+'Buzz' * (not i % 5) or i, range(1, 9))), sep='') 
# Using List-Comprehension 
print(['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 9)]) 


# import getpass
# database = {"dee": "45", "pyth": "245"}
# username = input("Enter username: ")
# password = getpass.getpass("Enter Your Password : ")
# for i in database.keys():
#     if username == i :
#         while password != database.get(i):
#             password = getpass.getpass("Enter Password Again! :")
#         break
# print("Verified")
#EquiEnum.labs


import random 
choices = ["rock", "paper", "scissors"]

while True:
    user_input = 'quit' #input ("Choose rock paper  or scissors (or 'quit' to stop):").lower()
    if user_input == 'quit':
        print("Thanks for playing")
        break
    if user_input not in choices:
        print("Invalid choice, please try again.")
        continue
    computer_input = random.choice(choices)
    print(f"computer chose{computer_input}")
    if user_input == computer_input:
        print("its a tie")
    elif(user_input == "rock" and computer_input == "scissors") or \
        (user_input == "paper" and computer_input == "rock") or \
        (user_input == "scissors" and computer_input == "paper"):
        print("You win!")
    else:
        print("You lose!")



