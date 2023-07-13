<!-- When they click log occurrence, loader appears and the pop up shows -->
<main>
    <div class ="pop_up">
        <h1>Choose One of the following</h1>
        <div class="choices">
            <div id="justLog">
                <img
                    id="log"
                    src="https://cdn-icons-png.flaticon.com/512/28/28811.png"
                    alt="occur"
                />

                <p>Log an</p>
                <p>occurrence only</p>
                <button>Exit</button>    
            </div>
            
            <div id="newDoc">
                <img
                    id="log"
                    src="https://cdn-icons-png.flaticon.com/512/8064/8064858.png"
                    alt="occur"
                />
                
                <p>Create a New Docke </p>
                <p>using Fair Chance</p>
                <button>Exit</button>    
            </div>
                    
        </div>
    </div>
</main>

<style>

.pop_up button {
		background-color: #091d30;
		border-radius: 10px;
		color: white;
		font-size: 15px;
		padding: 1vh;
		width: 30vh;
		cursor: pointer;
        margin: auto;
        border-color: #091d30;
	}

#newDoc, #justLog{
    margin: auto;
}

.choices{
    display: flex;
}
img {
		width: 20vh;
		height: 20vh;
		margin-left: 1vh;
		margin-top: 5vh;
	}

    p {
		color: white;
		font-size: 15px;
	}

    h1{
        color: white;
    }
    .pop_up{

        background-color: grey;
        height: 70vh;
        width: 110vh;
        border-radius: 10px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);
        text-align: center;
        opacity: 95%;

        /* Code to hide Pop Up
        
        top: 0;
        transform: translate(-50%,-50%, scale(0.1));
        visibility:hidde;

        */

    }
</style>