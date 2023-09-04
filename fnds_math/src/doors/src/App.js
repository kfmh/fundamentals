import './App.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function LandingPage() {
  return <h1>Welcome to the Landing </h1>;
}

function Challange() {
  return <div className="full-bg"></div>
}

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/"></Link>
            </li>
            <li>
              <Link to="/pastXse"></Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/pastXse" element={<Challange/>} />
        </Routes>
      </div>
    </Router>
  );
}


export default App;
