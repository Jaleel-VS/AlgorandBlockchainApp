<script>
    import CornerLogo from "../tools/Corner_logo.svelte";
    import Navigation from "../tools/Navigation.svelte";


    // offense details
    let offense_type = "";
    let offdate = "";
    let offTime = "";
    let offense_category = "";
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
            offense_category: offense_category,
            day_of_offense: offdate,
            time_of_offense: offTime,
            offense_type: offense_type,
            offense_description: offdesc,
            crime_code:  offCode,
            property_damage_or_injuries: offNature,
            accused_name: firstname,
            accused_surname: lastname,
            accused_race: race,
            accused_gender: gender,
            accused_age: age,
            accused_description: description,
            accused_last_seen: lastSeen
        }

        console.log(dataObject);

        // const backendURL = "http://127.0.0.1:8000/";

        // try {
        //     const response = await fetch(`${backendURL}case`, {
        //         method: "POST",
        //         headers: {
        //             "Content-Type": "application/json",
        //         },
        //         body: JSON.stringify(dataObject),
        //     });

        //     const data = await response.json();
        //     console.log(data);
        // } catch (error) {
            
        // }

    }

</script>

<main>
    <div class="docket">
        <div class="header">
            <CornerLogo></CornerLogo>
            <div class="navigation">
				<h1 id="cd">CASE DOCKET</h1>
                <Navigation></Navigation>
			</div>
		</div>
        <h1>PART A</h1>
        <h2>OFFENSE DETAILS</h2>
        
        <div class="body">
            <div class="offense">
                <p>Select the category under which the offense falls:</p>
                <form id="offense_type">
                    <input id="once" type = "radio" name = "offense:" value = "Once-off" /> Once-off <br/>
				    <input id="going" type = "radio" name = "offense:" value = "On-going" /> On-going <br/>

                    <label>Day of offense:
                        <input
                            type="date"
                            id="offdate"
                            name="offdate"
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
                    </div>
                </div>

                <div class="description">
                    <div id="offense_description_div">
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
                    </div>
                </div>
            </div>

            <h1>PART B</h1>
            <h2>ACCUSED DETAILS</h2>

            <div class="body">
                <div class="offense">
                    <p>Accused First Name:</p>
                    <div id="firstname_div">
                        <input type="text" name="firstname" id="firstname" bind:value={firstname} />
                    </div>

                    <p>Accused Last Name:</p>
                    <div id="lastname_div">
                        <input type="text" name="lastname" id="lastname" bind:value={lastname} />
                    </div>

                    <p>Gender:</p>
                    <div id="gender_div">
                        <input id="male" type="radio" name="gender" bind:group={gender} value="Male" /> Male <br />
                        <input id="female" type="radio" name="gender" bind:group={gender} value="Female" /> Female <br />
                        <input id="non-binary" type="radio" name="gender" bind:group={gender} value="Non-Binary" /> Non-Binary <br />
                    </div>

                    <p>Race:</p>
                    <div id="race_div">
                        <input id="white" type="radio" name="race" bind:group={race} value="White" required /> White <br />
                        <input id="african" type="radio" name="race" bind:group={race} value="African" /> African <br />
                        <input id="asian" type="radio" name="race" bind:group={race} value="Asian" /> Asian <br />
                        <input id="coloured" type="radio" name="race" bind:group={race} value="Coloured" /> Coloured <br />
                    </div>
                </div>

                <div class="description">
                    <div id="accused_description_div">
                        <label>
                            Accused Age:
                            <br />
                            <input
                                type="textarea"
                                id="offdesc"
                                name="offdesc"
                                required/>
                    </label>
                    
                    <input type="submit" id="off_details" value="Submit Offense Details" />
                </form>
            </div>

            <button type="submit" id="off_details">Submit Offense Details</button>
        </div>
    </main>
</form>


<style>

#off_details{
    background-color: #091d30;
    color: white;
    text-align: center;
    margin-left: 83vh;
    width: 35vh;
    height: 6vh;
    border-radius: 10px;
    margin-top: 2vh ;
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
    .description {
        background-color: grey;
        padding: 2vh;
        color: white;
        width: 70vh;
        margin: 5vh 10vh 2vh 5vh;
        height: 45vh;
    }

p{
    font-weight: bold;
    margin-bottom: 1vh;
}
label{
    font-weight: bold;
}
.offense{
    padding: 2vh;
    background-color:grey;
    color: white;
    width: 70vh;
    margin:5vh 5vh 2vh 10vh;
    height: 45vh;
}

    h2 {
        color: black;
        text-align: center;
        font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
            sans-serif;
        font-size: 20px;
    }

h1{
    color: #091D30;
    text-align: center;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-size: 30px;
}
.body{
    background-color: white;
    width: 180vh;
    height: 60vh;
    margin: auto;
    display: flex;
}
#cd{
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

.docket{
    background-color: #E8E8E8 ;
	height: 113vh;
	align-content: center;
}

</style> 