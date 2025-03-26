import React, { useState } from 'react';
import './Upload.css';
import { MailCheck, Upload, Trash2, FileText, Image as ImageIcon, Loader2 } from 'lucide-react';  // Icons
import Table from '../table/Table';

const columnsFile = [
  { header: 'ID', accessor: 'id' },
  { header: 'File Name', accessor: 'name' },
  { header: 'Actions', accessor: 'action' },
];

const FileUpload = () => {
  const [files, setFiles] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (event) => {
    setIsLoading(true);
    const uploadedFiles = Array.from(event.target.files);
    const newFiles = uploadedFiles.map((file) => ({
      file, // Keep the original File object
      name: file.name, // Add the file name
      isslected: false, // Add the 'isslected' property
      })
    );

    // Update the state with the new files
    setFiles((prevFiles) => [...prevFiles, ...newFiles]);
    setIsLoading(false);
  };

  const handleUpload = async (indexFile) => {
    if (files.length === 0) {
      alert('Please select files or a folder first!');
      return;
    }

    const formData = new FormData();
    formData.append('files', files[indexFile].file); // Append the selected file

    try {
      const response = await fetch('http://localhost:3200/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        alert('Files or folder uploaded successfully!');
        console.log('Response:', data);
        handleConfirm(indexFile);
      } else {
        alert('Failed to upload files or folder.');
      }
    } catch (error) {
      console.error('Error uploading files or folder:', error);
      alert('An error occurred while uploading.');
    }
  };

  const handleConfirm = (index) => { 
    const updatedFiles = [...files];
    updatedFiles.map((file, i) => {
      if (i === index) {
        file.isslectected = !file.isslectected;
      }
      return file;});
    setFiles(updatedFiles);
  }

  const handleRemove = (index) => {
    const updatedFiles = [...files];
    updatedFiles.splice(index, 1);
    setFiles(updatedFiles);
  };



  return (
    <div className="upload-container">
      <div className="upload-area">
        <label htmlFor="file-upload" className="upload-button" style={{
            display: "flex",
            width: "160px",
            margin: "auto",
          }}>
          <Upload color="#FFFFFF" />
          {isLoading ? 'Uploading...' : 'Upload Files'}
        </label>
        <input 
          type="file" 
          id="file-upload" 
          multiple 
          className="upload-input" 
          onChange={handleFileChange} 
          disabled={isLoading}
        />
      </div>

      {files.length > 0 && (
        <div className="file-table-container">
          <div className="table-scroll-wrapper">

          <table className="file-table">
            <thead>
              <tr>
                {columnsFile.map((column, index) => (
                  <th key={index}>{column.header}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {files.map((file, index) => (
                <React.Fragment key={index}>
                  <tr>
                    <td>{index + 1}</td>
                    <td>{file.name}</td>
                    <td className="action-buttons">
                      <button className="remove-btn" onClick={() => handleRemove(index)}>
                        <Trash2 className="trash-icon" /> Remove
                      </button>
                      <button className="confirm-btn" onClick={() => handleUpload(index)}>
                        <MailCheck color="#4CAF50" /> Confirm
                      </button>
                    </td>
                  </tr>
                  
                  {file.isslectected &&<tr>
                    <td colSpan={columnsFile.length}>
                      <Table />
                    </td>
                  </tr>}
                </React.Fragment>
              ))}
            </tbody>
          </table>
          </div>
        </div>
      )}
    </div>
  );
};

export default FileUpload;
