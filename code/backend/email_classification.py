import email
import numpy as np
import pandas as pd
import pdfplumber
import os
import docx
from transformers import pipeline
import win32com.client as win32
from transformers import BertTokenizer, BertModel
import json
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from email_sentimentAnalysis import analyze_text
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from preprocess_email import clean_email_text

# Load Excel file with predefined categories
category_file = "C:/Users/Vaishali/AIML_POC/email_automation/Loan_Servicing_Requests.xlsx"
df_categories = pd.read_excel(category_file)

# Convert to dictionary {Request Type: [Keywords]}
category_mapping = {}
for _, row in df_categories.iterrows():
    category_mapping[row["Request Type"]] = {
        "Sub Request Type": row["Subrequest Type"],
        "Keywords": row["Keywords in Email"].split(", ")  # Assuming keywords are comma-separated
    }

# print(category_mapping)

# Folder containing email files
email_folder = "C:/Users/Vaishali/AIML_POC/email_automation/dataset"

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

def extract_text_from_doc(doc_path):
    word = win32.Dispatch("Word.Application")
    doc = word.Documents.Open(doc_path)
    text = doc.Content.Text
    doc.Close()
    word.Quit()
    return text

def extract_text_from_eml(eml_path):
    with open(eml_path, 'rb') as f:
        msg = email.message_from_binary_file(f)
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                if "attachment" not in content_disposition:
                    return part.get_payload(decode=True).decode()
        else:
            return msg.get_payload(decode=True).decode()

# Read all files in the folder
email_texts = {}
for email_file in os.listdir(email_folder):
    file_path = os.path.join(email_folder, email_file)
    if email_file.endswith(".pdf"):
        email_texts[email_file] = extract_text_from_pdf(file_path)
    elif email_file.endswith(".docx"):
        email_texts[email_file] = extract_text_from_docx(file_path)
    elif email_file.endswith(".doc"):
        email_texts[email_file] = extract_text_from_doc(file_path)
    elif email_file.endswith(".eml"):
        email_texts[email_file] = extract_text_from_eml(file_path)

# print(email_texts)

# Load BERT model and tokenizer for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_summary(email_text, num_sentences=3):
    sentences = sent_tokenize(email_text)
    sentence_embeddings = model.encode(sentences)
    email_embedding = model.encode([email_text])[0]
    
    similarities = cosine_similarity([email_embedding], sentence_embeddings)[0]
    top_sentence_indices = similarities.argsort()[-num_sentences:][::-1]
    
    summary = " ".join([sentences[i] for i in top_sentence_indices])
    return summary

def classify_email(email_text):
    labels = list(category_mapping.keys())
    
    # Generate embeddings for email text and category labels
    email_embedding = model.encode(email_text)
    category_embeddings = model.encode(labels)
    
    # Calculate cosine similarity between email text and category labels
    similarities = cosine_similarity([email_embedding], category_embeddings)
    best_match_index = similarities.argmax()
    request_type = labels[best_match_index]
    
    # Find sub request type and keywords
    sub_request_type = category_mapping[request_type]["Sub Request Type"]
    keywords = category_mapping[request_type]["Keywords"] 

    # Calculate confidence score
    confidence_score = round(similarities[0][best_match_index] * 200, 2)

    # Generate reason for categorization
    reason = f"The input is similar to the following request type {request_type} hence selected the type with confidence score {confidence_score:.2f}"
    
    return {
        "Request Type": request_type,
        "Sub Request Type": sub_request_type,
        "Confidence Score": confidence_score,
        "Reason": reason
    }

# Process all emails
classified_results = {}
for file, text in email_texts.items():
    cleanedText = clean_email_text(text)

    sentiment_result, keywords_result = analyze_text(cleanedText)
    classified_results[file] = classify_email(" ".join(keywords_result))

# Convert classified_results to JSON serializable format
classified_results_serializable = {k: {key: (float(f"{val:.2f}") if isinstance(val, np.float32) else val) for key, val in v.items()} for k, v in classified_results.items()}

print(json.dumps(classified_results_serializable, indent=4))
