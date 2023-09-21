import React, { useState, useEffect } from 'react';
import graphImg1 from '../images/incoming_analysis.png'
import graphImg2 from '../images/nrwBilled.png'
function InputCards() {
    const [outgoingFlowChart, setOutgoingFlowChart] = useState('');
    const [meanValues, setMeanValues] = useState({
        normalFlowMean: 0,
        expectedFlowMean: 0,
        realTimeFlowMean: 0,
    });
    useEffect(() => {
        // Fetch the outgoing flow chart image from the Django API endpoint
        fetch('http://localhost:8000/console/generate_outgoing_flow_chart/')
          .then((response) => {
            if (response.ok) {
              return response.blob();
            }
            throw new Error('Network response was not ok.');
          })
          .then((blob) => {
            // Create a URL for the image blob
            const imageURL = URL.createObjectURL(blob);
            setOutgoingFlowChart(imageURL);
          })
          .catch((error) => {
            console.error('Error fetching outgoing flow chart image:', error);
          });

                // Fetch the mean values from your Django API endpoint
        fetch('http://localhost:8000/console/calculate_mean_values/')
        .then((response) => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then((data) => {
            setMeanValues(data);
        })
        .catch((error) => {
            console.error('Error fetching mean values:', error);
        });
}, []);
  return (
    <div className='inp_out_cards'>
        <div className="input_card">
            <img className="input_photo" alt='graph_img1'  src={outgoingFlowChart} />
            <h3 className="input_title" style={{ color: "black", textAlign: "center", fontWeight: "bold", fontSize: "40px", marginBottom:"20px" }}>Outgoing Analysis</h3>    
            <div className="input_description">
            <p style={{ color: "blue", textAlign: "center", fontSize: "20px" }}>Normal Flow: {meanValues.normal_flow_mean}</p>
            <p style={{ color: "yellow", textAlign: "center", fontSize: "20px" }}>Expected Flow: {meanValues.expected_flow_mean}</p>
            <p style={{ color: "red", textAlign: "center", fontSize: "20px" }}>Real Time Flow: {meanValues.real_time_flow_mean}</p>
            </div>
        </div>

        <div className="input_card">
            <img className="input_photo" alt='graph_img1'  src={graphImg1} />
            <h3 className="input_title" style={{ color: "black", textAlign: "center", fontWeight: "bold", fontSize: "40px", marginBottom:"20px" }}>Incoming Analysis</h3>    
            <div className="input_description">
            <p style={{ color: "blue", textAlign: "center", fontSize: "20px" }}>Normal Flow</p>
            <p style={{ color: "yellow", textAlign: "center", fontSize: "20px" }}>Expected Flow</p>
            <p style={{ color: "red", textAlign: "center", fontSize: "20px" }}>Real Time Flow</p></div>
        </div>

        <div className="input_card">
            <img className="input_photo" alt='graph_img1' src={graphImg2} />
            <h3 className="input_title" style={{ color: "black", textAlign: "center", fontWeight: "bold", fontSize: "40px", marginBottom:"20px" }}>Water Loss</h3>        
            <div className="input_description">
                <p style={{ color: "blue", textAlign: "center", fontSize: "20px" }}>Sytem Input Volume</p>
                <p style={{ color: "red", textAlign: "center", fontSize: "20px" }}>Billed Customer</p>
                </div>
        </div>
    </div>
  )
}

export default InputCards
