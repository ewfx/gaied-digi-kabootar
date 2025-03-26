from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# API endpoint for file upload
@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'message': 'No files uploaded.'}), 400

    uploaded_files = request.files.getlist('files')
    if len(uploaded_files) == 0:
        return jsonify({'message': 'No files uploaded.'}), 400

    saved_files = []
    for file in uploaded_files:
        # Generate a unique filename with a timestamp
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{file.filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        saved_files.append({
            'filename': filename,
            'path': f"/uploads/{filename}"
        })

    return jsonify({
        'message': 'Files uploaded successfully!',
        'files': saved_files
    }), 200

# Serve static files from the 'uploads' folder
@app.route('/uploads/<filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3200, debug=True)