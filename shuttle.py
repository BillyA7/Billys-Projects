from math import sqrt


class Rocket:
    # creates rocket class
    # initialises default values for x and y
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    # moves rocket to specified parameters
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

    # calculates distance between two specified rockets
    def get_distance(self, other_rocket):
        return round(sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2), 3)

class Shuttle(Rocket):

    def __init__(self, name, x=0, y=0, flights_completed=0, max_flights=0, spacewalk_capable=True, docking_capable=True):
        super().__init__(name, x, y)
        self.flights_completed = flights_completed
        self.max_flights = max_flights
        self.spacewalk_capable = spacewalk_capable
        self.docking_capable = docking_capable

    def dock_ISS(self, shuttle):
        return f'{shuttle} is docking with ISS.'

apollo = Shuttle('Apollo 7', 10, 10, 5, 10)

apollo.move_rocket(12, 4)

print(f'The {apollo.name} is at coordinates x:{apollo.x}, y:{apollo.y}. It has completed {apollo.flights_completed} flights out of it\'s maximum {apollo.max_flights} possible. ' + apollo.dock_ISS(apollo.name))
