
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Home from './pages/Home';
import Grid from './pages/Grid';

function App() {
  return (
    <div className="App">
    <Router>
      
        <Routes>
          <Route exact path="/" element={<Home/>}/>
          <Route exact path="/grid" element={<Grid/>}/>
        </Routes>
     
    </Router>
    </div>
  );
}

export default App;
