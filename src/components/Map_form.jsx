import React from 'react'

function Map_form() {
  return (
    <>
      <div id="map-info-form">
        <form className='map-form' action="#" method="post">
        <h2 className='map-h2'> NRW User-Portal</h2>
          <div>
            <label className='map-label' for="Name">Name: </label>
            <input className='map-input' type="text" id="name" name="name" required></input>
          </div>

          <div>
            <label className='map-label' for="District">District: </label>
            <input className='map-input' type="text" id="district" name="district" required></input>
          </div>

          <div>
            <label className='map-label' for="Consumer No">Consumer No: </label>
            <input
              className='map-input'
              type="text"
              id="consumer-no"
              name="consumer-no"
              required
            ></input>
          </div>

          <div>
            <label className='map-label' for="zone">Select DMA Zone:</label>
            <select className='map-menu' id="zone" name="zone">
              <option value="zone1">DMA 1</option>
              <option value="zone2">DMA 2</option>
              <option value="zone3">DMA 3</option>
              <option value="zone4">DMA 4</option>
            </select>
          </div>

          <div>
            <button className='map-btn'> Proceed </button>
          </div>
        </form>
      </div>
    </>
  )
}

export default Map_form
