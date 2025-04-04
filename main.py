import streamlit as st
import pickle
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def clean_code(text):
    text=re.sub('[^a-zA-Z0-9_\s]',' ',text) #remove special character
    tokens=word_tokenize(text.lower()) # tokenization and lower casing
    tokens=[word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

st.title("Bug Prediction & Prevention System")
st.write("Enter a python code snippet to check if it contain bug .")
user_input=st.text_area("Enter Code Snippet",height=200)
btn=st.button("Predict!")

if btn:
    vectorizer=pickle.load(open('tfidf_vectorizer.pkl','rb'))
    model=pickle.load(open('rf.pkl','rb'))
    
    cleaned_code=clean_code(user_input)
    input_tfidf=vectorizer.transform([cleaned_code])
    predictt=model.predict(input_tfidf)[0]

    if predictt:
        st.error("Bug detected in the code")

    else:
        st.success("No bugs found in the code")