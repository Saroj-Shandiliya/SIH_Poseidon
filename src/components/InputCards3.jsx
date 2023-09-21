import React, { useState, useEffect } from 'react';

function InputCards() {
    const [lineChartNRW, setLineChart] = useState('');

    useEffect(() => {
        // Fetch the line chart image from the Django API endpoint
        fetch('http://localhost:8000/console/generate_line_chart/')
          .then((response) => {
            if (response.ok) {
              return response.blob();
            }
            throw new Error('Network response was not ok.');
          })
          .then((blob) => {
            // Create a URL for the image blob
            const imageURL = URL.createObjectURL(blob);
            setLineChart(imageURL);
          })
          .catch((error) => {
            console.error('Error fetching line chart image:', error);
          });
    }, []);
    

  return (
    <div className='inp_out_cards'>
        <div className="input_card">
            <img className="input_photo" alt='graph_img' src={lineChartNRW} />
            <h3 className="input_title">Ceasefire 'possibility' ahead of Syria talks</h3>    
            <div className="input_description"><p>The US and Russia have discussed the possibility of "localised ceasefires" in Syria ahead of peace talks to be held in Switzerland next week.The US and Russia have discussed the possibility of "localised ceasefires" in Syria ahead of peace talks to be held in Switzerland next week.</p></div>
        </div>
    </div>
  )
}

export default InputCards
