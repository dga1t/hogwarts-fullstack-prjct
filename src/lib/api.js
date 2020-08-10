import axios from 'axios';

const baseUrl = 'http://localhost:5000/';

export async function getStudents() {
  const response = await axios.get(`${baseUrl}/students`);
  return response;
}

export function addStudent(student) {
  return axios.post(`${baseUrl}`, student);
}