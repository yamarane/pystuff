# python3
# classic rock-scissor-paper game
import random
game_running = True
while game_running:
    print("Do you wanna play Rock Paper Scissors game ?")
    user_input = input("enter rock or paper or scissor: ")
    items = ['rock', 'paper', 'scissor']
    computer = random.choice(items)
    print("user : %s    vs    computer : %s \n" % (user_input, computer))
    if user_input == computer:
        print("GAME IS TIE !\n")
    elif user_input == 'paper' and computer == 'rock':
        print("PAPER BEATS ROCK ---> USER WINS\n\n")
    elif user_input == 'scissor' and computer == 'paper':
        print("SCISSOR BEATS PAPER ---> USER WINS\n\n")
    elif user_input == 'rock' and computer == 'scissor':
        print("ROCK BEATS SCISSOR ---> USER WINS\n\n")
    else:
        print("%s BEATS %s ---> COMPUTER WINS\n" % (computer, user_input))
