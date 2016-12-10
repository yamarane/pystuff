# python3
# Its random guess game
import random
print("hey, i selected one number between 1 to 9\ncan you guess it?")
computer_guess = random.randint(0, 9)
count = 0
game_running = True
while game_running:
    try:
        user_guess = input("enter you guess number: ")
        if user_guess == 'exit':
            print("good bye")
            break
        elif user_guess == '':
            print("your guess should not be empty !")
            break
        elif int(user_guess) not in range(0, 10):
            print("your guess is beyond 0-9 range !!")
            break
        else:
            user_guess = int(user_guess)
    except ValueError as e:
        print(str(e))
        print("its not a digit...you should enter 0-9 only")
        continue
    count += 1
    if computer_guess < user_guess:
        print("? < %s ---> guess is too high" % user_guess)
    elif computer_guess > user_guess:
        print("? > %s ---> guess is too low" % user_guess)
    else:
        print("%s = %s ---> yey you guessed it !\n" % (computer_guess, user_guess))
        print("it took %s time(s) to find correct number !" % count)
        print("if you wanna continue enter a number between 0 to 9 else enter \'exit\'")
        computer_guess = random.randint(0, 9)
        count = 0
