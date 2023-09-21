import React from 'react'

function Ai_sugg() {
  return (
    <>
    <div className="container-fluid">
    <div className="row">
        <div className="col-12 mt-3">
            <div className="ai-card">
                <div className="ai-card-vertical">
                    <div className="ai-card-body">
                        <h4 className="ai-card-title">AI-Suggestions</h4>
                        <ul>
                        <li><p style={{ fontWeight: "bold", fontSize: "16.5px" }}className="ai-sugg">1. Water loss expected for the upcoming months.</p></li> 
                        <li><p style={{ fontWeight: "bold", fontSize: "16.5px" }}className="ai-sugg">2. Machinery change required (ZONE 2- ZONE 7).</p></li> 
                        <li><p style={{ fontWeight: "bold", fontSize: "16.5px" }}className="ai-sugg">3. Maintenance audit required (CS - ZONE 4).</p></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

    </>
  )
}

export default Ai_sugg
