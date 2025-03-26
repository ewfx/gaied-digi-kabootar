import React from 'react';
import Header from './component/header/Header';
import Upload from './component/upload/Upload';
import FolderUpload from './component/folderUpload/FolderUpload';

function UploadComponent() {
  return (
    <div className='wrapper'>
      <Header />
      <div className='content'>
        {/* <Upload /> */}
        <FolderUpload />
      </div>
    </div>
  );
}

export default UploadComponent;