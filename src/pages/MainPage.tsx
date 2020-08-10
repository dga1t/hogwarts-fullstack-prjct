import React, { useState, useEffect, useContext } from 'react';
import { getStudents, addStudent } from '../lib/api';
import styles from '../styles/MainPage.module.css';
import Container from "react-bootstrap/Container";
import StudentsList from '../components/StudentsList';
import { Student } from '../model/Student';
import PieChart from '../components/PieChart';
import UserContext from "../context/UserContext";


// const mockStudents = [{
//   id: '01',
//   date: new Date,
//   name: 'Van Helsing Jr.',
//   skills: {'nightvision': 5}}, 
// {
//   id: '02',
//   date: new Date,
//   name: 'Dr.Evil',
//   skills: {'giantlaser': 5}
// }]

const MainPage = () => {
  const [ students, setStudents ] = useState<Student[]>([]);
  const [ loading, setLoading ] = useState(false);

  useEffect(() => {
    setLoading(true);
    const students = getStudents()
      .then(response => {
        console.log(response.data)
        setStudents(response.data)
        setLoading(false);
      });
  }, []);

  return(
    <div className={styles.MainPageLayout}>
      <Container style={{ paddingLeft: 0, paddingRight: 0 }}>
        <StudentsList students={Object.values(students)} />
      </Container>
      <Container>
        <PieChart />
      </Container>
    </div>

  )
}

export default MainPage;

