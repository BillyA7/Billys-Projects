'''[PROJECT] 99 Bottles of Beer On the Wall Lyrics

GOAL

Create a program that prints out every line to the
song "99 bottles of beer on the wall."

This should be a pretty simple program,
so to make it a bit harder, here are some rules to follow.

RULES

If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.

Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.

Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

Put a blank line between each verse of the song.'''

# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.


for bottles in reversed(range(0, 100)):
    if bottles > 1:
        print(bottles, 'bottles of beer on the wall,', bottles, 'bottles of beer.')
        if bottles - 1 > 1:
            print('Take one down and pass it around,', bottles - 1, 'bottles of beer on the wall.\n')
        else:
            print('Take one down and pass it around,', bottles - 1, 'bottle of beer on the wall.\n')
    elif bottles == 1:
        print(bottles, 'bottle of beer on the wall,', bottles, 'bottle of beer.')
        print('Take one down and pass it around,', bottles - 1, 'bottles of beer on the wall.\n')
    else:
        print('No more bottles of beer on the wall, no more bottles of beer. ')
        print('Go to the store and buy some more,', bottles + 99, 'bottles of beer on the wall.')
