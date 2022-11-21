# python functions for text preprocessing
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

def lower(txt):
    '''
    Changes input string to lower case.
    '''
    txt = [word.lower() for word in txt]
    return txt

def remove_punc(txt):
    '''
    Removes punctuation from input string.
    '''
    table = str.maketrans('', '', string.punctuation)
    txt = [w.translate(table) for w in txt]
    return txt

def remove_stopwords(txt):
    '''
    Removes nltk stopword from input string.
    '''
    stop_words = stopwords.words('english')
    txt = [w for w in txt if not w in stop_words]
    return txt   
    
def my_stemmer(txt):
    '''
    Change input string into stem using nltk.
    '''
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in txt]
    return stemmed

def my_lemma(txt):
    '''
    Return lemmatized version of input string
    '''
    lemmatizer = WordNetLemmatizer()
    lemmad = [lemmatizer.lemmatize(word) for word in txt]
    return lemmad

def preprocess(txt):
    '''
    Applies the text preprocessing steps
    '''
    txt = txt.split()
    txt = remove_punc(txt)
    txt = lower(txt)
    txt = remove_stopwords(txt)
    txt = my_stemmer(txt)
    txt = my_lemma(txt)
    return txt
