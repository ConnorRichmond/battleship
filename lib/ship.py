class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = length
        self.sunk = False

    def sunk(self):
        return self.sunk

    def hit(self):
        if self.health > 0:
            self.health -= 1
            self.sunk = True if self.health == 0 else False