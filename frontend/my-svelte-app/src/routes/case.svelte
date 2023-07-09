<script>
	import CornerLogo from "../tools/Corner_logo.svelte";
    import Navigation from "../tools/Navigation.svelte";
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

                    <label>Time of offense:
                        <input
                            type="time"
                            id="offTime"
                            name="offTime"
                            required >
                    </label>

                    <p>Tick the relevant box:</p>
                       
                        <br/>
                        <input type = "checkbox" name = "Crime:" value = 1 /> Gender Based Violence
                        <input type = "checkbox" name = "Crime:" value = 1 /> Gang Related
                        <!-- <input type = "checkbox" name = "Shows:" value = 1 /> Railway Attack -->
                        <input type = "checkbox" name = "Crime:" value = 1 /> Police Involvement
                
                    <label>Nature and description of offense:
                    <br/>
                        <input
                            type="textarea"
                            id="offdesc"
                            name="offdesc"
                            required/>
                    </label>

                    <label> Crime Code:
                    <br/>
                        <input
                            type="text"
                            id="offCode"
                            name="offCode"
                            required
                        />
                    </label>

                    <label>Nature of property damage/injuries:
                        <br/>
                            <input
                                type="textarea"
                                id="offdesc"
                                name="offdesc"
                                required/>
                    </label>
                    
                    <input type="submit" id="off_details" value="Submit Offense Details" />
                </form>
            </div>
           
        </div>
        
    </div>

</main>

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

#offCode{
    margin-top: 2vh;
    margin-left: 5vh;
    width: 60vh;
}
#offdesc{
    margin-top: 2vh;
    margin-left: 5vh;
    height:10vh;
    width: 60vh;
}
/* .description{
    background-color: grey;
    padding: 2vh;
    color: white;
    width: 70vh;
    margin:5vh 10vh 2vh 5vh;
    height: 45vh;
} */

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

h2{
    color: black;
    text-align: center;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
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

.header{
        display: flex;
		background-color: #091D30;
		border-radius: 8px;
		text-align: center;
    }

.docket{
    background-color: #E8E8E8 ;
	height: 113vh;
	align-content: center;
}

</style> 