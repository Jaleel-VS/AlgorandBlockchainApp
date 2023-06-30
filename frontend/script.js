function saveData(event) {
    event.preventDefault();

    // Show the loader
    document.getElementById('loader').style.display = 'block';

    const tname = document.getElementById('name').value;
    const temail = document.getElementById('email').value;
    const tphone = document.getElementById('phone').value;
    const datadic = { name: tname, email: temail, phone: tphone };

    // Create a dictionary object

    const backendURL = "http://127.0.0.1:8000/";
    // Send the dictionary object to the backend
    fetch(`${backendURL}docket_test`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datadic)
    }).then(response=> response.json())
        .then(response => {

            // Hide the loader
            document.getElementById('loader').style.display = 'none';

            if (response.success) {
                // Request was successful
                console.log('Data sent to the backend successfully');
                //console.log(response.message);
                document.getElementById('displayIDText').textContent = "Docket successfully created. The transaction ID is: "
                document.getElementById('displayID').textContent = response.transaction_id

                document.getElementById('displayHashText').textContent = "The transaction hash is: "
                document.getElementById('displayHash').textContent = response.transaction_hash

                document.getElementById('displayAddressText').textContent = "The hash can be viewed on the blockchain at: "
                document.getElementById('displayAddress').textContent = response.transaction_address
                document.getElementById('displayAddress').href = response.transaction_address
            } else {
                // Request failed
                console.error('Error sending data to the backend');
            }
        })
        .catch(error => {
            // Hide the loader
            document.getElementById('loader').style.display = 'none';

            console.error('Error sending data to the backend:', error);
        });
}