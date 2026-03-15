import pickle
from preprocess import clean_text

# Load saved model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_sentiment(text):
    text = clean_text(text)
    vector = vectorizer.transform([text])
    result = model.predict(vector)[0]
    return "Positive" if result == 1 else "Negative"


# Test prediction
print(predict_sentiment("I really love this product"))
print(predict_sentiment("This is the worst experience"))
print(predict_sentiment("so bad"))
print(predict_sentiment("Oops never buy again"))
print(predict_sentiment("I like it"))
print(predict_sentiment("I definitely buy"))




