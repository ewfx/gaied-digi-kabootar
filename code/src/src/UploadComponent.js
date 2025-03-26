import React from 'react';
import Header from './component/header/Header';
import Footer from './component/footer/Footer';
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
      <Footer />
    </div>
  );
}

export default UploadComponent;