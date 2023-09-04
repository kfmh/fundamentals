import './App.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function LandingPage() {
  return <h1></h1>;
}

function Challange() {
  return <div className="full-bg"></div>
}

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/pastXse" element={<Challange/>} />
        </Routes>
      </div>
    </Router>
  );
}


export default App;
