# Sentiment Analysis System

A **Machine Learning based web application** that analyzes text reviews and predicts whether the sentiment is **Positive** or **Negative**. The system uses **Natural Language Processing (NLP)** techniques and a trained machine learning model to classify user input in real time.

---

## Project Overview

This project demonstrates how **Machine Learning and NLP** can be used to automatically analyze customer opinions or product reviews.
The model is trained on a dataset of text reviews and then integrated into a **Flask web application** where users can enter their own text and check the sentiment.

---

## Features

* Real-time sentiment prediction
* Machine learning model trained on review data
* Text preprocessing and feature extraction
* Web interface for user input
* Positive or Negative sentiment classification
* Fast and lightweight prediction system

---

## Technologies Used

### Programming Language

* Python

### Libraries & Tools

* Flask
* Scikit-learn
* Pandas
* NLTK
* Pickle

### Machine Learning Techniques

* TF-IDF Vectorization
* Logistic Regression / Naive Bayes

---

## Project Structure

Sentiment-Analysis-System
│
├── app.py                  # Flask web application
├── train_model.py          # Script used to train the ML model
├── preprocess.py           # Text preprocessing functions
├── predict.py              # Sentiment prediction logic
├── reviews.csv             # Dataset used for training
├── sentiment_model.pkl     # Trained machine learning model
├── vectorizer.pkl          # TF-IDF vectorizer

│
├── templates
│   └── index.html          # Web interface

│
└── README.md               # Project documentation

---

## How the System Works

1. The dataset of reviews is loaded.
2. Text preprocessing is applied (removing punctuation, stopwords, etc.).
3. TF-IDF vectorization converts text into numerical features.
4. A machine learning model is trained on the dataset.
5. The trained model and vectorizer are saved using Pickle.
6. Flask loads the trained model and predicts sentiment for user input.

---

## How to Run the Project

### 1. Clone the Repository

git clone https://github.com/BhoomikaSaxena786/Sentiment-Analysis-System.git

### 2. Navigate to the Project Folder

cd Sentiment-Analysis-System

### 3. Install Required Libraries

pip install -r requirements.txt

### 4. Run the Application

python app.py

### 5. Open in Browser

http://127.0.0.1:5000

Enter a text review and the system will predict whether it is **Positive or Negative**.

---

## Example

Input:

This product is amazing and works perfectly!

Output:

Positive Sentiment

---

## Future Improvements

* Add Neutral sentiment category
* Improve model accuracy using larger datasets
* Deploy the application online
* Enhance UI design
* Implement deep learning models like LSTM or BERT

---

## Author

Bhoomika Saxena

B.Tech (CSE - AI)
ABES Institute of Technology

GitHub
https://github.com/BhoomikaSaxena786

LinkedIn
https://www.linkedin.com/in/bhoomika-saxena-2aaab72a4/

Portfolio
https://bhoomikasaxena786.github.io/Portfolio_website/

