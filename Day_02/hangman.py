import random 
word_list = ["ardvark", "baboon", "camel"] # intial list of words
chosen_word = random.choice(word_list)
guess = input("Choose a random letter:").lower() # guessing a letter
word_length = len(chosen_word)
display = []
print(f"Psst, the chosen word is {chosen_word} ")  # help us see the word
for _ in range(word_length):
    display += "_"
print(display)
#for letter in chosen_word: # older version, kept for clarily of how it works.
#    if letter == guess:
#        print("Right")
#    else:
#       print("Wrong")
    
for position in range(word_length): # check the range of word length, letter is checked for current position, if letter is correct, the blank gets replaced by the letter
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)


# -----------------


#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# 1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You WIN!!!")




