import welcome

def plot_board(mapping_dict):
    horizontal_line = "-----"
    board: str = (
        mapping_dict["1 1"] + "|" + mapping_dict["1 2"] + "|" + mapping_dict["1 3"] + "\n" +
        horizontal_line + "\n" +
        mapping_dict["2 1"] + "|" + mapping_dict["2 2"] + "|" + mapping_dict["2 3"] + "\n" +
        horizontal_line + "\n" +
        mapping_dict["3 1"] + "|" + mapping_dict["3 2"] + "|" + mapping_dict["3 3"] + "\n"
    )
    print(board)
       
             

def initialize():
    mapping_dict = {"1 1": " ", "1 2": " ", "1 3": " ",
                "2 1": " ", "2 2": " ", "2 3": " ",
                "3 1": " ", "3 2": " ", "3 3": " ",
                }
    return mapping_dict


def modify_board(map_dict, user_choice, user_num):
    if user_num == 1:
        map_dict[user_choice] = "X"
    else:
        map_dict[user_choice] = "O"
    plot_board(mapping_dict=map_dict)


def count_point(map_dict):
    temp_dict = map_dict.copy()
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
    return max(list_comb), min(list_comb)