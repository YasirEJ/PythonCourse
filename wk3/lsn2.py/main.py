# set1 = {1, 2, 3, 4, 5, }
# set2 = {1, 2, 3, 4, 6, 7, 8}
#
# # set1.update(set2) == set1 = set1.union(set2)
#
# print(set2)
# print(set1)
# print(set1.isdisjoint(set2))
# from typing import Set

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}

# a.intersection_update(d)

# d.update(a, b, e, )
# g.update(f)
# print(d)
# print(c)
# print(g)
# first = {1, 2, 3, 5}
# second = {1, 2, 3, 5, 7}
#
# if first.issuperset(second):
#     print("is superset")
# else:
#     print('is not')



# if first.issubset(second) & False == second.issubset(first):
#     print(f'Obekt {second} eto chistoe supermnozhestvo')
# elif first.issubset(second) == False &  second.issubset(first):
#     print(f'Obekt {first} eto chistoe supermnozhestvo')
# elif first.issubset(second) == False & False == second.issubset(first):
#     print('Supermmozhestvo ne obnoruzheno')
# elif first.issubset(second) == False & False == second.issubset(first):
#     print('Supermmozhestvo ne obnoruzheno')
# elif first == second:
#     print('Supermmozhestvo ne obnoruzheno')



# comprehentioms - lidt, dict

# lists = [i for i in range()]
# print(lists)

# import datetime

# time_now = datetime.datetime.now()
# lists2 = ['banana', 'apple', 'pineapple', 'pen', 'cucumber']
# lists = {i: i*2 for i in lists2}
# print(lists)/
# print(datetime.datetime.now() - time_now)

# ubrat if

# from random import randint



# name_of_player = input('Enter your name: ')

# computer_points = 0
# player_points = 0

# while True:

#     choice_of_player = int(input('stone (1) or paper (2) or csossors (3): '))
#     choice_of_computer = randint(1, 3)

#     print(f'computer chose {choice_of_computer}')

#     if choice_of_computer == choice_of_player:
#         print('draw')
#         continue
#     elif choice_of_computer == 1 and choice_of_player == 2:
#         print(f'{name_of_player} win this round!')
#         player_points += 1
#         # continue
#     elif choice_of_computer == 2 and choice_of_player == 3:
#         print(f'{name_of_player} win this round!')
#         player_points += 1
#         # continue
#     elif choice_of_computer == 3 and choice_of_player == 1:
#         print(f'{name_of_player} win this round!')
#         player_points += 1
#         # continue
#     elif choice_of_computer == 1 and choice_of_player == 3:
#         print(f'{name_of_player} lose this round!')
#         computer_points += 1
#         # continue
#     elif choice_of_computer == 2 and choice_of_player == 1:
#         print(f'{name_of_player} lose this round!')
#         computer_points += 1
#         # continue
#     elif choice_of_computer == 3 and choice_of_player == 2:
#         print(f'{name_of_player} lose this round!')
#         computer_points += 1
#         # continue

#     if player_points == 3:
#         print('YOU WIN!!!')
#         break
#     elif computer_points == 3:
#         print('YOU LOSE!!!')
#         break  
#     print(f'your points: {player_points}')
#     print(f'points of computer: {computer_points}')
