import React from 'react'
import AnalyticalGraph from './AnalyticalGraph'
import Incidents from './Incidents'
import InputCards1 from './InputCards1'
// import InputCards2 from './InputCards2'
// import InputCards3 from './InputCards3'
import Reporting from './Reporting'
import Ai_sugg from './Ai_sugg'

function DashboardDisplay() {
  return (
    <>
        <div className="card_holder">
            <AnalyticalGraph />
            <Ai_sugg />
            <Incidents />
            <InputCards1 />
            <Reporting />
        </div>
    </>
  )
}

export default DashboardDisplay
