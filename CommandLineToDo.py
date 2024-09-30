from datetime import datetime

todo_items = []

while True:
    todo = input("Enter youre to-do items for today. Type 'done' to save and exit.")
    if todo == 'done':
        break
    todo_items.append(todo)


day = datetime.now().strftime("%A")
print(day)
filename = f'{day}.txt'
print(filename)

content = "\n".join(todo_items)

with open(filename, "w") as file:
    file.write(content)

print(f"Youre to-do list was saves as {filename}")