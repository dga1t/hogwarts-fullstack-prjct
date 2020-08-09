import React from 'react';
import { Route, Switch } from "react-router-dom";

import MainPage from "./pages/MainPage";
import StudentData from "./pages/StudentData";
import AddStudent from "./pages/AddStudent";
import Login from './pages/Login';
import SignUp from './pages/SignUp';

const Routes = () => {
  return(
    <Switch>
      <Route exact path="/">
        <MainPage />  
      </Route>
      <Route exact path="/student">
        <StudentData />  
      </Route>
      <Route exact path="/student/add">
        <AddStudent />  
      </Route>
      <Route exact path="/login">
        <Login />  
      </Route>
      <Route exact path="/signup">
        <SignUp /> 
      </Route>
    </Switch>
  )
}

export default Routes;