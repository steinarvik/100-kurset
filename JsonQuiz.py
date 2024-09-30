import requests

url = "https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json"
response = requests.get(url)
quiz_data = response.json()

# Ask the user for the question ID
question_id = int(input("enter the question ID: "))

# Initialize variables to track the correct answer and whether the question was found
correct_answer = None
question_found = False

# Find and print the correct answer
for quiz in quiz_data["quizzes"]:
    for question in quiz["questions"]:
        if question["id"] == question_id:
            print("funnet")
            question_found = True
            for choice, is_correct in question["choices"].items():
                if is_correct:
                    correct_answer = choice

if question_found:
    if correct_answer:
        print(f"The correct answer is: {correct_answer}")
    else:
        print("No correct answer found for the given question ID.")
else:
    print("Question ID not found.")