<script>
    import CornerLogo from "../tools/Corner_logo.svelte";
    import Navigation from "../tools/Navigation.svelte";

    import { occurrence, officer } from "../stores.js";
    import {push} from "svelte-spa-router";


    //docket_details
    let occID = $occurrence;
    let relevantOfficer = $officer.badgeID;
    // offense details
    let offense_category = "";
    let offdate = "";
    let offTime = "";
    let offdesc = "";
    let offCode = "";
    let offNature = "";

    // accused details
    let firstname = "";
    let lastname = "";
    let gender = "";
    let race = "";
    let age = "";
    let description = "";
    let lastSeen = "";

    // submitForm logic

    async function submitForm() {
        const dataObject = {
            occ_ID: occID,
            relevant_officer: relevantOfficer,
            offense_category: offense_category,
            day_of_offense: offdate,
            time_of_offense: offTime,
            offense_description: offdesc,
            crime_code: offCode,
            property_damage_or_injuries: offNature,
            accused_name: firstname,
            accused_surname: lastname,
            accused_race: race,
            accused_gender: gender,
            accused_age: age,
            accused_description: description,
            accused_last_seen: lastSeen,
            docket_status: "FOR_REVIEW",
            docket_feedback: [],
        };

        console.log(dataObject);

        const backendURL = "http://127.0.0.1:8000/";

        try {
            const response = await fetch(`${backendURL}submit_initial_docket`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(dataObject),
            });

            const data = await response.json();
            console.log(data);

            if (data.success) {
                alert("Case successfully submitted for review");
                push("/welcome");

            }
        } catch (error) {

        }
    }
</script>

<form on:submit|preventDefault={submitForm}>
    <div class="docket">
        <div class="header">
            <CornerLogo />
            <div class="navigation">
                <h1 id="cd">CASE DOCKET</h1>
                <Navigation />
            </div>
        </div>
        <h1>PART A</h1>
        <h2>OFFENSE DETAILS</h2>

        <div class="body">
            <div class="offense">
                <p>Select the category under which the offense falls:</p>
                <form id="offense_type">
                    <input
                        id="once"
                        type="radio"
                        name="offense:"
                        bind:group={offense_category}
                        value="Once-off"
                    />
                    Once-off <br />
                    <input
                        id="going"
                        type="radio"
                        name="offense:"
                        bind:group={offense_category}
                        value="On-going"
                    />
                    On-going <br />

                    <label
                        >Day of offense:
                        <input
                            type="date"
                            id="offdate"
                            name="offdate"
                            bind:value={offdate}
                            required
                        />
                    </label>

                    <label>
                        Time of offense:
                        <input
                            type="time"
                            id="offTime"
                            name="offTime"
                            bind:value={offTime}
                            required
                        />
                    </label>

                    <label>
                        Nature and description of offense:
                        <br />
                        <textarea
                            id="offdesc"
                            name="offdesc"
                            bind:value={offdesc}
                            required
                        />
                    </label>

                    <label>
                        Crime Code:
                        <br />
                        <input
                            type="text"
                            id="offCode"
                            name="offCode"
                            bind:value={offCode}
                            required
                        />
                    </label>

                    <label>
                        Nature of property damage/injuries:
                        <br />
                        <textarea
                            id="offNature"
                            name="offNature"
                            bind:value={offNature}
                            required
                        />
                    </label>
                </form>
            </div>
        </div>

        <h1>PART B</h1>
        <h2>ACCUSED DETAILS</h2>

        <div class="body2">
            <div class="accusedDetails">
                <p>Accused First Name:</p>
                <div id="firstname_div">
                    <input
                        type="text"
                        name="firstname"
                        id="firstname"
                        bind:value={firstname}
                    />
                </div>

                <p>Accused Last Name:</p>
                <div id="lastname_div">
                    <input
                        type="text"
                        name="lastname"
                        id="lastname"
                        bind:value={lastname}
                    />
                </div>

                <div class="gender_race">
                    <div class="gender">
                        <label
                            >Gender:
                            <br />
                            <br />
                            <input
                                id="male"
                                type="radio"
                                name="gender"
                                bind:group={gender}
                                value="Male"
                            />
                            Male <br />
                            <input
                                id="female"
                                type="radio"
                                name="gender"
                                bind:group={gender}
                                value="Female"
                            />
                            Female <br />
                            <input
                                id="non-binary"
                                type="radio"
                                name="gender"
                                bind:group={gender}
                                value="Non-Binary"
                            />
                            Non-Binary <br />
                        </label>
                    </div>

                    <div class="race">
                        <label
                            >Race:
                            <br />
                            <br />
                            <input
                                id="african"
                                type="radio"
                                name="race"
                                bind:group={race}
                                value="African"
                            />
                            African <br />
                            <input
                                id="asian"
                                type="radio"
                                name="race"
                                bind:group={race}
                                value="Asian"
                            />
                            Asian <br />
                            <input
                                id="coloured"
                                type="radio"
                                name="race"
                                bind:group={race}
                                value="Coloured"
                            />
                            Coloured <br />
                            <input
                                id="white"
                                type="radio"
                                name="race"
                                bind:group={race}
                                value="White"
                                required
                            />
                            White <br />
                        </label>

                       
                    </div>
                </div>

                <div id="accused_description_div">
                    <label
                    >Accuseed last seen:
                    <input
                        type="date"
                        id="offdate"
                        name="offdate"
                        bind:value={lastSeen}
                        required
                    />
                </label>
                    <label>
                        Accused Age:
                        <br />
                        <input
                            type="number"
                            id="accAge"
                            name="accAge"
                            bind:value={age}
                            required
                        />
                    </label>
                    
                    <label>
                        Accused Description:
                        <br />
                        <input
                            type="text"
                            id="accDes"
                            name="accAge"
                            bind:value={description}
                            required
                        />
                    </label>

                    <button id="off_details">Submit Accused Details</button>
                </div>
            </div>
        </div>
    </div>
