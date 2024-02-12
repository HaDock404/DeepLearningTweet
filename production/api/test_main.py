import unittest
import os
import joblib
from cleaning import preprocess_text


class TestApp(unittest.TestCase):

    def test_preprocess_text(self):
        input_text = "@switchfoot http://twitpic.com/2y1zl - \
            Awww, that's a bummer. You shoulda got David Carr of \
                Third Day to do it. ;D 1"
        expected_output = "awww thats bummer shoulda get david carr third day"
        result = preprocess_text(input_text)
        self.assertEqual(result, expected_output)

    def test_predict_sentence_positive(self):
        vectorizer_path = os.path.join("production/api/models",
                                       "vectorizer.pkl")
        with open(vectorizer_path, 'rb') as vec_file:
            vectorizer = joblib.load(vec_file)
        preprocess_sentence = 'Hello how are you ?'
        preprocess_sentence = preprocess_text(preprocess_sentence)
        preprocess_sentence = vectorizer.transform([preprocess_sentence])
        model_path = os.path.join("production/api/models",
                                  "model.pkl")
        with open(model_path, 'rb') as model_file:
            classifier = joblib.load(model_file)
        predictions_test = classifier.predict(preprocess_sentence)
        self.assertEqual(predictions_test, 1)

    def test_predict_sentence_negative(self):
        vectorizer_path = os.path.join("production/api/models",
                                       "vectorizer.pkl")
        with open(vectorizer_path, 'rb') as vec_file:
            vectorizer = joblib.load(vec_file)
        preprocess_sentence = 'I am angry'
        preprocess_sentence = preprocess_text(preprocess_sentence)
        preprocess_sentence = vectorizer.transform([preprocess_sentence])
        model_path = os.path.join("production/api/models",
                                  "model.pkl")
        with open(model_path, 'rb') as model_file:
            classifier = joblib.load(model_file)
        predictions_test = classifier.predict(preprocess_sentence)
        self.assertEqual(predictions_test, 0)


if __name__ == '__main__':
    unittest.main()

# python3 production/api/test_main.py -v
