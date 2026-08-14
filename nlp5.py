from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet 
import nltk 
nltk.download ('wordnet')
nltk.download ('omw-1.4')
lemmatizer = (WordNetLemmatizer())
print (lemmatizer.lemmatize("running", pos="v"))
print (lemmatizer. lemmatize("better", pos="a"))