function flashError(msg) {
    // the parent div that's meant to contain all the error messages
    let container = document.getElementById('messageContainer')

    // creating a temp div that's meant for showing message
    let errMsgDiv = document.createElement('div')
    
    // adding a class that will style the message accordingly
    errMsgDiv.classList.add('messageFlash')
    
    // putting text inside it
    errMsgDiv.innerText = String(msg)

    // temporarily displaying the error
    // since it's a div, 'block' is the most logical
    // choice for the display type
    errMsgDiv.style.display = 'block'
    
    // appending the temporary errMsgDiv to display it to the user
    container.appendChild(errMsgDiv)

    // removing the error message after 3000 milliseconds i.e. 3 seconds
    // also emptying the text inside
    setTimeout( () => {
        // setting diplay to none, before removing it
        errMsgDiv.style.display = 'none'
        
        // emptying the inner text
        errMsgDiv.innerText = ''

        // removing the errMsgDiv from the parent container div
        container.removeChild(errMsgDiv)
        
        console.log('removed the current child')
    }, 3000)
}
