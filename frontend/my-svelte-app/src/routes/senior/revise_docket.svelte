<script>
    import { onMount } from "svelte";
    import{officer} from "../../stores.js";
    // import { params } from 'svelte-spa-router';

    export let params = {};


    import CornerLogo from "../../tools/Corner_logo.svelte";
    import Navigation from "../../tools/Navigation.svelte";
    import { push } from "svelte-spa-router";


    // Subscribe to params to get the id
    // $params.subscribe(($params) => {
    let docketId = null;
    // });

    const backendURL = "http://127.0.0.1:8000/";

    /* TODO: Fetch docket from backend */

    let docket = null;
    let feedback = "";



    onMount(async () => {
        // Example GET REQUEST: http://127.0.0.1:8000/docket?docket_id=DOC0002
        docketId = params.id;
        const res = await fetch(`${backendURL}docket/?docket_id=${docketId}`);
        docket = await res.json();
        console.log(docket);
        console.log(docket.occ_ID);
    });


    let approved = true;

    const approval = (status) => {
        approved = status;

        if (approved) {
            submitDocket();
        }
    };

    const submitDocket = async() => {

        try {
            const res = await fetch(`${backendURL}approve_docket?docket_id=${docketId}`,
            {
                method: "POST",
                headers: {
                    "accept": "application/json",
                },
            }
            );
            const data = await res.json();
            console.log(data);

            if (data.success) {
                alert("Case successfully approved");
                push("/welcome_senior");

            }
        } catch (error) {

        }
        
    }

    const getCurrentDateTime = () => {
        // format 31/12/2021 23:59

        let today = new Date();
        let date = today.getDate() + "/" + (today.getMonth() + 1) + "/" + today.getFullYear();
        let time = today.getHours() + ":" + today.getMinutes();
        let dateTime = date + " " + time;

        return dateTime;
    }

    const submitFeedback = async () => {
        let feedbackString = `Date: ${getCurrentDateTime()} Feedback: ${feedback}`
        // Officer: ${officer.rank} ${officer.surname}

        try {
            const res = await fetch(`${backendURL}update_feedback?docket_id=${docketId}&feedback=${feedbackString}`,
            {
                method: "POST",
                headers: {
                    "accept": "application/json",
                },
            }
            );

            console.log(res);

            if (res.status == 200) {
                alert("Feedback submitted successfully");
                push("/welcome_senior");
            } else {
                alert("Feedback submission failed");
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
    <div class="previous" id="item">
        <h3>Previous Feedback</h3>
        {#if docket.docket_feedback} 

        {#each docket.docket_feedback as feedback}
            <p>{feedback}</p>
        {/each}

        {:else}

        <p>No previous feedback</p>
        {/if}
            
    </div>
    
    <div class="docket-info" id="item">
        <h3>Docket Info</h3>
        <p>Occurrence ID: {docket.occ_ID}</p>
        <p>Docket ID: {docket.docket_key}</p>
        <p>Relevant Officer: {docket.relevant_officer}</p>
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
    <button on:click={() => approval(false)}>Reject</button>


    {#if approved}
    <button on:click={() => approval(true)}>Approve</button>
    {/if}

    {#if !approved}
    Enter feedback:
    <form action="">
        <input type="text" placeholder="enter feedback" bind:value={feedback} required/>
        <button
            on:click|preventDefault={() => submitFeedback()}
        >Submit</button>
    </form>
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
        width: 30%;
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
