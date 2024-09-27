class Seat:
    def __init__(self):
        self.free = True
        self.occupant = ""

    def set_occupant(self, name):
        self.free = False
        self.occupant = name

    def remove_occupant(self):
        self.free = True
        self.occupant = ""

    def __str__(self):
        pass
        
class table:
    def __init__(self):
        self.capacity = 4
        self.seats = []
        for seat in range(4):
            self.seats.append(seat)

    def has_free_spot(self):
        if self.seats < self.capacity:
           print(True)

    def assign_seat(self, name):
        self.assign_seat = name

    def left_capacity(self):
        self.left_capacity = int(self.capacity - self.seats)
        



