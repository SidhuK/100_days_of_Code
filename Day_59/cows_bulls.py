# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
# tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.

# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.
import random


def cowbulls(random_number, guessed_number):
    cowbull = [0, 0]  # 0 cows, 0 bulls initially
    for i in range(len(random_number)):
        if random_number[i] == guessed_number[i]:
            cowbull[1] += 1
        else:
            cowbull[0] += 1
    return cowbull


if __name__ == "__main__":
    still_playing = True
    rand_number = str(random.randint(1000, 9999))
    guesses = 0

    print("Let's play a game of Cowbull!")  # explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while still_playing:
        user_number = input("What is your guess? : ")
        if user_number == "exit":
            break

        cowbull_count = cowbulls(rand_number, user_number)
        guesses += 1

        print("You have " + str(cowbull_count[0]) + " cows, and " + str(cowbull_count[1]) + " bulls.")

        if cowbull_count[1] == 4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was " + str(rand_number))
            break  # redundant exit
        else:
            print("Your guess isn't quite right, try again.")


# rand_number = list(map(int, str(random.randint(1000, 9999))))
# print(f"The randomly generated number is  {rand_number}")
# number_enter = list(map(int, str(int(input("Enter a 4 Digit Number: ")))))
# number = []
#
# for number in random_number and number in number_enter:
#     if random_number.index(number) == number_enter.index(number):
#         print("cow")
#     else:
#         print("bull")
