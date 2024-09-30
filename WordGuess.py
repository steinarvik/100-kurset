words = ["python", "java", "swift", "javascript", "ruby"]
no_of_attempts = 0


print("Welcome to the word guessing game")
print("I have selected a word")
print("You have 6 attempts")

for i in range(1, 6):
    your_guess = input("Enter you're guess:").strip()
    print(your_guess)
    no_of_attempts +=1
    print(no_of_attempts)
    print(i)
    if no_of_attempts == 6:
        break
    if your_guess in words:
        print("Funnet!")
        break


print("antall forsøk", no_of_attempts)
