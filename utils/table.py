import random

new_colleagues = ["Adheeba, Anastasiia, Basma, Dhrisya, Ihor, Izabela, Kelli, Kevin, Levin, Maarten, Moustafa, Muntadher, Nicolaas, Petra, Rasmita, Rik, Soha, Tom, Urson, Veena, Wouter, Yeliz, Yusra, Zelimkhan"]

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
        if self.free:
            return f"free seat"
        else:
            return f"{self.occupant}"
        
seat_1 = Seat()
seat_1.set_occupant(random.choices{new_colleagues, k=4})
print(seat_1)
        
class table:
    def __init__(self):
        self.capacity = 4
        self.seats = []
        for seat in range(4):
            self.seats.append(seat)

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
            else:
                return False

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                self.set_occupant(name)
                return True

    def left_capacity(self):
        left_free = 0
        for seat in self.seats:
            if seat.free:
                left_free +=1
        return left_free
    
    def __str__(self):
        pass

table_1 = table()
table_1.assign_seat(random.choice{new_colleagues})
print(table_1.has_free_spot)
print(table_1.left_capacity)