import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

sentence = "The intelligent student writes python code efficiently."

words = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(words)

print("Input sentence:", sentence)
print("Parts-of-Speech Tags:")

for word, tag in tagged_words:
    print(f"Word: {word:15} -> {tag}")