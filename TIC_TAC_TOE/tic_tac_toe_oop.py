from board_oop import Board, check_user_input
import re

playing_board =Board()

playing_board.print_board()

counter = 0
is_on = True

while counter < 9 and is_on:
    if counter % 2 == 0:
        user_num = 1
    else:
        user_num = 2
    is_correct, user_choice = check_user_input(user_num=user_num)
    if is_correct:
        playing_board.modify_board(user_choice= user_choice, 
                                   user_num=user_num)

        is_on = playing_board.check_score(user_num=user_num)
        
        if counter == 8:
            is_on = False
            playing_board.check_for_draw()
        counter += 1
