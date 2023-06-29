function saveData(event) {
    event.preventDefault();

    const tname = document.getElementById('name').value;
    const temail = document.getElementById('email').value;
    const tphone = document.getElementById('phone').value;
    const datadic = { name: tname, email: temail, phone: tphone };

    // Create a dictionary object

    const backendURL = "";
    // Send the dictionary object to the backend
    fetch(`${backendURL}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datadic)
    })
        .then(response => {
            if (response.ok) {
                // Request was successful
                console.log('Data sent to the backend successfully');
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