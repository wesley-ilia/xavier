import React from "react";
import Select from 'react-select';
import styled, { css } from 'styled-components'

export const StyledSelect = styled(Select)`
	background-color: ${props =>
    	props.theme.mode === 'dark' ? '#111' : '#EEE'};
	color: ${props =>
		props.theme.mode === 'dark' ? '#EEE' : '#111'};
`;