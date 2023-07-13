<script>
    import { push } from "svelte-spa-router";

    import { occurrence, officer } from "../stores.js";
    import { onMount } from 'svelte';
    import PopUp from "./Pop_Up.svelte";

    const backendURL = "http://127.0.0.1:8000/";

    // get occurernce ID from backend when page loads
    onMount(async () => {
        const response = await getOccurrenceID();
        console.log(response);
        occurrenceID = response;
        // set occurrence in store
        occurrence.set(occurrenceID);
        
    });

    const goHome = () => {
        push("/welcome");
    };

    const createDocket = () => {
        push("/submit_docket");
    };

    let occurrenceSubmitted = false;

    let occurrenceID = "";
    let name = "";
    let surname = "";
    let id = "";
    let cellnum = "";
    let homephone = "";
    let email = "";
    let address_1 = "";
    let address_2 = "";
    let desc = "";
    let officer_obs = "";

    /* FAST API MODEL
    class Occurrence(BaseModel):
    #occID: str
    victim_name: str
    victim_surname: str
    victim_ID: str # Their id number 
    cellphone: str
    telephone: str
    email: str
    residential_address: str
    occurance_description: str 
    observations_other_info: str
    */

    const fillFieldsWithDummyData = () => {
        name = "Mmabatho";
        surname = "Mojapelo";
        id = "0123456789123";
        cellnum = "(+27)78 256 7765";
        homephone = "(+27)11 256 7765";
        email = "mm@gmail.com";
        address_1 = "1234";
        address_2 = "Mmabatho Street";
        desc = "I was robbed";
        officer_obs = "The victim was very scared";
    };

    const saveData = async () => {
        const getBadgeNumber = () => {
            return $officer.badgeID ? $officer.badgeID : "1234567890";
        };
        const datadic = {
            // occID: occurrenceID,
            victim_name: name,
            victim_surname: surname,
            victim_ID: id,
            cellphone: cellnum,
            telephone: homephone,
            email: email,
            residential_address: address_1 + " " + address_2,
            occurance_description: desc,
            observations_other_info: officer_obs,
            attending_officer_id: getBadgeNumber(),
        };

        const dummyDic = {
            victim_name: "string",
            victim_surname: "string",
            victim_ID: "string",
            cellphone: "string",
            telephone: "string",
            email: "string",
            residential_address: "string",
            occurance_description: "string",
            observations_other_info: "string",
            attending_officer_id: "string",
        };

        console.log(datadic);

        try {
            const response = await fetch(`${backendURL}log_occurrence`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(datadic),
            });
            const data = await response.json();
            console.log(data);

            if (data.success) {
                console.log("Occurrence successfully logged");
                occurrenceSubmitted = true;
            } else {
                console.log(data.message);
            }

            console.log("Data sent to the backend successfully");
        } catch (error) {
            console.error("Error sending data to the backend:", error);
        }
    };

    const getOccurrenceID = async() => {
        try {
            // get from backend
            const response = await fetch(`${backendURL}occurrence_number`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            });

            return response.json();
        }
        catch (error) {
            console.error("Error getting occurrence ID:", error);
        }

    }
</script>

<button on:click={fillFieldsWithDummyData}
    >Fill with dummy data (DELETE LATER)</button
>

<form on:submit|preventDefault={saveData}>
    <h2>OCCURRENCE ID: {occurrenceID}</h2>
    <div class="names">
        <label
            >Name:
            <input
                bind:value={name}
                type="text"
                id="name"
                name="name"
                required
                placeholder="e.g. Mmabatho"
            />
        </label>
        <label>
            Surname:
            <input
                bind:value={surname}
                type="text"
                id="surname"
                name="surname"
                required
                placeholder="e.g. Mojapelo"
            /><br /><br />
        </label>
    </div>

    <label
        >Identification Number:
        <input
            bind:value={id}
            type="text"
            id="idNum"
            name="idNum"
            required
            placeholder="e.g. 0123456789123"
        />
    </label>

    <h2>Contact Details</h2>

    <div class="phones">
        <label
            >Cell:
            <input
                bind:value={cellnum}
                type="phone"
                id="cell"
                name="cell"
                required
                placeholder="e.g. (+27)78 256 7765"
            />
        </label>

        <label
            >Home Phone:
            <input
                bind:value={homephone}
                type="phone"
                id="cell"
                name="cell"
                required
                placeholder="e.g. (+21)78 256 7765"
            />
        </label>
    </div>

    <label
        >E-mail address:
        <input
            bind:value={email}
            type="email"
            id="email"
            name="email"
            required
            placeholder="e.g. mmabatho.mojapelo@gmail.com"
        />
    </label>

    <h2>Residential Address</h2>

    <input
        bind:value={address_1}
        type="text"
        id="address_1"
        name="address"
        required
    /><br /><br />

    <input
        bind:value={address_2}
        type="text"
        id="address_2"
        name="address"
        required
    />

    <h1 id="v">Additional Information</h1>

    <h2>Occurrence Desciption</h2>

    <input bind:value={desc} type="textarea" id="desc" name="desc" required />

    <h2>Officer Observation/Any other information</h2>

    <input
        bind:value={officer_obs}
        type="textarea"
        id="desc"
        name="desc"
        required
    /><br /><br />
    {#if !occurrenceSubmitted}
        <button>Submit Occurrence</button>
    {/if}
</form>

{#if occurrenceSubmitted}
    <div class="postSubmit">
        <h2>Occurrence Submitted Successfully!</h2>

        <div class="buttons">
            <button on:click={goHome}>Exit</button>
            <button on:click={createDocket}>Create Docket</button>
        </div>

        <!-- <Modal show={$modal} closeButton={false}>
    
    <button on:click={showModal}>Proceed</button>
    </Modal> -->
    </div>
{/if}

<style>
    button {
        background-color: #091d30;
        color: white;
        text-align: center;
        margin-left: 26vh;
        width: 25vh;
        height: 6vh;
        border-radius: 10px;
    }

    #v {
        color: #091d30;
        font-size: 30px;
        margin: auto;
        text-align: center;
        margin-top: 2vh;
        margin-bottom: 1vh;
    }

    #desc {
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 10vh;
        background-color: rgb(207, 207, 207);
        height: 25vh;
        width: 60vh;
        border-radius: 10px;
        margin-bottom: 0%;
    }

    h2 {
        color: #091d30;
        font-size: 15px;
        margin-left: 2vh;
    }
    .names {
        display: flex;
    }

    .phones {
        display: flex;
        margin-bottom: 2vh;
    }

    label {
        font-size: 12px;
        margin-left: 2vh;
        font-weight: bold;
    }

    #address_1,
    #address_2 {
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 10vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 60vh;
        border-radius: 10px;
        margin-bottom: 0%;
    }
    #cell {
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 22vh;
        border-radius: 10px;
    }
    #idNum,
    #email {
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 44vh;
        border-radius: 10px;
    }
    #name {
        /* margin-top: 5vh; */
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 20vh;
        border-radius: 10px;
    }

    #surname {
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 25vh;
        border-radius: 10px;
    }

    /* .buttons {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        
    } */
</style>