</form>

<style>
    #accAge {
        height: 5vh;
        width: 10vh;
        margin-left: 5vh;
        margin-top: 2vh;
    }
    #firstname,
    #lastname {
        margin-left: 5vh;
        width: 60vh;
    }

    .gender_race {
        display: flex;
        margin-top: 2vh;
    }

    .gender {
        margin-right: 10vh;
        margin-left: 5vh;
    }
    #off_details {
        background-color: #091d30;
        color: white;
        text-align: center;
        margin-left: 18vh;
        width: 35vh;
        height: 6vh;
        border-radius: 10px;
        margin-top: 7vh;
    }

    #offCode {
        margin-top: 2vh;
        margin-left: 5vh;
        width: 60vh;
    }

    #offdesc {
        margin-top: 2vh;
        margin-left: 5vh;
        height: 10vh;
        width: 60vh;
    }

    #offNature {
        margin-top: 2vh;
        margin-left: 5vh;
        height: 10vh;
        width: 60vh;
    }

    p {
        color: #091d30;
        font-weight: bold;
        margin-bottom: 1vh;
    }
    label {
        color: #091d30;
        font-weight: bold;
    }
    .offense {
        padding: 2vh;
        background-color: grey;
        color: white;
        width: 70vh;
        margin: 5vh 5vh 2vh 5.5vh;
        height: 72vh;
    }

    .body2 {
        background-color: white;
        width: 85vh;
        height: 86vh;
        margin: auto;
        display: flex;
    }

    .accusedDetails {
        padding: 2vh;
        background-color: grey;
        color: white;
        width: 70vh;
        margin: 5vh 5vh 2vh 5.5vh;
        height: 64vh;
    }

    h2 {
        color: black;
        text-align: center;
        font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
            sans-serif;
        font-size: 20px;
    }

    h1 {
        color: #091d30;
        text-align: center;
        font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
            sans-serif;
        font-size: 30px;
    }
    .body {
        background-color: white;
        width: 85vh;
        height: 86vh;
        margin: auto;
        display: flex;
    }
    #cd {
        color: white;
        margin-left: 55vh;
        margin-top: 2vh;
        font-size: 50px;
        margin-bottom: 2vh;
    }

    .header {
        display: flex;
        background-color: #091d30;
        border-radius: 8px;
        text-align: center;
    }

    .docket {
        background-color: #e8e8e8;
        height: 240vh;
        align-content: center;
    }
</style>
