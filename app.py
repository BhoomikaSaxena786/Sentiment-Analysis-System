from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# 1. Model aur Vectorizer load karna (Yeh 'Serialization' ka part hai)
try:
    model = pickle.load(open('sentiment_model.pkl', 'rb'))
    cv = pickle.load(open('vectorizer.pkl', 'rb'))
    print("Success: Model Loaded!")
except:
    print("Error: Files not found! Check your pkl file names.")

@app.route('/')
def home():
    # Pehli baar page khulne par index.html dikhayega
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # HTML form se 'review' naam ka data lena
        user_input = request.form.get('review')
        
        if user_input:
            # Step 1: Text ko TF-IDF format mein badalna
            data = [user_input]
            vect = cv.transform(data).toarray()
            
            # Step 2: Prediction karna (1 = Positive, 0 = Negative)
            prediction = model.predict(vect)
            result = int(prediction[0])
            
            # Step 3: Result ke saath wapas page refresh karna
            return render_template('index.html', prediction_text=result, original_text=user_input)
            
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)