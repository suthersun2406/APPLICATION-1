import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punctk')
nltk.download("stopwords")

st.title("stopword removal")

text = st.text_area("enter text here")
if st.button("removal stopwords"):
    tokens =word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    
    filtered = [word for word in tokens if word.lower() not in stop_words]
    removed_count =len(tokens) - len(filtered)
    
    st.write("filtered tokens:",filtered)
    st.write("stopwords removed:",removed_count)