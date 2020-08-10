import React from "react";

import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Container from "react-bootstrap/Container";
import Col from 'react-bootstrap/Col';


const AddStudent = () => {

  return (
    <Container>
      <Form className="mt-5">
        <Form.Row>
          <Col>
            <Form.Control placeholder="First name" />
          </Col>
          <Col>
            <Form.Control placeholder="Last name" />
          </Col>
        </Form.Row>
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="Enter email" />
        </Form.Group>
        <Form.Group controlId="exampleForm.SelectCustom">
          <Form.Label>Select a mastered skill</Form.Label>
          <Form.Control as="select" custom>
            <option>Potion making</option>
            <option>Spells</option>
            <option>Quidditch</option>
            <option>Animagus</option>
          </Form.Control>
        </Form.Group>
        <Form.Group controlId="exampleForm.SelectCustom">
          <Form.Label>Select a desired skill</Form.Label>
          <Form.Control as="select" custom>
            <option>Potion making</option>
            <option>Spells</option>
            <option>Quidditch</option>
            <option>Animagus</option>
          </Form.Control>
        </Form.Group>
        <Button variant="primary" type="submit">Submit</Button>
      </Form>
    </Container>
  )
}

export default AddStudent;