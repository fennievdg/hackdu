'use client';
import React, { useState } from 'react';

const Page = () => {
  const [report, setReport] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      // Perform API request to Flask Python backend
      const response = await fetch('/api/form', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          report,
        }),
      });

      // Handle the response if needed
      const responseData = await response.text();
      setResponse(responseData);
    } catch (error) {
      // Handle any errors
      console.error(error);
    }
  };

  return (
    <div>
      <h1>medDiana 👩🏼‍⚕️</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="report">Insert your lab report</label>
          <input
            type="text"
            id="report"
            value={report}
            onChange={(e) => setReport(e.target.value)}
            required
            className='input'
          />
        </div>
        <button type="submit">Submit</button>
      </form>
      {response && <p>{JSON.parse(response).response}</p>}
    </div>
  );
};

export default Page;
