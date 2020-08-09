import React from 'react';
import Container from 'react-bootstrap/esm/Container';
import StudentCard from './StudentCard';
import { Student } from '../model/Student';
import styles from '../styles/StudentsList.module.css';

interface StudentsListProps {
  students: Student[];
}

const StudentsList = ( {students}: StudentsListProps ) => {

  return(
    <Container className={styles.StudentsListLayout}>
      {students.map((student) => (
        <StudentCard key={student.id} student={student} />
      ))}
    </Container>
  )
}

export default StudentsList;