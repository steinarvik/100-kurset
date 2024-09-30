import random

# List of words to guess from
words = ["python", "java", "swift", "javascript", "ruby"]

# Randomly select a word from the list
word_to_guess = random.choice(words)
max_attempts = 6
attempts = 0

print("Welcome to the Word Guessing Game!")
print("I have selected a word from a list of programming languages.")
print(f"You have {max_attempts} attempts to guess the correct word.")

# Start the guessing loop
for i in range(max_attempts):
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if len(guess) < len(word_to_guess):
        print(f"Your guess is shorter than the correct word. Try again.")
    elif len(guess) > len(word_to_guess):
        print(f"Your guess is longer than the correct word. Try again.")
    elif guess != word_to_guess:
        print("The length is correct, but the word is not. Try again.")
    else:
        print(f"Congratulations! You've guessed the correct word '{word_to_guess}' in {attempts} attempts.")
        break

else:
    print(f"Sorry, you've used all {max_attempts} attempts. The correct word was '{word_to_guess}'.")


