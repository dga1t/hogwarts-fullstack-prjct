import React from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { Student } from '../model/Student';
import styles from '../styles/StudentCard.module.css';
import { Pencil, Trash } from 'react-bootstrap-icons';



interface StudentCardProps {
  student: Student;
}

const StudentCard = ( {student}: StudentCardProps) => {

  return(
    <Card className="mb-2 d-flex flex-row">
     <Card.Body className={styles.StudentCard}>{student.name}</Card.Body>
     <Button variant="primary"><Pencil size={22} /></Button>
     <Button variant="primary"><Trash size={22} /></Button>
    </Card>
  )
}

export default StudentCard;