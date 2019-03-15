class Car:

    def __init__(self, make, model, year, colour, doors, transmission, fuel_type, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.doors = doors
        self.transmission = transmission
        self.fuel_type = fuel_type
        self.mileage = mileage


    def describe_car(self):
        return f'The car is a {self.year} {self.make} {self.model} in {self.colour}. It has {self.doors} doors, a {self.transmission} transmission, runs on {self.fuel_type} and has done {self.mileage} miles.'

    def car_journey(self, miles_travelled):
        self.mileage += miles_travelled

# audis = [Car('Audi', 'RS4', '2006', 'Phantom Black', 5, 'manual', 'petrol', 52524) for cars in range(5)]

rs4 = Car('Audi', 'RS4', '2006', 'Phantom Black', 5, 'manual', 'petrol', 52524)

veyron = Car('Bugatti', 'Veyron', '2010', 'Carbon Fibre', 3, 'DSG', 'petrol', 1157)

print(rs4.describe_car())

rs4.car_journey(10000)

print(rs4.describe_car())

print(veyron.describe_car())