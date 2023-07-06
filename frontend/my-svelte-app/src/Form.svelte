<script>
    // Define initial form data
    let username = "";
    let password = "";

    // Define the function to handle form submit
    async function saveData(event) {
        event.preventDefault();

        const datadic = { username: username, password: password };

        console.log(datadic);

        const backendURL = "http://127.0.0.1:8000/";

        try {
            const response = await fetch(`${backendURL}login_test`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(datadic),
            });
            const data = await response.json();
            console.log(data); 

            if (data.officerType === "regular") {
                console.log("regular officer successfully connected")
            } else if (data.officerType === "senior") {
                console.log("senior officer successfully connected")
            }

            console.log("Data sent to the backend successfully");
        } catch (error) {
            console.error("Error sending data to the backend:", error);
        }
    }
</script>

<form on:submit={saveData}>
    <input
        bind:value={username}
        type="text"
        id="name"
        name="name"
        required
        placeholder="Username"
    /><br /><br />
    <input
        bind:value={password}
        type="password"
        id="pass"
        name="password"
        required
        placeholder="Password"
    /><br /><br />
    <a href="https://www.youtube.com/watch?v=gdZLi9oWNZg&pp=ygUDYnRz"
        ><u><h2>I forgot my password</h2></u></a
    >
    <input type="submit" id="submit" value="Sign In" />
</form>

<style>
    #submit {
        background-color: #091d30;
        color: white;
        margin-top: 5vh;
        text-align: center;
        margin-left: 18vh;
        width: 25vh;
        height: 6vh;
        border-radius: 10px;
    }

    #name {
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

    #pass {
        padding-left: 2vh;
        padding-top: 2vh;
        padding-bottom: 2vh;
        margin-top: 2vh;
        margin-left: 5vh;
        background-color: rgb(207, 207, 207);
        height: 6vh;
        width: 50vh;
        border-radius: 10px;
    }

    h2 {
        color: #091d30;
        font-weight: 400;
        font-size: 1em;
        margin-left: 5vh;
        margin-top: 0;
        font-weight: 700;
    }
</style>
