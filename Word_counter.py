# Read the content of the file
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split text into words using default whitespace separator
words = text.split()

# Count the number of words and characters
word_count = len(words)
character_count = len(text)


print(f"Total number of words: {word_count}")
print(f"Total number of characters: {character_count}")