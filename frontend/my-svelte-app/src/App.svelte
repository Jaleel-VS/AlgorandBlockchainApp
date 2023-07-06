<script>
	//export let name;
	import Image from "./Image.svelte"
	import Form from "./Form.svelte"
</script>

<main>
	<!-- <h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p> -->
	<div class="body">
		<div class="logo">
			<h1>Fair Chance</h1>
			<Image src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/SAPS_badge.svg/800px-SAPS_badge.svg.png" alt="badge"/>
			<h2>Where justice meets trust, security and transparency</h2>
		</div>
		<div class="sign-in">
			<h1 id="sign">Sign In</h1>
			<h2 id="catch">To serve South Africans truthfully</h2>
			<Form></Form>
			
		</div>	
	</div>
	
</main>

<style>
	.logo{
		margin: 15vh 0vh 5vh 25vh;
		background-color: #091D30 ;
		width: 90vh;
		height: 70vh;
		text-align: center;
		
	}

	.sign-in{
		margin-top: 15vh;
		background-color: white;
		width: 59vh;
		height: 70vh;
	}

	.body{
		display: flex;
		background-color: #4A5158 ;
		height: 98vh;
		align-content: center;
	}
	main {
		background-color: #4A5158;
		viewport-fit: 0px;
	}

	#sign{
		color: black;
		text-transform: none;
		font-size: 3em;
		margin-left: 5vh;
		margin-top: 3vh;
		font-weight: 500;
		font-family: 'Calibri';
		margin-bottom: 0px;
	}

	h1 {
		margin-top: 3vh;
		color: white;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 500;
		font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
	}

	h2{
		color: white;
		font-size: 1.2em;
	}

	#catch{
		color:#091D30;
		font-weight: 400;
		font-size: 1em;
		margin-left: 5vh;
		margin-top: 0;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>