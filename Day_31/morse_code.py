# You will use what you've learnt to create
# a text-based (command line) program that takes any String input and
# converts it into Morse Code.

# Imports the key from the key.py file
from key import key


# ask for input() from the user, convert it into lowercase
morse_input = input("What would you like to translate to morse?: ").lower()

# use those letters to find corresponding code from key.py using map function,
# join using spaces in between each code
morse = ' '.join(map(key.get, morse_input))

# print the morse code
print(f"You input '{morse_input}' to translate into morse. \nIt translates to the following in "
      f"morse code: \n{morse}\nNOTE: The morse code is not case sensitive")


# potential additions:
# add a text input using turtle
# make a GUI for the entire program.
# make a function to translate everything, the morse variable could be a function.
