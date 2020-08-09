import React, { useState, useEffect, useContext } from 'react';
import Container from "react-bootstrap/Container";
import { BrowserRouter as Router } from 'react-router-dom';

import Routes from './Routes';
import AppNavbar from "./components/AppNavbar";
import { User } from "./model/User";
import UserContext from "./context/UserContext";


function App() {
  const [currentUser, setCurrentUser] = useState<User | null>(null);

  return (
    <Router> 
      <UserContext.Provider
        value={{
          currentUser,
          setCurrentUser,
          logout: () => setCurrentUser(null),
        }}
      >
        <AppNavbar />
        <Container fluid style={{ paddingLeft: 0, paddingRight: 0 }}>
          <Routes />
        </Container>
      </UserContext.Provider>
    </Router>
  );
}

export default App;
