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