import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('stopwords')
nltk.download('punkt')  # segmentation phrases
nltk.download('averaged_perceptron_tagger')  # étiquettes grammaticales
nltk.download('wordnet')  # synonymes


def remove_stopwords(word_list):
    stop_words = set(stopwords.words('english'))
    filtered_words = []
    for word in word_list:
        if word not in stop_words:
            filtered_words.append(word)
    return filtered_words


def get_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV,
                "J": wordnet.ADJ}
    return tag_dict.get(tag, wordnet.NOUN)


def lemmatize_words(word_list):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word, get_pos(word))
                        for word in word_list]
    return lemmatized_words


def preprocess_text(preprocess_sentence):

    preprocess_sentence = re.sub(r'\S*@\S*\s?', '', preprocess_sentence)
    preprocess_sentence = re.sub(r'http\S+', '', preprocess_sentence)
    preprocess_sentence = re.sub(r'[^\w\s]', '', preprocess_sentence)
    preprocess_sentence = re.sub(r'\b\w\b', '', preprocess_sentence)
    preprocess_sentence = re.sub(r'\d', '', preprocess_sentence)
    preprocess_sentence = re.sub(r'\s+', ' ', preprocess_sentence)
    preprocess_sentence = preprocess_sentence.lower()
    preprocess_sentence = nltk.word_tokenize(preprocess_sentence)
    preprocess_sentence = remove_stopwords(preprocess_sentence)
    preprocess_sentence = lemmatize_words(preprocess_sentence)
    preprocess_sentence = ' '.join(preprocess_sentence)
    return preprocess_sentence
