import './App.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function LandingPage() {
  return <h1>nothing here</h1>;
}

function Challange() {
  return <div className="full-bg"></div>
}

function App() {
  return (
    <Router>

        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/pastXse" element={<Challange/>} />
        </Routes>
      <div>
        <div style={{position: "fixed", zIndex:"0"}}>
          <ul>
            <li>
              <Link to="/">t</Link>
            </li>
            <li>
              <Link to="/pastXse">t</Link>
            </li>
          </ul>
        </div>
      </div>
    </Router>
  );
}


export default App;
