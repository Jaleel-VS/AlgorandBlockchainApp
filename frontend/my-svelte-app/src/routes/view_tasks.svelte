<script>
    import CornerLogo from "../tools/Corner_logo.svelte";
    import Navigation from "../tools/Navigation.svelte";

    import { onMount } from "svelte";

    import {push} from "svelte-spa-router";

    /* TODO: Fetch tasks/dockets from backend */
    
    const backendURL = "http://127.0.0.1:8000/";

    onMount(async() =>
    {
        await getDockets();
    }
    )

    let dockets = [];

    const getDockets = async() => {
        try {
            fetch(`${backendURL}dockets/`)
                .then((response) => response.json())
                .then((data) => {
                    // filter only dockets that are for review
                    dockets = data.filter((docket) => docket.docket_status === "PENDING");
                });
        } catch (error) {
            console.log(error);
        }
    }



</script>

<header class="header">
    <CornerLogo />
    <div class="navigation">
        <h1 id="cd">Tasks</h1>
        <Navigation />
    </div>
</header>

<main class="main-content">
    <!-- Your content here -->
    <h2>List of Tasks</h2>
    <table>
        <thead>
            <tr>
                <th>Docket ID</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            {#each dockets as docket (docket._id)}
                <tr>
                    <td>{docket.docket_key}</td>
                    <td><button
                        on:click={() => {push(`/review_docket/${docket.docket_key}`)}}
                        >Ammend</button></td>
                </tr>
            {/each}
        </tbody>
    </table>
</main>

<style>
    .header {
        display: flex;
        background-color: #091d30;
        border-radius: 8px;
        text-align: center;
    }

    h1 {
        color: #091d30;
        text-align: center;
        font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
            sans-serif;
        font-size: 30px;
    }

    #cd {
        color: white;
        margin-left: 55vh;
        margin-top: 2vh;
        font-size: 50px;
        margin-bottom: 2vh;
    }

    .main-content {
        display: flex;
        /* justify-content: center; */
        align-items: center;
        flex-direction: column;
        background-color: #d3d3d3; /* This is light gray color. Adjust to your liking */
        min-height: 100vh; /* Adjust to your liking */
        padding: 1rem; /* Adjust to your liking */
    }

    h2 {
        margin-bottom: 1rem;
    }

    table {
        width: 100%;
        max-width: 800px;
        border-collapse: collapse;
    }

    th, td {
        border: 1px solid #000;
        padding: 1rem;
        text-align: left;
    }

    tr {
        background-color: #fff;
    }

    button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        transition-duration: 0.4s;
        cursor: pointer;
    }

    button:hover {
        background-color:darkgreen;
    }
</style>
