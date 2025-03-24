from flask import Flask, jsonify, request
import os
import json
from email_classification import extract_text_from_pdf, extract_text_from_docx, extract_text_from_doc, extract_text_from_eml, classify_email, clean_email_text, analyze_text

app = Flask(__name__)

@app.route('/email/categorize', methods=['POST'])
def categorize_email():
    email_path = request.json.get('email_path')
    if not email_path or not os.path.exists(email_path):
        return jsonify({"error": "Invalid email path"}), 400

    # Determine the file type and extract text accordingly
    if email_path.endswith(".pdf"):
        email_text = extract_text_from_pdf(email_path)
    elif email_path.endswith(".docx"):
        email_text = extract_text_from_docx(email_path)
    elif email_path.endswith(".doc"):
        email_text = extract_text_from_doc(email_path)
    elif email_path.endswith(".eml"):
        email_text = extract_text_from_eml(email_path)
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    # Clean the email text
    cleaned_text = clean_email_text(email_text)

    # Analyze sentiment and extract keywords
    sentiment_result, keywords_result = analyze_text(cleaned_text)

    # Classify the email
    classification_result = classify_email(" ".join(keywords_result))

    # Convert classification_result to JSON serializable format
    classification_result_serializable = {key: (round(float(val), 2) if isinstance(val, (np.float32, np.float64)) else val) for key, val in classification_result.items()}

    return jsonify(classification_result_serializable)

if __name__ == '__main__':
    app.run(debug=True)
