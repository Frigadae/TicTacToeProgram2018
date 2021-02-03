"""
Super advanced coding skillz!
"""
import random
from CodeModule import tictactoe
from CodeModule import checker

def main():
    head()
    body()

def head():
    banner = "\
       ___       ______         ____              ___           ___   \n\
      /  / |   /   /    /   /  /   /  /|   /     /    \   /    /      \n\
     /__/  |__/   /    /___/  /   /  / |  /     /__    \_/    /__     \n\
    /        /   /    /   /  /   /  /  | /     /       / \   /        \n\
   /        /   /    /   /  /___/  /   |/  o  /___    /   \ /___      \n"
    dash = "-" * ((len(banner) // 5) // 5)
    message = dash + "A file for testing whatever code you write" + dash
    message_2 = len(message) * "-"
    print(message_2)
    print(message_2)
    print(banner)
    print(message)
    print(message_2)

def body():
    """Put your stuff here!"""
    title()
    game()

def title():
    banner = "-- TIC TAC TOE SIMULATOR --"
    lines = len(banner) * "-"
    print()
    print(lines)
    print(banner)
    print(lines)
    print()

def game():
    array = tictactoe([[["_"],["_"],["_"]], [["_"],["_"],["_"]], [["_"],["_"],["_"]]])
    message_1 = "-- Place your coodinates --"
    message_2 = "----- To quit press 0 -----"
    print(message_1)
    print(message_2)
    print()
    x_axis = None
    y_axis = None
    while True:
        if array.is_full() == True:
            break
        x_coord = input("Place your X coordinate: ")
        x_axis = input_checker(x_coord)
        if x_axis == None:
            break
        y_coord = input("Place your Y coordinate: ")
        y_axis = input_checker(y_coord)
        if y_axis == None:
            break
        set_array(array, x_axis, y_axis)
        status = check_if_won(array)
        if status == True:
            print("The player has won!")
            break
        status = check_if_AI_won(array)
        if status == True:
            print("The Computer has won!")
            break
    print("Thank you for playing!")

def input_checker(value):
    while True:
        check = checker(value)
        outcome = check.if_alpha()
        if outcome == True:
            print("Input must be a single digit number!")
        else:
            outcome = check.if_quit()
            if outcome == True:
                return None
            else:
                outcome = check.within_limits()
                if outcome == True:
                    return int(value)
                else:
                    print("Please ensure your input is between 1 and 3 (Inclusive)")
        value = input("Try again: ")

def set_array(array, x_axis, y_axis):
    x_axis -= 1
    y_axis -= 1
    if array.check_coord(x_axis, y_axis) == True:
        array.set_coord(x_axis, y_axis)
        array.__str__()
        status = check_if_won(array)
        if status == True:
            return
        else:
            print(" --- Computer will now make their turn --- ")
            AI_turn(array)
    else:
        print("Cell already filled, please try again.")

def AI_turn(array):
    x_axis = random.randrange(0, 2)
    y_axis = random.randrange(0, 2)
    while True:
        if array.check_coord(x_axis, y_axis) == True:
            array.AI_set_coord(x_axis, y_axis)
            array.__str__()
            print(" --- Your turn --- ")
            break
        else:
            status = check_if_AI_won(array)
            if status == True:
                break
            if array.is_full() == False:
                x_axis = random.randrange(0, 3)
                y_axis = random.randrange(0, 3)
            else:
                print("-- No more available space, game ends in a draw --")
                break

def check_if_won(array):
    if array.check_win() == True:
        return True
    else:
        return False

def check_if_AI_won(array):
    if array.check_win_AI() == True:
        return True
    else:
        return False

main()
