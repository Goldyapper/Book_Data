from collections import defaultdict
import re

# Read the content of the file
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split text into words
words = re.findall(r'\b\w+\b', text.lower())

# Count the number of , words and characters
word_count = len(words)
character_count = len(text)

# Count paragraphs (non-empty blocks separated by empty lines)
paragraphs = [p for p in text.split('\n\n') if p.strip()]
paragraph_count = len(paragraphs)


def count_words_in_file(txt_file):
    
    word_count = defaultdict(int)

    for word in re.findall(r'\b\w+\b', text.lower()):
        word_count[word] += 1
    
    return dict(word_count)

word_counts = count_words_in_file(f)

# count the number of sentences
sentence_count = len(re.findall(r'[.!?]', text))

for word, count in word_counts.items():
    print(f"{word}: {count}")


print(f"Total number of paragraphs: {paragraph_count}")
print(f"Total number of sentences: {sentence_count}")
print(f"Total number of words: {word_count}")
print(f"Total number of characters: {character_count}")