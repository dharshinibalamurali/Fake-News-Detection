# 📰 Fake News Detection using Machine Learning

## 📌 PROJECT OVERVIEW

Fake News Detection is a Machine Learning project that classifies news articles as **Fake** or **Real** using Natural Language Processing (NLP). The model is trained on the **Fake.csv** and **True.csv** datasets and uses **TF-IDF Vectorization** with multiple Machine Learning algorithms.

The best-performing model (**Random Forest**) is saved and deployed using **Streamlit** for real-time predictions.

## 🎯 OBJECTIVES

- Detect whether a news article is Fake or Real.
- Apply Natural Language Processing (NLP) techniques.
- Compare multiple Machine Learning algorithms.
- Build a web application for real-time prediction.
- Deploy the project using Streamlit Community Cloud.

## 📂DATASET

The project uses two datasets:

- **Fake.csv**
- **True.csv**

### DATASET FEATURES

- Title
- Text
- Subject
- Date

Target Label:

- **0 → Fake News**
- **1 → Real News**

## 🛠 TECHNOLOGIES USED

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- Scikit-learn
- Streamlit
- Pickle
- Git & GitHub

## 📊 EXPLORATORY DATA ANALYSIS (EDA)

The following analyses were performed:

- Dataset Information
- Missing Value Analysis
- Duplicate Value Removal
- Fake vs Real News Distribution
- Subject-wise Distribution
- News Length Distribution
- Data Visualization

## 🧹 TEXT PREPROCESSING

The news articles were cleaned using the following steps:

- Convert text to lowercase
- Remove URLs
- Remove HTML tags
- Remove punctuation
- Remove numbers
- Remove stopwords
- Create cleaned text

## 🔤 FEATURE EXTRACTION

TF-IDF (Term Frequency–Inverse Document Frequency) was used to convert text into numerical feature vectors.

## 🤖 MACHINE LEARNING MODLES

The following algorithms were trained and evaluated:

1. Logistic Regression
2. Naive Bayes
3. Decision Tree
4. Random Forest

## 📈 MODEL PERFORMANCE

| Algorithm | Accuracy |
|------------|----------|
| Logistic Regression | **98.93%** |
| Naive Bayes | **94.89%** |
| Decision Tree | **99.62%** |
| Random Forest | **99.75%** ✅ |

### Best Model

**Random Forest Classifier**

Accuracy: **99.75%**

## 📊 EVALUATION METRICES

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

## 💾 MODEL SAVING

The trained model and vectorizer were saved using Pickle.

Generated files:

- fake_news_model.pkl
- tfidf_vectorizer.pkl

## 🌐 STREAMLIT APPLICATION

The Streamlit application allows users to:

- Enter a news article
- Predict Fake or Real news
- Display prediction confidence
- Provide a simple and interactive interface

## 📁 Project Structure

Fake-News-Detection/
│
├── Fake_News_Detection.ipynb
├── app.py
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
├── Fake.csv
└── True.csv

## ▶️ How to Run

### Clone Repository

git clone https://github.com/dharshinibalamurali/Fake-News-Detection.git

### Install Requirements

pip install -r requirements.txt


### Run Streamlit App


streamlit run app.py

## 📷 Sample Prediction

**Input**

The government announced a new education policy to improve schools.

**Prediction**


✅ Real News
Confidence: 99.87%

## 🚀 Future Improvements

- Deep Learning (LSTM/BERT)
- News Source Verification
- Multilingual Fake News Detection
- Explainable AI (XAI)
- Live News API Integration


## 👩‍💻 Author

**B.Dharshini**

B.Tech.Information Technology

Nehru Institude Of Institude Of Engineering and Technology
