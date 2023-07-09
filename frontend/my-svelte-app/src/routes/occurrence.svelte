<script>
    import CornerLogo from "../tools/Corner_logo.svelte";
    import Navigation from "../tools/Navigation.svelte";
    import OccurForm from "../tools/OccurForm.svelte";
</script>
<main>
    <div class="occurrence">

        <div class="header">
            <CornerLogo></CornerLogo>
			<div class="navigation">
				<h1>LOG OCCURRENCE</h1>
                <Navigation></Navigation>
			</div>
		</div>

        <div class="details">
            <div class="victim"> 
                <h1 id="v">Victim's Details</h1>
                <OccurForm></OccurForm>
            </div>
        </div>
    </div>

</main>

<style>

    .victim{
        background-color: white;
        height: 144vh;
        width: 80vh;
        margin:auto;
        margin-top: 5vh;
        border-radius: 10px;
    }

    .occurrence{
        background-color: #E8E8E8 ;
		height: 175vh;
		align-content: center;
    }

    .header{
        display: flex;
		background-color: #091D30;
		border-radius: 8px;
		text-align: center;
    }

    .navigation{
        text-align: center;
    }

    h1{
		color: white;
		margin-left: 55vh;
		margin-top: 2vh;
		font-size: 50px;
		margin-bottom: 2vh;
	}

    #v{
        color: #091D30;
        font-size: 30px;
        margin: auto;
        text-align: center;
        margin-bottom: 1vh;
    }


</style>