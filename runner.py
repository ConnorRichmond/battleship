from lib.ship import Ship
from lib.cell import Cell
from lib.board import Board
from lib.new_game import NewGame
from lib.player_interface import PlayerInterface

def main():
    game = NewGame()
    game.main_menu()

if __name__ == "__main__":
    main()