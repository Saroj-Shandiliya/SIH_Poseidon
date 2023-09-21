import React from 'react'

function Incidents() {
  return (
    <>
    <div className="container-fluid">
    <div className="row">
        <div className="col-12 mt-3">
            <div className="incident-card">
                <div className="incident-card-vertical">
                    <div className="incident-card-body">
                        <h4 className="incident-card-title">Recent Incidents</h4>
                        <ul>
                        <li><p style={{ color: "orange", textAlign: "center", fontWeight: "bold", fontSize: "26px" }}className="incidents">Loss detected : ZONE 2 - ZONE 7</p></li> 
                        <li><p style={{ color: "lightgreen", textAlign: "center", fontWeight: "bold", fontSize: "26px" }}className="incidents">Flow resolved : ZONE 3 - ZONE 8</p></li> 
                        <li><p style={{ color: "orange", textAlign: "center", fontWeight: "bold", fontSize: "26px" }}className="incidents">Loss detected : CS - ZONE 4</p></li>
                        <li><p style={{ color: "yellow", textAlign: "center", fontWeight: "bold", fontSize: "26px" }}className="incidents">Loss possibility : CS - ZONE 1</p></li> 
                        <li><p style={{ color: "lightgreen", textAlign: "center", fontWeight: "bold", fontSize: "26px" }}className="incidents">Flow resolved : ZONE 5 - ZONE 6</p></li> 
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

export default Incidents
