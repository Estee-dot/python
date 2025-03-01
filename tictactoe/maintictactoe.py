from player import Player
from board import Board

def sign_in_first_player():
    name = input("Enter your name: ")
    while not name.isalpha():
        print("Invalid input, Kindly enter your name: ")
        name = input("Enter your name: ")

    token = input("Enter your token. Either x or o: ")
    while token not in ["x", "o"]:
        print("Invalid Token, Kindly try again")
        token = input("Enter your token: ")
    first_player = Player(name, token)
    return first_player, token

def choose_second_token(first_player_token):
    return "x" if first_player_token == "o" else "o"

def sign_in_second_player(first_token):
    name = input("Enter your name: ")
    while not name.isalpha():
        print("Invalid input, Kindly enter your name: ")
        name = input("Enter your name: ")

    second_token = choose_second_token(first_token)
    second_player = Player(name, second_token)
    return second_player

class Game:
    def __init__(self):
        self.board = Board()

    def is_draw(self):
        for row in self.board.get_board():
            if " " in row:
                return False
        return True

    def play(self):
        players = []
        first_player, first_token = sign_in_first_player()
        players.append(first_player)
        print(first_player)

        second_player = sign_in_second_player(first_token)
        players.append(second_player)
        print(second_player)

        board = self.board
        counter = 0

        while counter < 9:
            for player in players:
                play = input(f"Dear Player {player.get_name()}, Choose a number between 1 - 9: ")
                while not play.isdigit() or not 1 <= int(play) <= 9:
                    print("Are you a chicken???🐔🐔🐔, Play again chicken bumbum!")
                    play = input(f"Dear Player {player.get_name()}, Choose a number between 1 - 9: ")
                    continue

                play = int(play) - 1
                row = play // 3
                col = play % 3
                if board.get_board()[row][col] != " ":
                    print("This Cell has already been occupied, Play next☺️")
                    continue

                board.players_moves(play + 1, player.get_token())
                board.display_board()

                if board.winning_condition(player.get_token()):
                    print(f"Player {player.get_name()} has won!!!!!🎊🎉 Congratulations!💃🏼💃🏼💃🏼💃🏼💃🏼")
                    return

                if self.is_draw():
                    print("Awww! It's a Tie☺️💃🏼")
                    return

                counter += 1

if __name__ == "__main__":
    game = Game()
    game.play()
