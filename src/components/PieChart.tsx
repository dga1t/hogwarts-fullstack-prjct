import React from "react";

import Container from "react-bootstrap/Container";
import { VictoryPie } from "victory";

const mockData = [
  {skill: 1, wanted: 4},
  {skill: 2, wanted: 2},
  {skill: 3, wanted: 8},
];

const PieChart = () => {

  return (
    <Container>
      <VictoryPie 
        data={mockData}
        x="skill"
        y="wanted"
        height={200}
        width={200}
      />
    </Container>
  )
}

export default PieChart;