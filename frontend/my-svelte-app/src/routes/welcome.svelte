<script>
	import { officer } from "../stores.js";

	import CornerLogo from "../tools/Corner_logo.svelte";

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
			<div class="occur">
				<img
					id="log"
					src="https://cdn-icons-png.flaticon.com/512/28/28811.png"
					alt="occur"
				/>
				<p>Fill out the log when potential victims visit the station</p>
				<button
					on:click={() => {
						push("/submit_occurrence");
					}}>Log Occurrence</button
				>
			</div>

			<div class="view">
				<img
					id="log"
					src="https://cdn-icons-png.flaticon.com/512/72/72647.png"
					alt="occur"
				/>
				<p>Fill out the log when potential victims visit the station</p>
				<button
					on:click={() => {
						push("/view_dockets");
					}}>View Dockets</button
				>
			</div>

			<div class="task">
				<img
					id="log"
					src="https://cdn-icons-png.flaticon.com/512/4345/4345573.png"
					alt="occur"
				/>
				<p>Fill out the log when potential victims visit the station</p>
				<button
					on:click={() => {
						push("/view_tasks");
					}}>View Tasks</button
				>
			</div>
		</div>
		<div class="pop" id="popUp">
			<h1 id="h1Pop">Choose one of the following</h1>
			<!-- <div class="choices">
				
				<div class="occurOnly">
					<img id="log" src="https://cdn-icons-png.flaticon.com/512/28/28811.png" alt="occur"/>
					<p id="log">Log an occurrence only</p>
					<button>Exit</button>
				</div>

			</div> -->
		</div>
	</div>
</main>

<style>
	#h1Pop {
		color: white;
	}
	.pop {
		text-align: center;
		background-color: gray;
		width: 150vh;
		height: 80vh;
		border-radius: 10px;
		position: absolute;
		top: 0;
		left: 50%;
		transform: translate(-50%, -50%) scale(0.1);
		opacity: 90%;
		visibility: hidden;
		transition: transform 0.5s, top 0.5s;
	}

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
	}

	.occur {
		height: 50vh;
		width: 45vh;
		margin: 5vh 10vh 10vh 15vh;
		text-align: center;
	}

	.view {
		height: 50vh;
		width: 45vh;
		margin: 5vh 10vh 10vh 10vh;
		text-align: center;
	}

	.task {
		height: 50vh;
		width: 45vh;
		margin: 5vh 10vh 10vh 10vh;
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
