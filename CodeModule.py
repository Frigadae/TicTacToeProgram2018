class tictactoe:
    def __init__(self, array):
        self.array = array
    def is_full(self):
        available_space = []
        for row in self.array:
            for grid in row:
                if "_" in grid:
                    available_space.append(grid)
        total = len(available_space)
        if total == 0:
            return True
        else:
            return False
    def set_coord(self, x, y):
        self.array[y][x][0] = "X"
    def AI_set_coord(self, x, y):
        self.array[y][x][0] = "O"
    def check_coord(self, x, y):
        if self.array[y][x][0] == "_":
            return True
        else:
            return False
    def __str__(self):
        for cell in self.array:
            print(cell)
    def check_win(self):
        if self.array[0][0][0] == "X" and self.array[1][0][0] == "X" and self.array[2][0][0] == "X":
            return True
        elif self.array[0][1][0] == "X" and self.array[1][1][0] == "X" and self.array[2][1][0] == "X":
            return True
        elif self.array[0][2][0] == "X" and self.array[1][2][0] == "X" and self.array[2][2][0] == "X":
            return True
        elif self.array[0][0][0] == "X" and self.array[0][1][0] == "X" and self.array[0][2][0] == "X":
            return True
        elif self.array[1][0][0] == "X" and self.array[1][1][0] == "X" and self.array[1][2][0] == "X":
            return True
        elif self.array[2][0][0] == "X" and self.array[2][1][0] == "X" and self.array[2][2][0] == "X":
            return True
        elif self.array[0][0][0] == "X" and self.array[1][1][0] == "X" and self.array[2][2][0] == "X":
            return True
        elif self.array[0][2][0] == "X" and self.array[1][1][0] == "X" and self.array[2][0][0] == "X":
            return True
        else:
            return False
    def check_win_AI(self):
        if self.array[0][0][0] == "O" and self.array[1][0][0] == "O" and self.array[2][0][0] == "O":
            return True
        elif self.array[0][1][0] == "O" and self.array[1][1][0] == "O" and self.array[2][1][0] == "O":
            return True
        elif self.array[0][2][0] == "O" and self.array[1][2][0] == "O" and self.array[2][2][0] == "O":
            return True
        elif self.array[0][0][0] == "O" and self.array[0][1][0] == "O" and self.array[0][2][0] == "O":
            return True
        elif self.array[1][0][0] == "O" and self.array[1][1][0] == "O" and self.array[1][2][0] == "O":
            return True
        elif self.array[2][0][0] == "O" and self.array[2][1][0] == "O" and self.array[2][2][0] == "O":
            return True
        elif self.array[0][0][0] == "O" and self.array[1][1][0] == "O" and self.array[2][2][0] == "O":
            return True
        elif self.array[0][2][0] == "O" and self.array[1][1][0] == "O" and self.array[2][0][0] == "O":
            return True
        else:
            return False

class checker:
    def __init__(self, user_input):
        self.user_input = user_input
    def if_alpha(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            if self.user_input == letter:
                return True
        return False
    def if_quit(self):
        if int(self.user_input) == 0:
            return True
        else:
            pass
    def within_limits(self):
        if 1 <= int(self.user_input) <= 3:
            return True
        else:
            return False
        
