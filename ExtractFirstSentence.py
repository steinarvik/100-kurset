import os
import re

directory = "text"
all_first_sentences = []

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as file:
        content = file.read()

        # Use regular expression to find all sentences
        pattern = r'[A-Za-z0-9,;"\'\s\-()]+[.!?]'
        first_sentences = re.findall(pattern, content)

        # Add the first sentence from the match to the list if available
        all_first_sentences.append(first_sentences[0])

    # Print all first sentences one in each line
    for sentence in all_first_sentences:
        print(sentence)

