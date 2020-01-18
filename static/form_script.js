function showSelectiveOptions() {
    /* selecting the div that contains the optional input tags 
    that should appear only if the user selects the pdf option */
    seletiveDiv = document.getElementById('selectivePdfOptions')
    
    // making the input tags visible
    seletiveDiv.style.display = 'block'

    // selecting the 'header and footer included' radio input tag 
    yesBannerInput = seletiveDiv.children[0]
    
    // making the 'header and footer included' radio input tag checked
    yesBannerInput.checked = true

}

function hideSelectiveOptions() {
    /* selecting the div that contains the optional input tags 
    that should appear only if the user selects the pdf option */
    seletiveDiv = document.getElementById('selectivePdfOptions')
    
    // making the input tags INvisibile
    seletiveDiv.style.display = 'none'

    // selecting the 'header and footer included' radio input tag 
    yesBannerInput = seletiveDiv.children[0]

    // removing the 'header and footer included' radio input tag UNchecked
    yesBannerInput.checked = false
}
