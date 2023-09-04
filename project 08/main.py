from art import logo 
from art import vs
from game_data import data
import os
import random

score = 0
continous = True

# data questions
def data_ques(account) :
  '''account data on the questions'''
  name = account['name']
  desc = account['description']
  cont = account['country']
  return (f"{name}, {desc}, from {cont} ")

# use if statement to correct the answer already true or false
def check_answer (answer, followers_a, followers_b): 
    '''use if statement to correct the answer already true or false'''
    if followers_a > followers_b :
        return answer == 'a'
    else :
        return answer == 'b'

random_ques_2 = random.choice(data)

while continous : 
    '''print logo'''
    print(logo)

    # make function of questions
    random_ques_1 = random_ques_2
    random_ques_2 = random.choice(data)
    remove_1 = data.remove(random_ques_1)
    
    print(f"Compare A : {data_ques(random_ques_1)}")
    print(vs)
    print(f"Aggainst B : {data_ques(random_ques_2)}")
    
    answer = str(input(f"\nwho has more followers? Type 'A' or 'B': ")).lower()
    

    # get the follower of two account 
    followers_a =  random_ques_1['follower_count']
    followers_b = random_ques_2['follower_count']
    is_correct = check_answer(answer, followers_a, followers_b)

    # clear the code
    os.system('cls')

    # feedback output
    # score view
    if is_correct :
        score += 1
        print(f"You're right Congratulation. Current score : {score}")

    else :
        print(f"WRONGGGG !!!!, you looseee. Current score : {score}")
        continous = False




# def game():
#   print(logo)
#   print(f"compare A : ")
  

# game()




 






# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# random_element = random.choice(my_list)
# b = my_list.pop(random_element)
# a = [random_element]
# a = b
# print(b)
# print(my_list)
