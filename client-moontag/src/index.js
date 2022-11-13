import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import reportWebVitals from './reportWebVitals';
import StoreRegister from './Components/register/store_register';
import Welcome from './Components/Welcome/welcome';



const regiter = ReactDOM.createRoot(document.getElementById('regiter'));
regiter.render (
  <Router>
  <React.StrictMode>
  <Switch>
    <Route path="/register">
      <StoreRegister url='/store-register' />
    </Route>
  </Switch>
  </React.StrictMode>
  </Router>
)

const welcome = ReactDOM.createRoot(document.getElementById('welcome'))
welcome.render (
  <Router>
  <React.StrictMode>
  <Switch>
    <Route path="/welcome">
      <Welcome url='/welcome'/>
    </Route>
  </Switch>
  </React.StrictMode>
  </Router>
)






reportWebVitals();
