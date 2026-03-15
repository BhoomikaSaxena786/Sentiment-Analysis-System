import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from preprocess import clean_text
import pickle
# from sklearn.metrics import classification_report, confusion_matrix


# Load data :- read krega csv file 
data = pd.read_csv("reviews.csv")

# Clean text
data['review'] = data['review'].apply(clean_text)

# Split input and output
X = data['review']
y = data['sentiment']

# Convert text to numbers
# vectorizer = TfidfVectorizer(stop_words='english')
# vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2) ,max_features=100)
cv = TfidfVectorizer(ngram_range=(1, 2)) 
X = cv.fit_transform(df['review'])

# X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
# Save model and vectorizer
pickle.dump(model, open("sentiment_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))






















































# I used TF-IDF to convert text into numerical features and trained a Logistic Regression model using scikit-learn.

# print(classification_report(y_test, predictions))
# print(confusion_matrix(y_test, predictions))