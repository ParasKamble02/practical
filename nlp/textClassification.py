from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = ["I love this product", "worst thing ever",
         "Amazing experience", "Terrible waste of money"]
labels = ["positive", "negative", "positive", "negative"]

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(texts, labels)

print(model.predict(["I didn't really enjoy it"]))

