#Number Guessing Game Objectives:
import random
number = []
for i in range(1, 101):
  number.append(i)
# print(number)
# Include an ASCII art logo.
art = '''
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/ 
'''
print(art)
# Allow the player to submit a guess for a number between 1 and 100.
print(f"Welcome to the Number Guessing Game !!!")
print(f"I'm thinking of a number between 1 and 100.")

key = random.choice(number)
print(key)

easy = 10
hard = 5

input_1 = str(input(f"Choose difficulty. Type 'easy' or 'hard' : "))
if input_1 == 'easy' :
  print(f"You have {easy} attempts remaining to guess")
  guess = int(input("Make a guess : "))
elif input_1 == 'hard' :
  print(f"You have {hard} attempts remaining to guess")
  guess = int(input("Make a guess : "))
else :
 print("read the instruction COK!\n\n\n")
 guess = "END"

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# key = 10
# guess = 5

# if key > guess :
#   print("Too low, guess again")
#   print("You have 4  attempts remaining to guess")

while key != guess :
  if guess == "END" :
    break
  if input_1 == 'easy' :
        easy -= 1
        print(easy)
        def tebak (guess) :
            if key > guess :
                print("Too low, guess again")
                print(f"You have {easy}  attempts remaining to guess")
            # guess_again = int(input("make guess again : "))
            elif key < guess :
             print("too high, guess again")
             print(f"You have {easy}  attempts remaining to guess")
        tebak(guess)
        guess = int(input("make guess again : "))
        if key == guess :
            print(f"you've got it. the number is {key}\n")
        if easy == 0 :
            key == guess
            print(f"You attempts is over, You Looooseeee :( \n")
            print(f"the number is {key}\n")
            break
  elif input_1 == 'hard' :
        hard -= 1
        print(hard)
        def tebak (guess) :
            if key > guess :
                print("Too low, guess again")
                print(f"You have {hard}  attempts remaining to guess")
            # guess_again = int(input("make guess again : "))
            elif key < guess :
             print("too high, guess again")
             print(f"You have {hard} attempts remaining to guess")
        tebak(guess)
        guess = int(input("make guess again : "))
        if key == guess :
            print(f"you've got it. the number is {key}\n")
        if hard == 0 :
            key == guess
            print(f"You attempts is over, You Looooseeee :( \n")
            print(f"the number is {key}\n")
            break
        

            




# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

