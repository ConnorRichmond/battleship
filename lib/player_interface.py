class PlayerInterface:
    # Main Menu
    def welcome(self):
        print("Welcome to BATTLESHIP\n" +
              "Enter p to play. Enter q to quit.")
        return input().strip().lower()

    def quit(self):
        print("Thank you for playing BATTLESHIP!")

    def invalid_start(self):
        print('Invalid Input. Please use either p or q.')

    # Build Board
    def game_board_intro(self):
        print("Let's build your game board!\n" +
              "The game board can be 4x4 squares up to 10x10 squares")

    def get_board_size(self):
        print("Please enter the number of rows and columns you want (min of 4 & max of 10):")
        size = int(input().strip())
        while size < 4 or size > 10:
            print("Please enter a valid number between 4 and 10:")
            size = int(input().strip())
        return size

    def get_ship_count(self):
        print("Enter the number of ships to create:")
        ship_count = int(input().strip())
        while ship_count < 1 or ship_count > 5:
            print('Invalid Input. Must create at least one ship but less than 5.')
            ship_count = int(input().strip())
        return ship_count

    # Create Ships
    def get_ship_name(self, i):
        print(f"Enter the name for Ship {i + 1}:")
        name = input().strip()
        while not name:
            print("Name cannot be empty.")
            print(f"Enter the name for Ship {i + 1}:")
            name = input().strip()
        return name

    def get_ship_length(self, name, size):
        print(f"Enter the length for the {name}:")
        length = int(input().strip())
        while length <= 1 or length > size:
            print("Please enter a length greater than 1 and less than the board size.")
            print(f"Enter the length for the {name}:")
            length = int(input().strip())
        return length

    # Place Ships
    def get_ship_placement(self, ship, player_board):
        print(f"Enter the squares for the {ship.name} ({ship.length} spaces):")
        print(player_board.render(True))
        return input().strip().upper().split()

    def invalid_placement(self):
        print("Those are invalid coordinates. Please try again.")

    # Take Turns
    def render_board(self, computer_board, player_board):
        print("=============COMPUTER BOARD=============")
        print(computer_board.render())
        print("==============PLAYER BOARD==============")
        print(player_board.render(True))

    # Player Shots
    def choose_coordinate(self):
        print("Choose a coordinate to fire at:")
        return input().strip().upper()

    def invalid_shot(self):
        print("Please enter a valid coordinate.")

    def already_shot_at(self, shoot_at):
        print(f"Oops! You already fired at {shoot_at}.")

    def player_render_shot(self, cell):
        print(f"Your shot on {cell.coordinate} was a {self.hit_miss_sink(cell)}.")

    def computer_render_shot(self, cell):
        print(f"My shot on {cell.coordinate} was a {self.hit_miss_sink(cell)}.")

    # This is a helper method for describing the shots
    def hit_miss_sink(self, cell):
        if cell.render() == "M":
            return "miss"
        elif cell.render() == "H":
            return "hit"
        elif cell.render() == "X":
            return f"hit and sunk the {cell.ship.name} \U0001F62D"

    # End of Game
    def computer_won(self):
        print("\nI won! Better luck next time \U0001F61C")

    def player_won(self):
        print("\n\U0001F389 Congrats! You won!! \U0001F3C6")

    def return_to_menu(self):
        print("\nHit ENTER to return to the Main Menu")
        input()