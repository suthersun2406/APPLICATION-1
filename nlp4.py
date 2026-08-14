# WORD and SENTENCE Tokenize
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text="Suthersun as an lovely fellow. He stays in SAFA Apartments in chennai and he is too far from me!"
print("Word Tokenize:",word_tokenize(text))
print("Sentence Tokenize:",sent_tokenize(text))