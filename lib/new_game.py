from lib.board import Board
from lib.ship import Ship
from lib.player_interface import PlayerInterface

class NewGame:
    def __init__(self):
        self.player_interface = PlayerInterface()

    def main_menu(self):
        response = self.player_interface.welcome()
        if response == 'p':
            self.play()
        elif response == 'q':
            self.player_interface.quit()
        else:
            self.player_interface.invalid_start()
            self.main_menu()

    def play(self):
        self.build_board()
        self.create_ships(self.player_interface.get_ship_count())
        self.player_place_ships()
        self.computer_place_ships()
        while not all(ship.sunk() for ship in self.player_ships) and not all(ship.sunk() for ship in self.computer_ships):
            self.take_turns()
        self.end_of_game()

    def build_board(self):
        self.player_interface.game_board_intro()
        self.size = self.player_interface.get_board_size()
        self.computer_board = Board(self.size)
        self.player_board = Board(self.size)

    def create_ships(self, count):
        self.player_ships = []
        self.computer_ships = []
        for i in range(count):
            name = self.player_interface.get_ship_name(i)
            length = self.player_interface.get_ship_length(name, self.size)
            self.player_ships.append(Ship(name, length))
            self.computer_ships.append(Ship(name, length))

    def player_place_ships(self):
        for ship in self.player_ships:
            self.place_ship(ship, self.player_board)

    def computer_place_ships(self):
        for ship in self.computer_ships:
            self.computer_board.randomly_place(ship)

    def place_ship(self, ship, board):
        ship_placement = self.player_interface.get_ship_placement(ship, board)
        if board.valid_placement(ship, ship_placement):
            board.place(ship, ship_placement)
        else:
            self.player_interface.invalid_placement()
            self.place_ship(ship, board)

    def take_turns(self):
        self.player_interface.render_board(self.computer_board, self.player_board)
        self.player_shot()
        if not all(ship.sunk() for ship in self.computer_ships):
            self.computer_shot()

    def player_shot(self):
        shoot_at = self.player_interface.choose_coordinate()
        cell = self.computer_board.cells[shoot_at]
        if not self.computer_board.valid_coordinate(shoot_at):
            self.player_interface.invalid_shot()
            self.player_shot()
        elif cell.fired_upon():
            self.player_interface.already_shot_at(shoot_at)
            self.player_shot()
        else:
            cell.fire_upon()
            self.player_interface.player_render_shot(cell)

    def computer_shot(self):
        random_cell = self.player_board.random_cells(1)[0]
        while self.player_board.cells[random_cell].fired_upon():
            random_cell = self.player_board.random_cells(1)[0]
        cell = self.player_board.cells[random_cell]
        cell.fire_upon()
        self.player_interface.computer_render_shot(cell)

    def end_of_game(self):
        if all(ship.sunk() for ship in self.player_ships):
            self.player_interface.computer_won()
        elif all(ship.sunk() for ship in self.computer_ships):
            self.player_interface.player_won()
        self.player_interface.return_to_menu()
        self.main_menu()