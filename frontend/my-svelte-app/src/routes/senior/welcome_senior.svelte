<script>
	import { officer } from "../../stores.js";

	import CornerLogo from "../../tools/Corner_logo.svelte";

	import { push } from "svelte-spa-router";

	// import PopUp from "../tools/PopUp.svelte";
	// document.getElementById("logButt").onclick = function(){
	// 	location.href= "/#/occurrence"
	// }

	//For Pop Up
	// let popUp = document.getElementById(popUp)

	// function popFunction(){
	//  	popUp.classList.add("open-popup")
	// }
</script>

<main>
	<div class="welcome">
		<div class="header">
			<CornerLogo />
			<div class="instruction">
				{#if Object.keys($officer).length === 0}
					<h1>Welcome</h1>
					<h2>Please log in</h2>
				{:else}
					<h1>Welcome {$officer.rank} {$officer.surname}</h1>
					<h2>Please select one of the following</h2>
				{/if}
			</div>
		</div>
		<div class="body">
			
			<div class="view">
				<img
					id="log"
					src="https://cdn-icons-png.flaticon.com/512/72/72647.png"
					alt="occur"
				/>
				<p>Fill out the log when potential victims visit the station</p>
				<button
					on:click={() => {
						push("/review_dockets");
					}}>View Dockets for Review</button
				>
			</div>

			
		</div>
	</div>
</main>

<style>
	
	/* .open-popup{
		visibility: visible;
		top: 50%;
		transform: translate(-50%,-50%) scale(1);
	} */

	.welcome {
		background-color: #e8e8e8;
		height: 98vh;
		align-content: center;
	}

	/* Body */

	button {
		background-color: #091d30;
		border-radius: 10px;
		color: white;
		font-size: 15px;
		padding: 1vh;
		width: 45vh;
		cursor: pointer;
	}

	p {
		color: #091d30;
		font-size: 20px;
	}

	.body {
		display: flex;
        justify-content: center;
        align-items: center;
	}



	.view {
		/* height: 50vh;
		width: 45vh;
		margin: 5vh 10vh 10vh 10vh; */
		text-align: center;
	}

	img {
		width: 30vh;
		height: 30vh;
		margin-left: 1vh;
		margin-top: 5vh;
	}

	/* Header */

	.header {
		display: flex;
		background-color: #091d30;
		border-radius: 8px;
		text-align: center;
	}

	.instruction {
		text-align: center;
	}

	h2 {
		color: white;
		margin-left: 58vh;
		font-weight: 400;
		margin-top: 0%;
	}

	h1 {
		color: white;
		margin-left: 58vh;
		margin-top: 2vh;
		font-size: 50px;
		margin-bottom: 2vh;
	}
</style>
