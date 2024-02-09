from flask import Flask
from flask import render_template
from flask import request
import joblib
from preprocess import preprocess_text

app = Flask(__name__)


@app.route('/', methods=["Get", "POST"])
def home():
    return render_template("index.html")


@app.route('/predict', methods=["Get", "POST"])
def predict_sentence():
    user_input = request.form['X_test']

    with open("./models/vectorizer.pkl", 'rb') as vec_file:
        vectorizer = joblib.load(vec_file)

    preprocess_sentence = user_input

    preprocess_sentence = preprocess_text(preprocess_sentence)
    preprocess_sentence = vectorizer.transform([preprocess_sentence])

    with open("./models/model.pkl", 'rb') as model_file:
        classifier = joblib.load(model_file)

    predictions_test = classifier.predict(preprocess_sentence)
    if predictions_test == 1:
        print_result = 'positif'
    elif predictions_test == 0:
        print_result = 'negatif'

    return print_result


if __name__ == '__main__':
    app.run(debug=True, port=5002)
