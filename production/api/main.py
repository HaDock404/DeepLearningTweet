from flask import Flask
from flask import render_template
from flask import request
import joblib
from cleaning import preprocess_text
import os

app = Flask(__name__)


@app.route('/', methods=["Get", "POST"])
def home():
    return render_template("index.html")


@app.route('/predict', methods=["Get", "POST"])
def predict_sentence():
    user_input = request.form['X_test']

    vectorizer_path = os.path.join("production/api/models",
                                   "vectorizer.pkl")

    with open(vectorizer_path, 'rb') as vec_file:
        vectorizer = joblib.load(vec_file)

    preprocess_sentence = user_input

    preprocess_sentence = preprocess_text(preprocess_sentence)
    preprocess_sentence = vectorizer.transform([preprocess_sentence])

    model_path = os.path.join("production/api/models",
                              "model.pkl")

    with open(model_path, 'rb') as model_file:
        classifier = joblib.load(model_file)

    predictions_test = classifier.predict(preprocess_sentence)
    if predictions_test == 1:
        print_result = '<div class="result">\
                            Le sentiment de ce texte est \
                                : <strong class="green">POSITIF</strong>\
                        </div>'
    elif predictions_test == 0:
        print_result = '<div class="result">\
                            Le sentiment de ce texte est \
                                : <strong class="red">NEGATIF</strong>\
                        </div>'

    return print_result


if __name__ == '__main__':
    app.run(debug=True, port=5002)
