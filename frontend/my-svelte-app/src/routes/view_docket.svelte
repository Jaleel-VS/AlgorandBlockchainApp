<script>
    import { onMount } from "svelte";

    import CornerLogo from "../tools/Corner_logo.svelte";
    import Navigation from "../tools/Navigation.svelte";

    let docketId = null;
    
    const backendURL = "http://127.0.0.1:8000/";

    let docket = null;

    export let params = {};


    onMount(async () => {
        // Example GET REQUEST: http://127.0.0.1:8000/docket?docket_id=DOC0002
        docketId = params.id;
        const res = await fetch(`${backendURL}docket/?docket_id=${docketId}`);
        docket = await res.json();
    });




    let docket_object = {
        occ_ID: "123456789",
        docket_ID: "123456789",
        relevant_officer: "John Doe",

        // offense info
        offense_category: "Gender Based Violence",
        day_of_offense: "2021-05-01",
        time_of_offense: "18:30",
        offense_type: "Assault",
        offense_description: "Physical assault against a woman",
        crime_code: "ABC123",
        property_damage_or_injuries: "Minor injuries",

        // accused info
        accused_name: "Jane",
        accused_surname: "Doe",
        accused_race: "White",
        accused_gender: "Female",
        accused_age: 30,
        accused_description: "Tall with blonde hair",
        accused_last_seen: "2021-05-02",
        
        // hash info
        hash_link: "https://i",
        hash_date: "2021-05-02",
    };
</script>

<header class="header">
    <CornerLogo />
    <div class="navigation">
        <h1 id="cd">Dockets</h1>
        <Navigation />
    </div>
</header>

<h2>Docket Information</h2>

{#if docket}
<main class="main-content">
    <!-- Your content here -->

    <div class="docket-info" >
        <div class="feed" id="item">
            <h3> Feedback </h3>

            {#if docket.docket_feedback} 

            {#each docket.docket_feedback as feedback}
                <p>{feedback}</p>
            {/each}

            {:else}

            <p>No previous feedback</p>
            {/if}
        </div>
        <div class="info"id="item">
            <h3>Docket Info</h3>
            <p>Occurrence ID: {docket.occ_ID}</p>
            <p>Docket ID: {docket.docket_key}</p>
            <p>Relevant Officer: {docket.relevant_officer}</p>
        </div>
    </div>

    <div class="offense-info" id="item">
        <h3>Offense Info</h3>
        <p>Offense Category: {docket.offense_category}</p>
        <p>Day of Offense: {docket.day_of_offense}</p>
        <p>Time of Offense: {docket.time_of_offense}</p>
        <p>Offense Description: {docket.offense_description}</p>
        <p>Crime Code: {docket.crime_code}</p>
        <p>
            Property Damage or Injuries: {docket.property_damage_or_injuries}
        </p>
    </div>

    <div class="accused-info" id="item">
        <h3>Accused Info</h3>
        <p>Accused Name: {docket.accused_name}</p>
        <p>Accused Surname: {docket.accused_surname}</p>
        <p>Accused Race: {docket.accused_race}</p>
        <p>Accused Gender: {docket.accused_gender}</p>
        <p>Accused Age: {docket.accused_age}</p>
        <p>Accused Description: {docket.accused_description}</p>
        <p>Accused Last Seen: {docket.accused_last_seen}</p>
    </div>

 

</main>

<section>
    {#if docket.transcation_addresses}

    <h3>Transaction Addresses</h3>
    <p>The content of this docket and subsequent changes have been hashed <br> These hashes have been stored at the following addresses:</p>
    {#each docket.transcation_addresses as address}
    <!-- use anchor tags -->
    <a href="{address}" target="_blank">Transaction</a>
    {/each}
    {/if}
</section>
{/if}


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

    h2 {
        text-align: center;
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
        justify-content: center;
        /* align-items: center; */
        flex-direction: row;
        background-color: #d3d3d3; /* This is light gray color. Adjust to your liking */
        min-height: auto; /* Adjust to your liking */
        padding: 1rem; /* Adjust to your liking */
    }
    
    #item {
        background-color: white;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem;
        width: 25rem;
        height: auto;

    }

    h2 {
        margin-bottom: 1rem;
    }

    section {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        background-color: #d3d3d3; /* This is light gray color. Adjust to your liking */
        min-height: auto; /* Adjust to your liking */
        padding: 1rem; /* Adjust to your liking */
    }
</style>
