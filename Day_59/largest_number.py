# Implement a function that takes as input three variables, and returns the largest of the three. Do this without
# using the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need
# is some variables and if statements!


def largest(a, b, c):
    if a > b and a > c:
        print(f"Maximum Value is  {a}")
    elif b > c and b > a:
        print(f"Maximum Value is {b}")
    elif c > b and c > a:
        print(f"Maximum Value is {c}")


largest(31, 9, 17)
