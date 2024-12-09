let generalTextStyling = (query) => {
    // Text general styling
    document.querySelector(query).style.textAlign = 'center';
    document.querySelector(query).style.marginTop = '20px';
    document.querySelector(query).style.fontSize = '50px';
}

// Section 1 Event
let checkSectionOne = (event) => {
    let button = event.target;

    if (button.innerHTML.toLowerCase() == 'c') {
        button.style.backgroundColor = 'green';
        document.querySelector('#feedback-1').innerHTML = 'Correct';
        document.querySelector('#feedback-1').style.color = 'green';
    }
    else {
        button.style.backgroundColor = 'red';
        document.querySelector('#feedback-1').innerHTML = 'Incorrect';
        document.querySelector('#feedback-1').style.color = 'red';
    }
    
    generalTextStyling('#feedback-1');
}

// Section 2 Event
let checkSectionTwo = (event) => {
    let button = event.target;
    let input = document.querySelector('input');
    
    if (input.value.toLowerCase() == 'python') {
        button.style.backgroundColor = 'green';
        document.querySelector('#feedback-2').innerHTML = 'Correct';
        document.querySelector('#feedback-2').style.color = 'green';
    }
    else {
        button.style.backgroundColor = 'red';
        document.querySelector('#feedback-2').innerHTML = 'Incorrect';
        document.querySelector('#feedback-2').style.color = 'red';
    }

    generalTextStyling('#feedback-2');
}

