import random
list_of_possible = ['rock', 'paper', 'scissors']

computer_choice = random.choice(list_of_possible)

player_choice = input('What do you choose? Type 0 for rock 1 for Paper or 2 for Scissors: ')

if player_choice == '0':
    player_choice = list_of_possible[0]
elif player_choice == '1':
    player_choice = list_of_possible[1]  
else:
    player_choice = list_of_possible[2]
print(f"Computer choose:{computer_choice}")
print(f"You choose:{player_choice}")
if player_choice == list_of_possible[0] and computer_choice  == list_of_possible[2]: 
    print('you won')
elif player_choice == list_of_possible[1] and computer_choice  == list_of_possible[0]:
    print('you won')
elif player_choice == list_of_possible[2] and computer_choice  == list_of_possible[1]:
    print('you won')
elif player_choice == list_of_possible[0] and computer_choice  == list_of_possible[1]:
    print('you lost')
elif player_choice == list_of_possible[1] and computer_choice  == list_of_possible[2]:
    print('you lost')
elif player_choice == list_of_possible[2] and computer_choice  == list_of_possible[0]:
    print('you lost')
else:
    print('draw')

