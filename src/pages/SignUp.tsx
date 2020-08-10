import React from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Container from "react-bootstrap/Container";
import { useForm, SubmitHandler } from "react-hook-form";

type FormData = {
  email: string;
  password: string;
};

const SignUp = () => {

  const { register, handleSubmit, errors } = useForm<FormData>();
  const onSubmit: SubmitHandler<FormData> = data => console.log(data);

  return(
    <Container>
      <Form onSubmit={handleSubmit(onSubmit)} className="mt-5">
        <Form.Group controlId="formBasicName">
          <Form.Label>Name</Form.Label>
          <Form.Control name="name" type="text" placeholder="Enter your name" ref={register} />
        </Form.Group>
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control name="email" type="email" placeholder="Enter email" ref={register} />
        </Form.Group>
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control name="password" type="password" placeholder="Password" ref={register} />
        </Form.Group>
        <Form.Group controlId="formBasicPassword">
          <Form.Label>Repeat password</Form.Label>
          <Form.Control name="password" type="password" placeholder="Repeat password" ref={register} />
        </Form.Group>
        <Button variant="primary" type="submit">Submit</Button>
      </Form>
    </Container>
  )
}

export default SignUp;