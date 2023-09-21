import React from 'react'

function InfoCards() {
    return (
      <div className="cards">
      <div className="mission-card">
        <h1>Our Mission</h1>
        <h6>Tackling Non-Revenue Water (NRW) Globally</h6>
        <p>Non-Revenue Water (NRW) poses a pressing global challenge, and its impact on societies cannot be overstated. In India alone, the annual cost of NRW reaches billions of dollars, affecting the lives of millions. NRW not only depletes our precious water resources but also strains financial sustainability and threatens environmental health.</p>
      </div>
      <div className="info-container">
<div class="flip">
    <div class="front">
       <h1 class="text-shadow">Engagement and Transparency for All</h1>
    </div>
    <div class="back">
    <p>To create a more engaged and transparent community, we've established a dedicated platform for both end-users and the general public. Here, individuals can easily report concerns related to water distribution, such as water leaks or theft. Additionally, we provide access to valuable information on relevant circulars and announcements, fostering a sense of community involvement in addressing water-related challenges.</p>
    </div>
</div>
<div class="flip">
<div class="front">
       <h1 class="text-shadow">Our Commitment to Action</h1>
    </div>
    <div class="back">
    <p>We are here to address this critical issue head-on, and our approach is powered by innovation. Our project introduces a cutting-edge, state-of-the-art software solution designed to combat NRW effectively. At its core, our solution excels in detecting leaks, improving distribution efficiency, and conserving vital resources.
</p>
    </div>
</div>
<div class="flip">
<div class="front">
       <h1 class="text-shadow">Empowering Change with Technology
</h1>
    </div>
    <div class="back">
    <p>Our platform goes beyond traditional NRW management. It plays a dual role: not only does it assist in the detection of water loss, but it also paves the way for training future Machine Learning Models. These models are pivotal in the meticulous analysis of Non-Revenue Water, guiding us towards informed decision-making.
</p>
    </div>
</div>

  
<div class="flip flip-vertical">
<div class="front">
       <h1 class="text-shadow">Streamlined Response and Continuous Improvement
</h1>
    </div>
    <div class="back">
    <p>Efficiency and responsiveness are at the heart of our platform. We offer automated responses to various events and complaints, simplifying the process of report generation. Real-time feedback from end-users and the general public enriches our data analysis, steering us towards continuous improvement.
</p>
    </div>
</div>
<div class="flip flip-vertical">
<div class="front">
       <h1 class="text-shadow">Data Integrity and Transparency</h1>
    </div>
    <div class="back">
    <p>We understand the importance of data integrity. That's why we've implemented a secure logging mechanism for District Metering Areas (DMA). This ensures the reliability and traceability of our data, supporting our commitment to transparency.
</p>
    </div>
</div>
<div class="flip flip-vertical">
<div class="front">
       <h1 class="text-shadow">Collaborative Data Sharing</h1>
    </div>
    <div class="back">
    <p>One of our platform's unique strengths is the seamless integration of district metering areas. Each DMA has its own console, facilitating data collection and sharing. This collaborative approach across DMAs enhances our ability to detect and mitigate water loss issues linked to NRW, ultimately helping us trace and combat any form of water loss more effectively.
</p>
    </div>
</div>
      </div>
      </div>

    )
  }

export default InfoCards
