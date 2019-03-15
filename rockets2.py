from math import sqrt


class Rocket:
    # creates rocket class
    # initialises default values for x and y
    # use None to allow passing of no arguments to Class init(ie. lst comprehension)
    def __init__(self, name=None, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.fuel = 100
        self.crew = 8

    # moves rocket to specified parameters
    def move_rocket(self, x_increment=0, y_increment=1):
        # reduces fuel by distance travelled
        self.fuel -= round(sqrt((x_increment**2) + (y_increment**2)))
        self.x += x_increment
        self.y += y_increment

    # calculates distance between two specified rockets
    def get_distance(self, other_rocket):
        return round(sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2), 3)


# creates fleet of unique rockets
rockets = [Rocket() for rocket in range(0, 5)]

rocket_1 = rockets[0]

rocket = Rocket('Apollo')

print(rocket.fuel, rocket.x, rocket.y, rocket.name)

rocket_1.name = 'Starship'

print(rocket_1.fuel, rocket_1.x, rocket_1.y, rocket_1.name)

rocket_1.move_rocket(10, 5)

print(rocket_1.fuel, rocket_1.x, rocket_1.y, rocket_1.name)

rocket_1.move_rocket(11, 2)

print(rocket_1.fuel, rocket_1.x, rocket_1.y, rocket_1.name)

rocket_1.move_rocket(17, 21)

print(rocket_1.fuel, rocket_1.x, rocket_1.y, rocket_1.name)

rocket_1.move_rocket()

print(rocket_1.fuel, rocket_1.x, rocket_1.y, rocket_1.name, rocket_1.crew)
