from collections import defaultdict
import re
import matplotlib.pyplot as plt

Stopwords = {
    "a", "an", "the", "and", "or", "but", "if", "while", "with", "without", "to", "of", "in", "on", "at",
    "for", "from", "by", "about", "as", "is", "was", "were", "are", "be", "been", "being", "this", "that",
    "these", "those", "it", "its", "i", "you", "he", "she", "we", "they", "them", "his", "her", "their",
    "my", "mine", "our", "your", "yours", "me", "us", "do", "does", "did", "have", "has", "had", "not",
    "so", "no", "yes", "can", "will", "would", "could", "should", "shall", "just", "it's", "i'm", "you're",
    "he's", "she's", "we're", "they're", "there", "here", "up", "down", "out", "over", "under", "him"
}


def count_words_in_file():
    
    word_count = defaultdict(int)

    for word in re.findall(r"\b[\w'`’]+\b", text.lower()):
        word_count[word] += 1
    return dict(word_count)


def filter_stopwords(word_counts):
    return {word: count for word, count in word_counts.items() if word not in Stopwords}


# Read the content of the file
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split text into words
words = re.findall(r"\b[\w'`’]+\b", text.lower())


# Count the number of , words and characters
word_count = len(words)
character_count = len(text)

# Count paragraphs (non-empty blocks separated by empty lines)
paragraphs = [p for p in text.split('\n\n') if p.strip()]
paragraph_count = len(paragraphs)

word_counts = count_words_in_file()

# count the number of sentences
sentence_count = len(re.findall(r'[.!?]', text))

word_counts_desc = sorted(word_counts.items(), key=lambda item: item[1],reverse=True)
top_20_words_desc = sorted(word_counts_desc[:20])
top_20_asc = sorted(top_20_words_desc, key=lambda item: item[1])  

filtered_counts = filter_stopwords(word_counts)
top_10_filtered = sorted(filtered_counts.items(), key=lambda item: item[1], reverse=True)[:10]
top_nonstop_asc = sorted(top_10_filtered, key=lambda item: item[1])

print("Top 20 words:")
for word, count in top_20_asc:
    print(f"{word}: {count}")

print("Top 10 non-stop words:")
for word, count in top_nonstop_asc:
    print(f"{word}: {count}")

print(f"Total number of paragraphs: {paragraph_count}")
print(f"Total number of sentences: {sentence_count}")
print(f"Total number of words: {word_count}")
print(f"Total number of characters: {character_count}")

sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True) [:50]
# Separate words and counts
words, counts = zip(*sorted_words)

plt.figure(figsize=(16, 8))
plt.bar(words, counts, color='blue')
plt.xlabel('Frequency')
plt.title('All Words by Frequency')
plt.xticks(rotation=90)  
plt.tight_layout()
plt.show()