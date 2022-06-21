function change_status(e, status) {
    /** Find the span above this function call
     This span will contain the user_id in our custom made attribute
     data-visitor-id. Now we know which user we need to modify 
     */
    const span = e.target.closest('span.close');
    const user_id = span.getAttribute('data-visitor-id');

    const data = new FormData()
    data.append('user_id', user_id);
    data.append('status', status);

    /** AJAX request to the python function
    from the route markVisitor in app.py
    this will send the user_id and the new
    status to the python function, which 
    will properly update de database
    */
    return fetch('/markVisitor', {
        method: 'POST',
        body: data,
    }).then(function (response) {
        return response.json();
    }).then(function (response) {
        /** This part changes the status in the 
         browser without the need to refresh the page*/
        const statusNode = span.querySelector('b')
        if (statusNode) {
            statusNode.innerText = status
        }
    });
}

function accept(e) {
    change_status(e, 'infected');
}

function reject(e) {
    change_status(e, 'uninfected');
}
