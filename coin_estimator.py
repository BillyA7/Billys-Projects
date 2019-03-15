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

weight_metric = input(
    'Please enter whether you want to submit the weight of your coins in grams or pounds.\n---> ').lower()
if weight_metric == 'grams':
    pennies, nickels, dimes, quarters = map(float, input(
        'Please enter the weight of your pennies, nickels, dimes and quarters.\n---> ').split())
elif weight_metric == 'pounds':
    coins = list(map(float, input(
        'Please enter the weight of your pennies, nickels, dimes and quarters.\n---> ').split()))
    pennies, nickels, dimes, quarters = [i * 453.59237 for i in coins]

penny_total, nickel_total, dime_total, quarter_total = int(
    pennies / 2.5), int(nickels / 5.0), int(dimes / 2.268), int(quarters / 5.67)

penny_wrapper, nickel_wrapper, dime_wrapper, quarter_wrapper = int(
    penny_total / 50), int(nickel_total / 40), int(dime_total / 50), int(quarter_total / 40)

total_value = [float(
    penny_total * 0.01), float(nickel_total * 0.05), float(dime_total * 0.1), float(quarter_total * 0.25)]


print(penny_total, nickel_total, dime_total, quarter_total)
print(penny_wrapper, nickel_wrapper, dime_wrapper, quarter_wrapper)
print(round(sum(total_value)))


# test