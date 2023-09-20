import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import img1 from "./images/Poseidon.png";

//user-form card
function User() {
  return (
    <>
      <div id="info-form">
        <h2> NRW User-Portal</h2>
        <form action="#" method="post">
          <div>
            <label for="Name">Name: </label>
            <input type="text" id="name" name="name" required></input>
          </div>

          <div>
            <label for="District">District: </label>
            <input type="text" id="district" name="district" required></input>
          </div>

          <div>
            <label for="Consumer No">Consumer No: </label>
            <input
              type="text"
              id="consumer-no"
              name="consumer-no"
              required
            ></input>
          </div>

          <div>
            <label for="zone">Select DMA Zone:</label>
            <select id="zone" name="zone">
              <option value="zone1">DMA 1</option>
              <option value="zone2">DMA 2</option>
              <option value="zone3">DMA 3</option>
              <option value="zone4">DMA 4</option>
            </select>
          </div>

          <div>
            <button> Proceed </button>
          </div>
        </form>
      </div>
    </>
  );
}

function MyImage() {
  return (
    <div class="Image-side">
      <img src={img1} alt="MapImage" />
    </div>
  );
}

ReactDOM.render(
  <>
    <h1>NRW Distribution Management</h1>
    <div class="Container">
      <MyImage />
      <User />
    </div>
  </>,
  document.getElementById("root")
);
