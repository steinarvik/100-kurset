import random

number_to_guess = random.randint(1, 100)
max_attempts = 10
attempts = 0

print("Welcome to ...")
print("I have chosen a number beteen 1 and 100")
print(f"You have {max_attempts} attemps to guess that number.")

for i in range(max_attempts):
    guess = int(input("Enter youre choice:"))
    attempts += 1

    if guess < number_to_guess:
        print("Too low. Try again!")
    elif guess > number_to_guess:
        print("Too high. Try again!")
    else:
        print(f"Congratualation! You guessed right in {attempts} attempts.")
        break


else:
    print(f"Sorry, you have used all {max_attempts} attempts. The correct number was {number_to_guess}.")