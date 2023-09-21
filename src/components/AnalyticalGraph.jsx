import React, { useState, useEffect } from 'react';

function AnalyticalGraph() {
    const [pieChartImage, setPieChartImage] = useState('');
    const [insights, setInsights] = useState({});

    useEffect(() => {
        // Fetch the pie chart image from the Django API endpoint
        fetch('http://127.0.0.1:8000/console/generate_pie_chart/')
            .then((response) => {
                if (response.ok) {
                    return response.blob();
                }
                throw new Error('Network response was not ok.');
            })
            .then((blob) => {
                // Create a URL for the image blob
                const imageURL = URL.createObjectURL(blob);
                setPieChartImage(imageURL);
            })
            .catch((error) => {
                console.error('Error fetching pie chart image:', error);
            });

        // Fetch the insights from the Django API endpoint
        fetch('http://127.0.0.1:8000/console/generate_pie_chart_insights/')
            .then((response) => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Network response was not ok.');
            })
            .then((data) => {
                setInsights(data);
            })
            .catch((error) => {
                console.error('Error fetching pie chart insights:', error);
            });
    }, []);

    return (
        <div className="container-fluid">
            <div className="row">
                <div className="col-12 mt-3">
                    <div className="card">
                        <div className="card-horizontal">
                            <div className="img-wrapper">
                                <img className="pie_img" src={pieChartImage} alt="Pie Chart" />
                            </div>
                            <div className="card-body">
                                <h4 className="card-title">Non-Revenue Water</h4>
                                <div className="insights">
                                    <p><strong>Total Non-Revenue Water:</strong> {insights['Non-Revenue Water']}</p>
                                    <p><strong>Total Real Losses:</strong> {insights['Real Losses']}</p>
                                    <p><strong>Total Arbitrary Loss:</strong> {insights['Arbitrary Loss']}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default AnalyticalGraph;
