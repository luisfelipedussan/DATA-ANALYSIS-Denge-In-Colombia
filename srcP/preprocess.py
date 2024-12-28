import nltk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Descargar recursos de NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Preprocesamiento de texto
def preprocess_text(text):
    # Convertir a minúsculas
    text = text.lower()
    # Tokenización
    tokens = word_tokenize(text)
    # Eliminar puntuación y palabras vacías
    tokens = [word for word in tokens if word not in string.punctuation and word not in stopwords.words('english')]
    return ' '.join(tokens)

# Cargar el dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    # Suponemos que el dataset tiene 'text' y 'label' como columnas
    df['text'] = df['text'].apply(preprocess_text)
    return df

# Dividir el dataset en entrenamiento y prueba
def split_data(df):
    X = df['text']
    y = df['label']
    le = LabelEncoder()
    y = le.fit_transform(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

