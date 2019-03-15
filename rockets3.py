import time
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

    # warning message if rockets get too close
    def safety_check(self, other_rocket):
        if self.get_distance(other_rocket) == 0.0:
            print('THE ROCKETS HAVE CRASHED!')
        elif self.get_distance(other_rocket) < 5:
            print('WARNING COLLISON IMMINENT! PLEASE CHANGE COURSE!')

    # launch sequence
    def launch(self, rocket):
        for i in reversed(range(1, 11)):
            print(i)
            time.sleep(1)
        print(f'We have lift off for the {rocket}!')

    # landing sequence
    def land_rocket(self):
        print('Initiating landing manoeuvre.')
        count = 5
        while count > 0:
            print('Descending...')
            time.sleep(1)
            count -= 1
        self.x = 0
        self.y = 0
        print('Landing completed successfully!')



# creates fleet of unique rockets
rockets = [Rocket() for rocket in range(0, 5)]

rocket_1 = rockets[0]
rocket_1.name = 'Apollo 13'

rocket_2 = rockets[1]
rocket_2.name = 'Starship Enterprise'

rocket_3 = rockets[2]
rocket_3.name = 'Nebuchadnezzar'

rocket_3.launch(rocket_3.name)
rocket_3.move_rocket(7, 7)
time.sleep(2)

print(f'{rocket_3.name} is currently at coordinates X: {rocket_3.x} and Y: {rocket_3.y}.')
time.sleep(2)

rocket_3.land_rocket()
time.sleep(2)
print(f'Final coordinates for {rocket_3.name} are X: {rocket_3.x} and Y: {rocket_3.y}.')

rocket_1.launch(rocket_1.name)
rocket_2.launch(rocket_2.name)
time.sleep(1)

rocket_1.move_rocket(13, 7)
rocket_2.move_rocket(10, 7)

print(f'{rocket_1.name} is currently at coordinates X: {rocket_1.x} and Y: {rocket_1.y}.')
time.sleep(1)
print(f'{rocket_2.name} is currently at coordinates X: {rocket_2.x} and Y: {rocket_2.y}.')
time.sleep(1)
print(f'{rocket_1.name} is {rocket_1.get_distance(rocket_2)} miles away from the {rocket_2.name}.')
time.sleep(2)

rocket_1.safety_check(rocket_2)

time.sleep(2)
rocket_2.move_rocket(3, 0)
print(f'{rocket_1.name} is {rocket_1.get_distance(rocket_2)} miles away from the {rocket_2.name}.')
time.sleep(1)

rocket_1.safety_check(rocket_2)

time.sleep(2)