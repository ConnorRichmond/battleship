from random import sample
from lib.cell import Cell

class Board:
    def __init__(self, size):
        self.size = size
        self.cells = self.create_cells()

    def create_cells(self):
        keys = self.create_keys()
        cells = {}
        for key in keys:
            cells[key] = Cell(key)
        return cells

    def create_keys(self):
        letters = list(map(chr, range(ord('A'), ord('A') + self.size)))
        keys = [f"{letter}{num}" for letter in letters for num in range(1, self.size + 1)]
        return keys

    def last_letter(self):
        all_letters = list(map(chr, range(ord('A'), ord('J') + 1)))
        return all_letters[self.size - 1]

    def valid_coordinate(self, coordinate):
        return coordinate in self.cells

    def valid_placement(self, ship, coordinates):
        return (
            self.same_length(ship, coordinates) and
            self.not_diagonal(coordinates) and
            self.consecutive(ship, coordinates) and
            self.not_overlapping(ship, coordinates)
        )

    def same_length(self, ship, coordinates):
        return len(ship) == len(coordinates)

    def not_diagonal(self, coordinates):
        return coordinates[0][0] == coordinates[1][0] or coordinates[0][1] == coordinates[1][1]

    def consecutive(self, ship, coordinates):
        letters = [coord[0] for coord in coordinates]
        numbers = [coord[1:] for coord in coordinates]
        
        if len(set(letters)) == 1:
            return any(valid_arrays == numbers for valid_arrays in self.number_possibilities(ship))
        elif len(set(numbers)) == 1:
            return any(valid_arrays == letters for valid_arrays in self.letter_possibilities(ship))

    def letter_possibilities(self, ship):
        return [list(map(chr, range(ord('A'), ord(self.last_letter()) - ship + 2))) for _ in range(ship)]

    def number_possibilities(self, ship):
        return [list(map(str, range(1, self.size - ship + 3))) for _ in range(ship)]

    def not_overlapping(self, ship, coordinates):
        return all(self.cells[cell].ship is None for cell in coordinates)

    def place(self, ship, coordinates):
        if self.valid_placement(ship, coordinates):
            for cell in coordinates:
                self.cells[cell].place_ship(ship)

    def render(self, reveal_board=False):
        lines = [self.line_1()]

        for letter in range(ord('A'), ord(self.last_letter()) + 1):
            letter = chr(letter)
            line = letter + ''.join(f' {self.cells[f"{letter}{num}"].render(reveal_board)}' for num in range(1, self.size + 1)) + ' \n'
            lines.append(line)

        return ''.join(lines)

    def line_1(self):
        return ' ' + ' '.join(map(str, range(1, self.size + 1)))

    def randomly_place(self, ship):
        placement = self.random_cells(ship)
        self.place(ship, placement)

    def random_cells(self, ship):
        options = list(self.cells.keys())
        placement = sample(options, k=len(ship))

        while not self.valid_placement(ship, placement):
            placement = sample(options, k=len(ship))

        return placement