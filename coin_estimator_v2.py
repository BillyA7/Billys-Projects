"""[Project] Coin Estimator By Weight When some people receive change after shopping, they put it into a container
and let it add up over time. Once they fill up the container, they'll roll them up in coin wrappers which can then be
traded in at a bank for what they are worth. While most banks will give away coin wrappers for free, it's convenient
to have an idea of how many you will need. Instead of counting how many coins you have, it's easier to separate all
of your coins, weigh them, and then estimate how many of each type you have and then how many wrappers you'll need.

For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have
about 563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.

Goal Create a program that allows the user to input the total weight of each type of coin they have (pennies,
nickels, dimes, and quarters), and then print out how many of each type of wrapper they would need, how many coins
they have, and the estimated total value of all of their money.

Sub goals

Round all numbers printed out to the nearest whole number.

Allow the user to select whether they want to submit the weight in either grams or pounds."""

# Coin weights
# ----------------------------------
# Cent (since 1983) - 2.500 g
# .
# Nickel (since 1866) - 5.000 g
# .
# Dime (since 1965) - 2.268 g
# .
# Quarter (since 1965) - 5.670 g
#
# Coin Wrapper Capacity
# -----------------------------------
# Penny or 1 Cent	50	$0.50
# Nickel or 5 Cents	40	$2.00
# Dime or 10 Cents	50	$5.00
# Quarter or 25 Cents	40	$10.00

# Pounds-grams-grams-pounds formula
# -----------------------------------
# pounds = grams * 0.002205
# grams = pounds * 453.59237


class Coin:
    def __init__(self, weight, value, wrapper):
        self.weight = weight
        self.value = value
        self.wrapper = wrapper


class Penny(Coin):
    def __init__(self):
        super().__init__(2.5, 0.01, 50)


class Nickel(Coin):
    def __init__(self):
        super().__init__(5.0, 0.05, 40)


class Dime(Coin):
    def __init__(self):
        super().__init__(2.268, 0.1, 50)


class Quarter(Coin):
    def __init__(self):
        super().__init__(5.67, 0.25, 40)


print('- - - - - - - - - - - - - - - - - - ')
print('Welcome to the coin estimator!')
print('- - - - - - - - - - - - - - - - - - \n')

weight = input('Are you submitting the weight of your coins in grams or pounds?\n--->').lower()

pennies = float(input('Please enter the weight of your pennies:\n--->')) / Penny().weight
nickels = float(input('Please enter the weight of your nickels:\n--->')) / Nickel().weight
dimes = float(input('Please enter the weight of your dimes:\n--->')) / Dime().weight
quarters = float(input('Please enter the weight of your quarters:\n--->')) / Quarter().weight

if weight == 'pounds':
    pennies *= 453.59237
    nickels *= 453.59237
    dimes *= 453.59237
    quarters *= 453.59237


total_value = [pennies * Penny().value, nickels * Nickel().value,
               dimes * Dime().value, quarters * Quarter().value]

total_wrappers = {'Pennies': pennies / Penny().wrapper, 'Nickels': nickels / Nickel().wrapper,
                  'Dimes': dimes / Dime().wrapper, 'Quarters': quarters / Quarter().wrapper}

print(f'You need {int(total_wrappers["Pennies"])} wrappers for your {int(pennies)} pennies')
print(f'You need {int(total_wrappers["Nickels"])} wrappers for your {int(nickels)} nickels')
print(f'You need {int(total_wrappers["Dimes"])} wrappers for your {int(dimes)} dimes')
print(f'You need {int(total_wrappers["Quarters"])} wrappers for your {int(quarters)} quarters\n')

print(f'You have an esitmated ${int(sum(total_value))}.\n')
