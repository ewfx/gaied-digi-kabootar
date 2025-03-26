import React, { useState } from 'react';
import './FolderUpload.css';
import { Trash2, Upload, MailCheck } from 'lucide-react'; // Icons
import Table from '../table/Table';

const FolderUpload = () => {
  const [files, setFiles] = useState([]);
  const [emailData, setEmailData] = useState({});

  const handleFileChange = (event) => {
    const uploadedFiles = Array.from(event.target.files);
    setFiles((prevFiles) => [...prevFiles, ...uploadedFiles]);
  };

  const handleUpload = async () => {
    if (files.length === 0) {
      alert('Please select a folder first!');
      return;
    }

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        formData.append('files[]', file); 
    }
 
    try {
      const response = await fetch('http://127.0.0.1:5000/upload/folder', {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        const data = await response.json();
        alert('File uploaded successfully!');
        console.log('Response:', data);

       // Fetch the folder path from the response
       const folderPath = data.folderPath;

       // GET request to categorize the folder
       const categorizeResponse = await fetch(
         `http://127.0.0.1:5000/email/categorize-folder?folder_path=${encodeURIComponent(folderPath)}`,
         {
           method: 'GET',
         }
       );

       if (categorizeResponse.ok) {
        const categorizeData = await categorizeResponse.json();
        console.log('Categorization Response:', categorizeData);
        setEmailData(categorizeData); // Update the state with the categorization data
      } else {
        alert('Failed to categorize the folder.');
      }

      } else {
        alert('Failed to upload the file.');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('An error occurred while uploading.');
    } 
  };

  const handleRemove = (index) => {
    const updatedFiles = [...files];
    updatedFiles.splice(index, 1);
    setFiles(updatedFiles);
  };

  return (
    <div className="folder-upload-container">
      <div className="upload-area">
        <label htmlFor="folder-upload" className="upload-button" style={{
            display: "flex",
            width: "160px",
            margin: "auto",
          }}>
          <Upload color="#FFFFFF" />
          <div style={{
            marginLeft: "10px"
          }}>{'Upload Folder'}</div>
        </label>
        <input
          type="file"
          id="folder-upload"
          webkitdirectory="true" // Enable folder selection
          multiple
          className="upload-input"
          onChange={handleFileChange}
          directory
        />
      </div>

      {files.length > 0 && (
        <div className="file-table-container">
          <table className="file-table">
            <thead>
              <tr>
                <th>#</th>
                <th>File Name</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {files.map((file, index) => (
                <tr key={index}>
                  <td>{index + 1}</td>
                  <td>{file.name}</td>
                  <td>
                    <button
                      className="remove-btn"
                      onClick={() => handleRemove(index)}
                    >
                      <Trash2 className="trash-icon" /> Remove
                    </button>
                   
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

        </div>
      )}
      <div className="upload-button" style={{
        marginTop: "40px",
        }}>
        <button className="upload-btn" onClick={handleUpload} >
          <MailCheck className="upload-icon" /> Submit
        </button>
    </div>
      <Table dataResponse={emailData}/>
    </div>
  );
};

export default FolderUpload;