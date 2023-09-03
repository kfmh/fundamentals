import React from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

function LandingPage() {
  return <h1>Welcome to the Landing Page!</h1>;
}

function TestPage() {
  return <h1>This is the Test Page</h1>;
}

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Landing Page</Link>
            </li>
            <li>
              <Link to="/test">Test Page</Link>
            </li>
          </ul>
        </nav>

        <Route path="/" exact component={LandingPage} />
        <Route path="/test" component={TestPage} />
      </div>
    </Router>
  );
}

export default App;
