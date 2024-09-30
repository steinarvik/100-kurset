from datetime import datetime

diary_items = []

while True:
    note = input("Enter youre notes for today. Type 'exit' to save and exit.")
    if note == 'exit':
        break
    diary_items.append(note)


day = datetime.now().strftime("%Y-%m-%d")
print(day)
filename = f'{day}.txt'
print(filename)

content = "\n".join(diary_items)

with open(filename, "w") as file:
    file.write(content)

print(f"Youre notes have been saved to {filename}")