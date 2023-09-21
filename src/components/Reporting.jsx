import React, { useState } from 'react';
import { RiAddCircleFill } from 'react-icons/ri';

function Reporting() {
  const [reportLink, setReportLink] = useState(null); // State to store the report link

  const fetchReport = async () => {
    try {
      // Fetch the report from the Django API endpoint
      const response = await fetch('http://localhost:8000/console/generate_report/'); // Replace with the correct URL
      if (response.ok) {
        // If the response is successful, get the blob (PDF) and create a URL for it
        const blob = await response.blob();
        const reportURL = URL.createObjectURL(blob);
        setReportLink(reportURL); // Set the report link in the state
      } else {
        console.error('Error fetching report:', response.statusText);
      }
    } catch (error) {
      console.error('Error fetching report:', error);
    }
  };

  return (
    <div>
      {/* Call the fetchReport function when the reporting_card div is clicked */}
      <div onClick={fetchReport} className="reporting_card">
        <a
          href={reportLink}
          target="_blank"
          rel="noopener noreferrer"
          className="report_btn"
        >
          <div style={{color:"black"}} className="report-text">
            <h1>Report Generation</h1>
          </div>
          <div className="report_icon">
            <RiAddCircleFill style={{color:"black"}}/>
          </div>
        </a>
      </div>
    </div>
  );
}

export default Reporting;
