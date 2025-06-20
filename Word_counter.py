# Read the content of the file
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

line_count = 0

# Split text into words using default whitespace separator
words = text.split()

# Count the number of lines, words and characters
word_count = len(words)
character_count = len(text)


Content_List = text.split("\n")
for i in Content_List:
    if i:
        line_count += 1

print(f"Total number of lines: {line_count}")
print(f"Total number of words: {word_count}")
print(f"Total number of characters: {character_count}")