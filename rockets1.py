from math import sqrt


class Rocket:
    # creates rocket class
    # initialises default values for x and y
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # moves rocket to specified parameters
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

    # calculates distance between two specified rockets
    def get_distance(self, other_rocket):
        return round(sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2), 3)


# creates fleet of unique rockets
rockets = [Rocket() for rocket in range(0, 5)]

for i in rockets:
    print(i)

print(rockets[0].x, rockets[0].y)

rockets[0].move_rocket(10, 5)

print(rockets[0].x, rockets[0].y)

rockets[0].move_rocket(-10, -5)

print(rockets[0].x, rockets[0].y)

rockets[0].move_rocket(-10, -5)

print(rockets[1].x, rockets[1].y)

rockets[1].move_rocket(7, 3)

rockets[2].move_rocket(12, 15)

rockets[3].move_rocket(6, 2)

rockets[4].move_rocket(11, 9)

distance = rockets[0].get_distance(rockets[1])
print(distance)

distance = rockets[0].get_distance(rockets[2])
print(distance)

distance = rockets[0].get_distance(rockets[3])
print(distance)

distance = rockets[0].get_distance(rockets[4])
print(distance)
