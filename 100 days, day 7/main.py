## Day 7 - Revving previous concepts
"""
For and while loops
if/else
lists
strings
Range function
"""
# 53 Video : flowchart/explanation

## 54 Step 1 - Picking a Random Words and Checking Answers
"""
import random

word_list = ["snowhite","barbie","batman","snowden"]

word = random.choice(word_list)

blank = []
for i in range(0,len(word),1):
    blank.append("_")

print(list(word))
print(blank)

ug = str(input("Enter your guess :")).lower()
"""
"""
for letter in word:
    if letter == ug:
        print("Right")
    else:
        print("Wrong")

##55 Replacing the Blanks with the guesses

# Create a display that puts the guess letter in the right positions and _

# extending the for loop

display = ""

for letter in word:
    if letter == ug:
        display += letter
    else:
        display += "_"

print(display)

## Step 3 checking if a player wins

game_over = False

while not game_over:
    ug = str(input("Enter your guess :")).lower()

    display = ""

    for letter in word:
        if letter == ug:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")

"""

import random

# List of words to guess
word_list = ["python", "java", "hangman", "programming", "developer"]

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a display with underscores
display = ["_"] * word_length

# Game variables
lives = 6  # Number of wrong attempts allowed
guessed_letters = set()

print("Welcome to Hangman!")

while "_" in display and lives > 0:
    print("\n" + " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for index in range(word_length):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        print(f"Wrong guess! You lose a life. Lives left: {lives - 1}")
        lives -= 1

# Game result
if "_" not in display:
    print(f"\nCongratulations! You guessed the word: {chosen_word}")
else:
    print(f"\nGame over! The word was: {chosen_word}")

### at line 102 the idea of doing replacing it through the index values plays a satisying role