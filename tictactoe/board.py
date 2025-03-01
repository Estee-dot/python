class Board:
    def __init__(self):
        self.__board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def display_board(self):
        print("\n Welcome to NaturalQueen's TicTacToe Game🎊🎊🎊. Have FUNNNN!🎮🧩")
        print("\n______________")
        for i in range(3):
            print("| ", end="")
            for j in range(3):
                print(self.__board[i][j] + " | ", end="")
            print("\n______________")
        print()

    def winning_condition(self, player):
        for i in range(3):
            if all([self.__board[i][j] == player for j in range(3)]) or all([self.__board[j][i] == player for j in range(3)]):
                return True
        if self.__board[0][0] == player and self.__board[1][1] == player and self.__board[2][2] == player:
            return True
        if self.__board[2][0] == player and self.__board[1][1] == player and self.__board[0][2] == player:
            return True
        return False

    def players_moves(self, moves: int, token: str):
        if not 1 <= int(moves) <= 9:
            raise ValueError("Invalid Move! Kindly try again🌚")
        row = (moves - 1) // 3
        col = (moves - 1) % 3
        if self.__board[row][col] != " ":
            raise ValueError("Position has been taken, Try again you Chicken🐔")
        self.__board[row][col] = token

    def get_board(self):
        return self.__board


board = Board()
board.display_board()
