<script>
	import {officer} from "../stores.js";

	import CornerLogo from "../tools/Corner_logo.svelte";
</script>

<main>
	<div class="welcome">
		<div class="header">
			<CornerLogo></CornerLogo>
			<div class="instruction">

				{#if Object.keys($officer).length === 0}
					<h1>Welcome</h1>
					<h2>Please log in</h2>
				{:else}
					<h1>Welcome {$officer.rank} {officer.surname}</h1>
					<h2>Please select one of the following</h2>
				{/if}
			</div>
		</div>
		<div class="body">
			<div class="occur">
				<img id="log" src="https://cdn-icons-png.flaticon.com/512/28/28811.png" alt="occur"/>
				<p>Fill out the log when potential victims visit the station</p>
				<button>Log Occurrence</button>
			</div>

			<div class="view">
				<img id="log" src="https://cdn-icons-png.flaticon.com/512/72/72647.png" alt="occur"/>
				<p>Fill out the log when potential victims visit the station</p>
				<button>View Dockets</button>
			</div>

			<div class="task">
				<img id="log" src="https://cdn-icons-png.flaticon.com/512/4345/4345573.png" alt="occur"/>
				<p>Fill out the log when potential victims visit the station</p>
				<button>View Tasks</button>
			</div>
		</div>
	</div>
   
</main>

<style>
 	
	.welcome{
		background-color: #E8E8E8 ;
		height: 98vh;
		align-content: center;
	}

	/* Body */

	button{
		background-color: #091D30;
		border-radius: 10px;
		color: white;
		font-size: 15px;
		padding: 1vh;
		width:45vh;
	}
	
	p{
		color: #091D30;
		font-size: 20px;
		
	}

	.body{
		display: flex;
	}

	.occur{
		
		height: 50vh;
		width: 45vh;
		margin: 5vh 10vh 10vh 15vh;
		text-align: center;
	}

	.view{
		
		height: 50vh;
		width: 45vh;
		margin: 5vh 10vh 10vh 10vh;
		text-align: center;

	}

	.task{
		
		height: 50vh;
		width: 45vh;
		margin: 5vh 10vh 10vh 10vh;
		text-align: center;
	}

	img{
		width: 30vh;
		height: 30vh;
		margin-left: 1vh;
		margin-top: 5vh;

	}

	/* Header */
	
	.header{
		display: flex;
		background-color: #091D30;
		border-radius: 8px;
		text-align: center;

	}

	.instruction{
		text-align: center;
	}

	h2{
		color: white;
		margin-left: 58vh;
		font-weight: 400;
		margin-top: 0%;
	}

	h1{
		color: white;
		margin-left: 58vh;
		margin-top: 2vh;
		font-size: 50px;
		margin-bottom: 2vh;
	}

</style>