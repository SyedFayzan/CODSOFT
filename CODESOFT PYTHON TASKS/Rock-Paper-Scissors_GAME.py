#import random module 
import random

#function to get the winner
def winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'scissors' and comp_choice == 'paper') or (user_choice == 'paper' and comp_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

#function to get computer choice
def get_comp_choice():
    return random.choice(['rock','paper','scissors'])

#function to get user or player choice
def get_user_choice():
    choice=input("Enter Your Choice (rock ,paper, scissors) : ")
    if choice not in ['rock','paper','scissors']:
        print("""INVALID CHOICE!!
          please choose rock,paper or scissorss""")
    else:
        return choice


#function to play game
def play_game():
    while 1:
        user_choice=get_user_choice()
        comp_choice=get_comp_choice()
        print(f"Computer choose {comp_choice}")
        print(winner(user_choice,comp_choice))
        continue_play=input("Do you want to play again ?(yes/no) :")
        if continue_play!='yes':
            print("Thanks for playing :)")
            break

#START THE GAME
play_game()



