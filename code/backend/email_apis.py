from flask import Flask, jsonify, request
import os
import json
from email_classification import email_classification

app = Flask(__name__)

@app.route('/email/categorize-folder', methods=['GET'])
def categorize_folder():
    # Get the folder path from the query parameter
    folder_path = request.args.get('folder_path')
    if not folder_path or not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        return jsonify({"error": "Invalid folder path"}), 400

    # Call the email classification function with the folder path
    return email_classification(folder_path)

if __name__ == '__main__':
    app.run(debug=True)
