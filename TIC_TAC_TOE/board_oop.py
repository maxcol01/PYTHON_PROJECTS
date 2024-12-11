import numpy as np
import re

class Board:

    def __init__(self):
        self.map_dict= {"1 1": " ", "1 2": " ", "1 3": " ",
                "2 1": " ", "2 2": " ", "2 3": " ",
                "3 1": " ", "3 2": " ", "3 3": " ",
                }
        self.horizontal_line = "-----"
        self.count1, self.count2 = 0, 0


    def print_board(self):
        board: str = (
        self.map_dict["1 1"] + "|" + self.map_dict["1 2"] + "|" + self.map_dict["1 3"] + "\n" +
        self.horizontal_line + "\n" +
        self.map_dict["2 1"] + "|" + self.map_dict["2 2"] + "|" + self.map_dict["2 3"] + "\n" +
        self.horizontal_line + "\n" +
        self.map_dict["3 1"] + "|" + self.map_dict["3 2"] + "|" + self.map_dict["3 3"] + "\n"
    )
        print(board)


    def modify_board(self, user_choice, user_num):
        if user_num == 1:
            self.map_dict[user_choice] = "X"
        else:
            self.map_dict[user_choice] = "O"
        self.print_board()
    

    def check_score(self, user_num):
        temp_dict = self.map_dict.copy()
        for key, value in temp_dict.items():
            if  value == "X":
                temp_dict[key] = 1
            elif value == "O":
                temp_dict[key] = -1
            else:
                temp_dict[key] = 0

        comb1 = temp_dict["1 1"]+temp_dict["1 2"]+temp_dict["1 3"]
        comb2 = temp_dict["2 1"]+temp_dict["2 2"]+temp_dict["2 3"]
        comb3 = temp_dict["3 1"]+temp_dict["3 2"]+temp_dict["3 3"]

        comb4 = temp_dict["1 1"]+temp_dict["2 1"]+temp_dict["3 1"]
        comb5 = temp_dict["1 2"]+temp_dict["2 2"]+temp_dict["3 2"]
        comb6 = temp_dict["1 3"]+temp_dict["2 3"]+temp_dict["3 3"]

        comb7 = temp_dict["1 1"]+temp_dict["2 2"]+temp_dict["3 3"]
        comb8 = temp_dict["3 1"]+temp_dict["2 2"]+temp_dict["1 3"]
        list_comb = [comb1, comb2, comb3, comb4, comb5, comb6, comb7, comb8]
        self.count1 = max(list_comb)
        self.count2 = min(list_comb) 
        print(f"Player 1 you current score is {self.count1}")
        print(f"Player 2 you current score is {np.abs(self.count2)}")

        if self.count1 == 3 or self.count2 == -3:
            print("##########################################")
            print(f"Player {user_num} Congrats ! You Win !!! ")
            print("##########################################")
            return False
        return True
    
    
    def check_for_draw(self):
        if  (self.count1 < 3 and self.count2 > -3):
            print("It is a draw !!!")


def check_user_input(user_num):
    valid_type_answer = r"[1-3] [1-3]"
    user_choice = input(f"Enter your choice player {user_num}: ")
    print(user_choice)
    if re.search(valid_type_answer, user_choice):
        return True, user_choice
    else:
        # return the call of the function to include 
        # the returned values when the condition above is true 
        # otherwise it will implicitly retrun None.
        return check_user_input(user_num)

    
