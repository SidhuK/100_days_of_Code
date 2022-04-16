# Exercise
# Implement the same exercise as Exercise 1 (Create a program that asks the
# user to enter their name and their age. Print out a message addressed to them
# that tells them the year that they will turn 100 years old), except use f-strings
# instead of the + operator to print the resulting output message.

name = input("What is your name? : ")
age_right_now = int(input("What is your age? : "))

print(f"Hello {name}, you are {age_right_now} years old now, so "
      f"it looks like you will turn 100 years old in another {100 - age_right_now} years")

