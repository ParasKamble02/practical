import spacy

nlp = spacy.load("en_core_web_lg")

text = "Sachin Tendulkar lives in Mumbai and works with Microsoft"
doc = nlp(text)

print("Content:", text)
print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)