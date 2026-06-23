import random

# Predefined list of words
words = ["apple", "banana", "orange", "grape", "melon"]

# Choose a random word from the list
word = random.choice(words)
# Create a display list with underscores for each letter
display = ['_'] * len(word)

# Limit for incorrect guesses
max_incorrect = 6
incorrect_guesses = 0

# Set of guessed letters to avoid repeats
guessed_letters = set()

print("Welcome to Hangman!")

while incorrect_guesses < max_incorrect and '_' in display:
    print("\nCurrent word: " + ' '.join(display))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
    guess = input("Guess a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        # Reveal the guessed letter in the display
        for idx, letter in enumerate(word):
            if letter == guess:
                display[idx] = guess
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check if the player has won or lost
if '_' not in display:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame over! The word was: {word}")