<script>
    import { onMount } from "svelte";
    // import { useParams } from "svelte-spa-router";

    import CornerLogo from "../tools/Corner_logo.svelte";
    import Navigation from "../tools/Navigation.svelte";

    /* TODO: Fetch docket from backend */

    // let docket = null;

    // const { id } = useParams();

    // onMount(async () => {
    //     const res = await fetch(`/api/dockets/${id}`);
    //     docket = await res.json();
    // });

    /* TODO: Add loading animation */
    // let _ = {
    //     // docket info
    //     occ_ID: docket.occ_ID,
    //     docket_ID: docket.docket_ID,
    //     relevant_officer: docket.relevant_officer,

    //     // offense info
    //     offense_category: docket.offense_category,
    //     day_of_offense: docket.day_of_offense,
    //     time_of_offense: docket.time_of_offense,
    //     offense_type: docket.offense_type,
    //     offense_description: docket.offense_description,
    //     crime_code: docket.crime_code,
    //     property_damage_or_injuries: docket.property_damage_or_injuries,

    //     // accused info
    //     accused_name: docket.accused_name,
    //     accused_surname: docket.accused_surname,
    //     accused_race: docket.accused_race,
    //     accused_gender: docket.accused_gender,
    //     accused_age: docket.accused_age,
    //     accused_description: docket.accused_description,
    //     accused_last_seen: docket.accused_last_seen,
    // };
    

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


<main class="main-content">
    <!-- Your content here -->

    <div class="docket-info" id="item">
        <h3>Docket Info</h3>
        <p>Occurrence ID: {docket_object.occ_ID}</p>
        <p>Docket ID: {docket_object.docket_ID}</p>
        <p>Relevant Officer: {docket_object.relevant_officer}</p>
    </div>

    <div class="offense-info" id="item">
        <h3>Offense Info</h3>
        <p>Offense Category:</p>
        <input bind:value={docket_object.offense_category} />
        <p>Day of Offense:</p>
        <input bind:value={docket_object.day_of_offense} />
        <p>Time of Offense:</p>
        <input bind:value={docket_object.time_of_offense} />
        <p>Offense Type:</p>
        <input bind:value={docket_object.offense_type} />
        <p>Offense Description:</p>
        <input bind:value={docket_object.offense_description} />
        <p>Crime Code:</p>
        <input bind:value={docket_object.crime_code} />
        <p>Property Damage or Injuries:</p>
        <input bind:value={docket_object.property_damage_or_injuries} />
    </div>
    
    <div class="accused-info" id="item">
        <h3>Accused Info</h3>
        <p>Accused Name:</p>
        <input bind:value={docket_object.accused_name} />
        <p>Accused Surname:</p>
        <input bind:value={docket_object.accused_surname} />
        <p>Accused Race:</p>
        <input bind:value={docket_object.accused_race} />
        <p>Accused Gender:</p>
        <input bind:value={docket_object.accused_gender} />
        <p>Accused Age:</p>
        <input bind:value={docket_object.accused_age} />
        <p>Accused Description:</p>
        <input bind:value={docket_object.accused_description} />
        <p>Accused Last Seen:</p>
        <input bind:value={docket_object.accused_last_seen} />
    </div>
    

 

</main>

<section>
    <button>Submit for Review</button>

</section>



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
