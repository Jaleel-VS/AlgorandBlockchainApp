<form onsubmit="saveData(event)">
    <input type="text" id="name" name="name" required placeholder="Username"><br><br>
    <input type="password" id="pass" name="password" required placeholder="Password"><br><br>
    <a href="https://www.youtube.com/watch?v=gdZLi9oWNZg&pp=ygUDYnRz"><u><h2>I forgot my password</h2></u></a>
    <input type="submit" id="submit" value="Sign In">
</form>


<style>

    #submit{
        background-color: #091D30;
        color: white;
        margin-top: 5vh;
        text-align: center;
        margin-left: 18vh;
        width: 25vh;
        height: 6vh;
        border-radius: 10px;
    }

    

    #name{
        margin-top: 5vh;
        padding-left: 2vh;
        padding-top: 2vh;
        padding-bottom: 2vh;
        margin-left: 5vh;
        background-color: rgb(207, 207, 207);
        height: 6vh;
        width: 50vh;
        border-radius: 10px;
    }

    #pass{
        padding-left: 2vh;
        padding-top: 2vh;
        padding-bottom: 2vh;
        margin-top: 2vh;
        margin-left: 5vh;
        background-color:  rgb(207, 207, 207);
        height:6vh;
        width: 50vh;
        border-radius: 10px;
    }

    h2{
		color:#091D30;
		font-weight: 400;
		font-size: 1em;
		margin-left: 5vh;
		margin-top: 0;
        font-weight: 700;
        
	}
</style>

<script>
    function saveData(event) {
    event.preventDefault();

    // Show the loader
    //document.getElementById('loader').style.display = 'block';

    const username = document.getElementById('name').value;
    const password = document.getElementById('pass').value;
    const datadic = { name: username, password: password};

    // Create a dictionary object

    const backendURL = "http://127.0.0.1:8000/";
    // Send the dictionary object to the backend
    fetch(`${backendURL}login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datadic)
    }).then(response=> response.json())
        .then(response => {

            // Hide the loader
            //document.getElementById('loader').style.display = 'none';

            // if (response.success) {
            //     // Request was successful
            //     console.log('Data sent to the backend successfully');
            //     //console.log(response.message);
            //     document.getElementById('displayIDText').textContent = "Docket successfully created. The transaction ID is: "
            //     document.getElementById('displayID').textContent = response.transaction_id

            //     document.getElementById('displayHashText').textContent = "The transaction hash is: "
            //     document.getElementById('displayHash').textContent = response.transaction_hash

            //     document.getElementById('displayAddressText').textContent = "The hash can be viewed on the blockchain at: "
            //     document.getElementById('displayAddress').textContent = response.transaction_address
            //     document.getElementById('displayAddress').href = response.transaction_address
            // } else {
                // Request failed
                console.error('Error sending data to the backend');
         //   }
        })
        .catch(error => {
            // Hide the loader
            //document.getElementById('loader').style.display = 'none';

            console.error('Error sending data to the backend:', error);
        });
}
</script>