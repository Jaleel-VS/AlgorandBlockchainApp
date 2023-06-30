function saveData(event) {
    event.preventDefault();

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
            if (response.success) {
                // Request was successful
                console.log('Data sent to the backend successfully');
                //console.log(response.message);
                document.getElementById('displayData').textContent = response.transaction_hash
            } else {
                // Request failed
                console.error('Error sending data to the backend');
            }
        })
        .catch(error => {
            console.error('Error sending data to the backend:', error);
        });


    // const data = `Name: ${name}\nEmail: ${email}\nPhone: ${phone}`;
    // const blob = new Blob([data], { type: 'text/plain' });

    // const filename = 'data.txt';
    // const link = document.createElement('a');
    // link.href = URL.createObjectURL(blob);
    // link.download = filename;
    // link.click();

    // Display the data on the screen
    // document.getElementById('displayData').textContent = data;
}