// This function allows Agents to accept hospital users

function change_status(e, status) {
    var span = e.target.closest('span.hospital');
    var hospitalId = span.getAttribute('data-hospital-id');
    /** Get the span which is closest to the button.
    This span will have an attribute which holds the hospital_id.
    This way, we know which hospital we need to modify.
    */
    var data = new FormData()
    data.append('hospitalId', hospitalId);
    data.append('status', status);
    /** AJAX post request to the python function
     hospitalAction() in app.py . This function
     simply updates a hospital's status in the database
     */
    return fetch('../hospitalAction', {
        method: 'POST',
        body: data,
    }).then(function (response) {
        return response.json();
    }).then(function (response) {
        /** remove the span after the button is pressed,
         as the hospital whose span we are on no longer has the 
         status 'pending'*/
        console.log(response);
        span.parentElement.removeChild(span);
    });
}

function accept(e) {
    change_status(e, 'accepted');
}

function reject(e) {
    change_status(e, 'rejected');
}
