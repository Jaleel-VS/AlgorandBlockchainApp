<script>
    import { onMount } from "svelte";
    import { push } from "svelte-spa-router";


    export let params = {};

    import CornerLogo from "../tools/Corner_logo.svelte";
    import Navigation from "../tools/Navigation.svelte";

    let docketId = null;
    
    const backendURL = "http://127.0.0.1:8000/";

    let docket = null;

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


    const submitDocket = async() => {
        try {
            const response = await fetch(`${backendURL}submit_docket_for_review?docket_id=${docketId}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(docket),
            });

            const data = await response.json();
            console.log(data);

            if (data.success) {
                alert("Docket submitted for review");
                push("/welcome");
            }
        } catch (error) {

        }
    }
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
        <p>Offense Category:</p>
        <input bind:value={docket.offense_category} />
        <p>Day of Offense:</p>
        <input bind:value={docket.day_of_offense} />
        <p>Time of Offense:</p>
        <input bind:value={docket.time_of_offense} />
        <p>Offense Description:</p>
        <input bind:value={docket.offense_description} />
        <p>Crime Code:</p>
        <input bind:value={docket.crime_code} />
        <p>Property Damage or Injuries:</p>
        <input bind:value={docket.property_damage_or_injuries} />
    </div>
    
    <div class="accused-info" id="item">
        <h3>Accused Info</h3>
        <p>Accused Name:</p>
        <input bind:value={docket.accused_name} />
        <p>Accused Surname:</p>
        <input bind:value={docket.accused_surname} />
        <p>Accused Race:</p>
        <input bind:value={docket.accused_race} />
        <p>Accused Gender:</p>
        <input bind:value={docket.accused_gender} />
        <p>Accused Age:</p>
        <input bind:value={docket.accused_age} />
        <p>Accused Description:</p>
        <input bind:value={docket.accused_description} />
        <p>Accused Last Seen:</p>
        <input bind:value={docket.accused_last_seen} />
    </div>
    

 

</main>

<section>
    <button
        on:click={
            () => {
                submitDocket()
            }
        }
    >Submit for Review</button>

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
        flex-wrap: wrap;
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

    .docket-info {
        display: flex;
        flex-direction: column;
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
