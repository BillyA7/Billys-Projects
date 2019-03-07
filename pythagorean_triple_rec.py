'''[PROJECT] Pythagorean Triples Checker
BACKGROUND INFORMATION

If you do not know how basic right triangles work, read wikipedia.

MAIN GOAL

Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean Triple or not.

SUBGOALS

If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides in any order. Remember, the hypotenuse (c) is always the longest side.

Loop the program so the user can use it more than once without having to restart the program.'''

import sys


def pythagorean_triple():
    try:
        nums = list(
            map(int, input('Please enter 3 whole positive numbers seperated by spaces.\n\nOr press enter to quit\n>').split()))
    except ValueError:
        print('Incorrect input, please try again.\n')
        pythagorean_triple()
    if len(nums) in range(1, 3):
        print('Incorrect input, please try again.\n')
        pythagorean_triple()
    elif not len(nums):
        print('Goodbye')
        sys.exit(0)
    else:
        nums.sort()
        a, b, c = [x**2 for x in nums]
        if a + b != c:
            print('Not a Pythagorean Triple')
            pythagorean_triple()
        else:
            print('Woohoo a Pythagorean Triple')
            pythagorean_triple()


pythagorean_triple()
