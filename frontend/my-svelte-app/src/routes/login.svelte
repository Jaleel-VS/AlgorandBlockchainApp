<script>
	import Image from "../tools/Image.svelte"
	import Form from "../tools/LogInForm.svelte"
</script>

<main>
	<div class="body">
		<div class="logo">
			<h1>Fair Chance</h1>
			<Image src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/SAPS_badge.svg/800px-SAPS_badge.svg.png" alt="badge"/>
			<h2>Where justice meets trust, security, and transparency</h2>
		</div>
		<div class="sign-in">
			<h1 id="sign">Sign In</h1>
			<h2 id="catch">To serve South Africans truthfully</h2>
			<Form></Form>
		</div>	
	</div>
</main>

<style>
	.logo {
		margin: 15vh 0vh 5vh 25vh;
		background-color: #091D30;
		width: 90vh;
		height: 70vh;
		text-align: center;
	}

	.sign-in {
		margin-top: 15vh;
		background-color: white;
		width: 59vh;
		height: 70vh;
	}

	.body {
		display: flex;
		background-color: #4A5158;
		height: 98vh;
		align-content: center;
	}

	main {
		background-color: #4A5158;
		viewport-fit: 0px;
	}

	#sign {
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

	h2 {
		color: white;
		font-size: 1.2em;
	}

	#catch {
		color: #091D30;
		font-weight: 400;
		font-size: 1em;
		margin-left: 5vh;
		margin-top: 0;
	}

	@media (max-width: 640px) {
		.body {
			flex-direction: column;
			align-items: center;
		}

		.logo {
			width: 80%;
			height: 40vh;
			margin: 10vh auto;
		}

		.sign-in {
			width: 80%;
			height: 50vh;
			margin-top: 10vh;
		}

		h1 {
			font-size: 2em;
		}

		h2 {
			font-size: 1em;
		}

		#sign {
			font-size: 2em;
		}

		#catch {
			font-size: 0.8em;
		}
	}

	@media (max-width: 480px) {
		.logo {
			width: 90%;
			height: 30vh;
			margin: 5vh auto;
		}

		.sign-in {
			width: 90%;
			height: 40vh;
			margin-top: 5vh;
		}

		h1 {
			font-size: 1.5em;
		}

		h2 {
			font-size: 0.9em;
		}

		#sign {
			font-size: 1.5em;
		}

		#catch {
			font-size: 0.7em;
		}
	}
</style>
