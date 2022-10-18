'''
        Universidad del valle de Guatemala
        Laboratorio 9. DS
        Visualizaciones interactivas con Dash

        Andres Quinto
        Andree Toledo
'''

from _plotly_utils.basevalidators import TitleValidator
from dash.dcc.Graph import Graph
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
from nltk.util import ngrams
import re
import string
import emoji
import numpy as np
from dash import Dash, dcc, html, Input, Output
import random
import warnings
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

def normalize_data(data):
    _max = 0
    for i in data:
        if(_max<len(i)):
            _max=len(i)
    for i in data:
        while (_max>len(i)):
            i.append(" ") 
    return (data)


app = Dash(__name__)

# Import and clean data

tweet_frequency = pd.read_csv('tweet_count.csv')
blogs_frequency = pd.read_csv('blogs_count.csv')
news_frequency = pd.read_csv('news_count.csv')

# Open TXT files
# en_us_test = open('test.txt', "r")
en_us_blogs = open('test.txt', "r", encoding="utf8") # CHANGE THE NAME OF TXT FILES FOR THE CORRECT ONE
en_us_news = open('test.txt', "r", encoding="utf8")
en_us_twitter = open('test.txt', "r", encoding="utf8")

# Read TXT files
# en_us_test_text = en_us_test.readlines()
en_us_blogs_text = en_us_blogs.readlines()
en_us_news_text = en_us_news.readlines()
en_us_twitter_text = en_us_twitter.readlines()

# Close TXT Files
# en_us_test.close()
en_us_blogs.close()
en_us_news.close()
en_us_twitter.close()

normalized = normalize_data([en_us_blogs_text, en_us_news_text, en_us_twitter_text])
# Turn data into Dataframe
data = {
    "blogs": normalized[0],
    "news": normalized[1],
    "twitter": normalized[2],
}
df = pd.DataFrame(data=data)

# Eliminar signos de puntuación, url y números
def remove_characters(text):
    '''Remove all signs from a string'''
    return text.translate(text.maketrans('', '', string.punctuation))

def remove_url(text):
    '''Remove url from a string'''
    return re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

def remove_num(text):
    '''Remove num'''
    return re.sub('^\d+\s|\s\d+\s|\s\d+$','',text)

# Se quitan vacíos
df = df.dropna(subset=['blogs'])
df = df.dropna(subset=['news'])
df = df.dropna(subset=['twitter'])

# Lowercasing
df['blogs'] = df['blogs'].apply(lambda line: str(line).lower())
df['news'] = df['news'].apply(lambda line: str(line).lower())
df['twitter'] = df['twitter'].apply(lambda line: str(line).lower())

# Se quitan signos de puntuación
df['blogs'] = df['blogs'].apply(lambda line: remove_characters(str(line)))
df['news'] = df['news'].apply(lambda line: remove_characters(str(line)))
df['twitter'] = df['twitter'].apply(lambda line: remove_characters(str(line)))

# Se quitan enlaces URL
df['blogs'] = df['blogs'].apply(lambda line: remove_url(str(line)))
df['news'] = df['news'].apply(lambda line: remove_url(str(line)))
df['twitter'] = df['twitter'].apply(lambda line: remove_url(str(line)))

# Se quitan los emojis
df['blogs'] = df['blogs'].apply(lambda line: emoji.demojize(str(line)))
df['news'] = df['news'].apply(lambda line: emoji.demojize(str(line)))
df['twitter'] = df['twitter'].apply(lambda line: emoji.demojize(str(line)))

# Se quitan números
df['blogs'] = df['blogs'].apply(lambda line: remove_num(str(line)))
df['news'] = df['news'].apply(lambda line: remove_num(str(line)))
df['twitter'] = df['twitter'].apply(lambda line: remove_num(str(line)))

expresiones = []
for i in expresiones:
    stopwords.add(i)

clean_tweets = []
for tweet in df['twitter']:
    word_list = []
    for word in tweet.split():
        word_list.append(word)
    clean_tweets.append(' '.join(word_list))

clean_blogs = []
for blog in df['blogs']:
    word_listo = []
    for word in blog.split():
        word_listo.append(word)
    clean_blogs.append(' '.join(word_listo))

clean_news = []
for new in df['news']:
    list_words = []
    for word in new.split():
        list_words.append(word)
    clean_news.append(' '.join(list_words))

global_data = clean_tweets+clean_news+clean_blogs
val=round(len(global_data)*0.1,0)
random_sample=random.sample(global_data,int(val))
warnings.filterwarnings('ignore')

# Digrama
digrama=[]
size=2
def ngram(ngrama, size):
    for word in range(len(random_sample)):
        try:
            for item in ngrams(random_sample[word].split(),size):
                ngrama.append(item)
        except Exception as e:
            print(e)
            return ngrama
    return ngrama
digrama = ngram(digrama, size)

#Trigrama
trigrama=[]
size=3
trigrama = ngram(trigrama, size)

#Tetragrama
tetragrama=[]
size=4
tetragrama = ngram(tetragrama, size)

#Pentagrama
pentgrama=[]
size=5
pentgrama = ngram(pentgrama, size)
