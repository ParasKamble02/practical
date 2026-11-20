import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt_tab')

text = "Natural Language Processing is interesting. Python makes NLP easy."

words = word_tokenize(text)
print("Word Tokenization:", words)

subwords = []
for w in words:
    if w.isalpha() and len(w) > 4:
        mid = (len(w) + 1) // 2
        subwords.extend([w[:mid] + "-", "-" + w[mid:]])
    else:
        subwords.append(w)
print("Sub-word Tokenization:", subwords)

print("Character Tokenization:", list(text.replace(" ", "")))

print("Sentence Tokenization:", sent_tokenize(text))