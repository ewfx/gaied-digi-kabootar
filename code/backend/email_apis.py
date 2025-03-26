import re
from flask import Flask, jsonify, request
import os
import json
from flask_cors import CORS  # Import Flask-CORS
from email_classification import email_classification

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/email/categorize-folder', methods=['GET'])
def categorize_folder():
    print("Inside categorize_folder")
    # Get the folder path from the query parameter
    folder_path = request.args.get('folder_path')
    if not folder_path or not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        return jsonify({"error": "Invalid folder path"}), 400

    # Call the email classification function with the folder path
    return email_classification(folder_path)

# API endpoint for folder upload
@app.route('/upload/folder', methods=['POST'])
def upload_folder():
    # Directory to store uploaded files
    UPLOAD_FOLDER = 'uploads'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    # Directory to store uploaded files
    if 'files[]' not in request.files:
        return jsonify({'message': 'No files uploaded.'}), 400

    uploaded_files = request.files.getlist('files[]')
    if len(uploaded_files) == 0:
        return jsonify({'message': 'No files uploaded.'}), 400

    saved_files = []
    for file in uploaded_files:
        # Preserve folder structure using the file's relative path
        relative_path = file.filename  # This should include the folder structure
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], relative_path)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure folder structure exists
        file.save(save_path)
        saved_files.append({
            'filename': relative_path,
            'path': save_path
        })

    # Regular expression to extract folder path
    folder_match = re.match(r'^(.*)[\\/][^\\/]+$', save_path)
    folder_path = folder_match.group(1) if folder_match else None  # Extract the folder path as a string

    if not folder_path:
        return jsonify({'message': 'Failed to extract folder path.'}), 500

    print(f'Folder Path:',folder_path)
    return jsonify({
        'message': 'Folder uploaded successfully!',
        'folderPath': folder_path  # Return the extracted folder path as a string
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
