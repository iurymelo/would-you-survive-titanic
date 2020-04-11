import React from 'react';
import TopBar from "./Navigation/TopBar";
import './global.css'
import Home from "./Views/Home/Home";

function App() {
  return (
    <div >
      <TopBar />
      <Home/>
    </div>
  );
}

export default App;
