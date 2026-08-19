# word_counter.py
text = input("Enter your text: ")

words = text.split()
word_count = len(words)
char_count = len(text)
char_count_no_space = len(text.replace(" ", ""))

print(f"\nTotal Words: {word_count}")
print(f"Total Characters: {char_count}")
print(f"Characters without spaces: {char_count_no_space}")