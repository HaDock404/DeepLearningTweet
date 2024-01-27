# Analyse_exploratoire/preprocessing

```python
data = data.rename(columns={data.columns[0]: 'target'})
data = data.rename(columns={data.columns[1]: 'id'})
data = data.rename(columns={data.columns[2]: 'date'})
data = data.rename(columns={data.columns[3]: 'flag'})
data = data.rename(columns={data.columns[4]: 'user'})
data = data.rename(columns={data.columns[5]: 'text'})
```
Remplacement des noms des colonnes  

```python
data['text'] = data['text'].apply(lambda x: re.sub(r'\S*@\S*\s?', '', x))
data['text'] = data['text'].apply(lambda x: re.sub(r'http\S+', '', x))
data['text'] = data['text'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
data['text'] = data['text'].apply(lambda x: re.sub(r'\b\w\b', '', x))
data['text'] = data['text'].apply(lambda x: re.sub(r'\d', '', x))
data['text'] = data['text'].apply(lambda x: re.sub(r'\s+', ' ', x))
data['text'] = data['text'].apply(lambda x: x.lower())
```
Suppression des valeurs inutiles dans le texte :
- suppression du nom de l'utilisateur ex. @user123
- suppression des liens ex. https://www.google.com
- suppression de tous les caractères non alphanumériques (symboles, ponctuations)
- suppression des lettres seuls dans le texte ex. L
- suppression des caractères numériques ex. 9
- suppression des doubles espaces
- transformation de tous les caractères en minuscule  

```python
data['text_token'] = 0

for i in range(len(data['text'])):
    data['text_token'][i] = nltk.word_tokenize(data['text'][i])
```
Tokenisation des mots du Dataframe pour pouvoir effectuer des opérations dessus ensuite.  
Les mots seront dé-tokenisé par la suite. Cette opération est nécessaire pour utiliser remove_stopwords().  

```python
nltk.download('stopwords')

def remove_stopwords(word_list):
    stop_words = set(stopwords.words('english'))
    filtered_words = []
    for word in word_list:
        if word not in stop_words:
            filtered_words.append(word)
    return filtered_words

for i in range(len(data['text_token'])):
    data['text_token'][i] = remove_stopwords(data['text_token'][i])
```
Suppression de tous les stops words du texte à partir de la liste fournie par `nltk`.
La fonction remove_stopwords() boucle sur tous les mots de chaque individu du Dataframe et les compares à la liste de stopWords et supprime les mots qui correspondent à la liste.

```python
nltk.download('punkt')# segmentation phrases
nltk.download('averaged_perceptron_tagger') # étiquettes grammaticales
nltk.download('wordnet')# synonymes

def lemmatize_words(word_list):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word, get_pos(word)) for word in word_list]
    return lemmatized_words

def get_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV, "J": wordnet.ADJ}
    return tag_dict.get(tag, wordnet.NOUN)

for i in range(len(data['text_token'])):
    data['text_token'][i] = lemmatize_words(data['text_token'][i])
```  
Lemmatization des mots du Dataframe. On retrouve la racine des mots en supprimants la conjugaison, le pluriel, ou le féminin des mots.  

```python
array_list = df['text_token'].values
data_list = []
for item in array_list:
    data_list.append(ast.literal_eval(item))

df_list = pd.DataFrame({'text_token': data_list})
df = df.drop(columns=['text_token'])
df['text_token'] = df_list['text_token']
df['words'] = df['text_token'].apply(lambda x: ' '.join(x))
df = df.drop(columns=['text_token'])
```  
Suppression de la tokenisation des mots.