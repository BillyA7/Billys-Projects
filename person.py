from datetime import datetime, date


class Person:

    # creates Person class and common attributes
    def __init__(self, name, birth_date, birth_town, height, weight):
        self.name = name
        self.birth_date = birth_date
        self.birth_town = birth_town
        self.height = height
        self.weight = weight
        

    # quick method to introduce a person
    def introduce_yourself(self):
        return f'Hello, my name is {self.name} and I was born in {self.birth_town} on the {self.birth_date}.'


    # a method to calculate the age of the person
    def age_person(self):
        # converts string to datetime object
        dob = datetime.strptime(self.birth_date, "%d %m %Y")
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 
    

billy = Person('Billy', '03 09 1981', 'Doncaster', '5ft 11', '15st')

print(billy.introduce_yourself())

print(f'I am {billy.age_person()} years old, {billy.height} and weigh {billy.weight}')
