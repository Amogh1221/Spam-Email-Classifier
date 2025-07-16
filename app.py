import streamlit as st
import numpy as np
import pandas as pd
import pickle
from nltk.corpus import stopwords
import nltk
import string
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')


def process(text):
  text=text.lower()
  text=word_tokenize(text)
  text=[word for word in text if word.isalnum()]
  text=[word for word in text if word not in stopwords.words('english')]
  for i in range(len(text)):
    text[i]=stemmer.stem(text[i])
  return ' '.join(text)

model=pickle.load(open('spam_email_classifier.pkl','rb'))
stemmer=pickle.load(open('stemmer.pkl','rb'))
tf_itf=pickle.load(open('transform.pkl','rb'))

st.title("Spam Email Classifier")

input_email=st.text_area("Enter your message")

if st.button('Predict'):

    input_email=process(input_email)
    vectorized = tf_itf.transform([input_email])
    res=model.predict(vectorized)
    
    if res == 1:
        st.header("It's a Spam")
    else:
        st.header("It is Not a Spam")



