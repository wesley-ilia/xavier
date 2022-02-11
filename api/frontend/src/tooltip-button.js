import styled from "styled-components";

export var TooltipButton = styled(Button)`
  text-align: center;
`;

export var TooltipBox = styled.div`
  position: absolute;
  top: calc(100% + 10px);
  // left: 30px;
  visibility: hidden;
  color: transparent;
  background-color: transparent;
  // width: 150px;
  padding: 5px 5px;
  border-radius: 4px;
  transition: visibility 0.5s, color 0.5s, background-color 0.5s, width 0.5s,
    padding 0.5s ease-in-out;
  &:before {
    content: "";
    width: 0;
    height: 0;
    // left: 40px;
    top: -10px;
    position: absolute;
    border: 10px solid transparent;
    transform: rotate(135deg);
    transition: border 0.3s ease-in-out;
  }
`;

export var TooltipCard = styled.div`
  position: relative;
  & ${TooltipButton}:hover + ${TooltipBox} {
    visibility: visible;
    color: ${(props) => props.theme.color};
    background-color: ${(props) => props.theme.background};
    &:before {
      border-color: transparent transparent ${(props) => props.theme.background}
        ${(props) => props.theme.background};
    }
  }
`;
