import streamlit as st
import pickle
import re
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

# Load model
with open("fake_news_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load vectorizer
with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Page title
st.set_page_config(page_title="Fake News Detection", page_icon="📰")

st.title("📰 Fake News Detection")
st.write("Enter a news article to check whether it is Fake or Real.")

news = st.text_area("News Article")

if st.button("Predict"):

    if news.strip() == "":
        st.warning("Please enter a news article.")
    else:
        cleaned = clean_text(news)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)

        probability = model.predict_proba(vector)

        confidence = probability.max() * 100

        if prediction[0] == 0:
            st.error("🚨 Fake News")
        else:
            st.success("✅ Real News")

        st.write(f"Confidence: {confidence:.2f}%")