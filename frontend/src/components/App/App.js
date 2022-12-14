import './App.css';
import {BrowserRouter,Route,Routes} from "react-router-dom"
import Images from "./../Images/Images";
import Menu from '../Menu/NavBar';
function App() {
  return (
    <div className="container">
      {Menu()}
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Images/>}/>    
          <Route path='/dashboard' element={<Images/>}/>    
        </Routes>
      </BrowserRouter>
    </div>
  );
}

/**
  <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
 */

export default App;
