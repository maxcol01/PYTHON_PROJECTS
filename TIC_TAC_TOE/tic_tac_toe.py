# to do 
# 1. display the board
# 2. Manually modify and display the board
# 3. ask for user input

from board import initialize, plot_board, modify_board, count_point
import numpy as np # type: ignore
map_dict = initialize()
plot_board(mapping_dict=map_dict)

# user for X
counter = 0
while counter < 9:
    if counter % 2 == 0:
        user_num = 1
    else:
        user_num = 2

    user_choice = input(f"Enter your choice player {user_num}: ")

    modify_board(map_dict=map_dict, user_choice=user_choice, user_num = user_num)

    count1, count2 = count_point(map_dict=map_dict)
    print(f"Player 1 you current score is {count1}")
    print(f"Player 2 you current score is {np.abs(count2)}")

    if count1 == 3 or count2 == -3:
        print(f"Player {user_num} Congrats ! You Win !!! ")
        break
    counter += 1

if  (count1 < 3 or count2 > -3):
    print("It is a draw !!!")

