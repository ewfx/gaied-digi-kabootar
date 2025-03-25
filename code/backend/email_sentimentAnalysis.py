# Install necessary libraries
# pip install nltk rake-nltk

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from rake_nltk import Rake
# from email_cosine_embedding import extract_text_from_docx, extract_text_from_doc, extract_text_from_eml, extract_text_from_pdf

# Download the necessary NLTK data
nltk.download("vader_lexicon")

# Initialize the NLTK Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Function for sentiment analysis and keyword extraction
def analyze_text(text):
    # Sentiment Analysis using NLTK
    sentiment_scores = sia.polarity_scores(text)
    sentiment = {
        "Sentiment": "Positive" if sentiment_scores["compound"] > 0 else "Negative" if sentiment_scores["compound"] < 0 else "Neutral",
        "Scores": sentiment_scores,
    }

    # Keyword Extraction using RAKE
    rake = Rake()
    rake.extract_keywords_from_text(text)
    keywords = rake.get_ranked_phrases()

    return sentiment, keywords

# Example text input
text = "The movie was absolutely fantastic! The performances were top-notch and the visuals were stunning."

# Analyze text
# sentiment_result, keywords_result = analyze_text(extract_text_from_docx("C:/Users/Vaishali/AIML_POC/email_automation/dataset/DataSet_2.docx"))

# Output results
# print("Sentiment Analysis Result=====:", sentiment_result)
# print("Extracted Keywords:", keywords_result)