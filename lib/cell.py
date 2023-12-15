class Cell:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.ship = None
        self.fired_upon = False

    def empty(self):
        return self.ship is None

    def place_ship(self, ship):
        self.ship = ship

    def fire_upon(self):
        self.fired_upon = True
        if self.ship:
            self.ship.hit()

    def fired_upon(self):
        return self.fired_upon

    def render(self, reveal_ship=False):
        if self.fired_upon:
            if not self.empty() and self.ship.sunk():
                return "X"
            elif self.empty():
                return "M"
            else:
                return "H"
        else:
            return "S" if reveal_ship and not self.empty() else "."