import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [caption, setCaption] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:5000/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setCaption(response.data.caption);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <h1>Instagram Caption Generator</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Generate a Caption</button>
      </form>
      {caption && (
        <div>
          <h2>Generated Caption:</h2>
          <p>{caption}</p>
        </div>
      )}
    </div>
  );
}

export default App;
