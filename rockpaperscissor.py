import random; #importing the random library so that we can use the random function inside this library
choices=['rock','paper','scissor'];#the computer is going to select the choice from the list of the rock paper and scissor
rules ={
     'rock':'scissor',
     'paper': 'rock',
     'scissor':'paper'
}
computer_choice = random.choice(choices)
user_choice=None;#the user choice is set to none so that there is no garbage value
while user_choice  not in ['rock','paper','scissor']:
        user_choice=input('please enter you choice in rock paper and scissoir').lower()

print(f"you choice is {user_choice}")
print(f"computer choice is {computer_choice}")

if(user_choice==computer_choice):
 print("It's a tie")

elif rules[user_choice]==computer_choice:
 print('The user wins')

else:
   print("computer wins")
