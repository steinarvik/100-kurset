def remove_punctuation(text):
    punctuation = ".,!?:;'()[]{}"
    for char in punctuation:
        text = text.replace(char, "")
        return text

text = input("Enter a block of text for analysis\n")
characters = len(text)
words = len(text.split())
sentences = text.count(".") + text.count("!") + text.count("?")
word_frequency = {}

word_list = remove_punctuation(text).lower().split()

for word in word_list:
    if not word in word_frequency:
        word_frequency[word]=1
    else:
        word_frequency[word] += 1

lengths = {len(word) for word in word_list}
average_word_lenght = sum(lengths) / len(lengths)
average_sentence_lenght = words / sentences

print("\n")
print(word_frequency)
most_frequent_word = max(word_frequency, key=word_frequency.get)

print("Text analysis results")
print("-" * 20)
print(f"Total character: {characters}")
print(f"Antall ord: {words}")
print(f"Total sentences: {sentences}")
print(f"Most frequent word: {most_frequent_word} (used {word_frequency[most_frequent_word]} times).")
print(f"Average word length: {average_word_lenght}")
print(f"Average sentence length: {average_sentence_lenght} words")