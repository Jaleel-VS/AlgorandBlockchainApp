<script>
	import CornerLogo from "../tools/Corner_logo.svelte";
    import Navigation from "../tools/Navigation.svelte";
</script>

<main>
    <div class="accussed">
        <div class="header">
            <CornerLogo></CornerLogo>
            <div class="navigation">
				<h1 id="cd">ACCUSSED INFORMATION</h1>
                <Navigation></Navigation>
			</div>
		</div>
        <div class="body">
            <div class="info">
                <h2>Particulars of Accussed</h2>
                <form class="accInfo">
                    <label>Name:
                        <input
                            type="text"
                            id="accname"
                            name="accname"
                            required >
                    </label>

                    <label>Surname:
                        <input
                            type="text"
                            id="accsurname"
                            name="accsurname"
                            required >
                    </label>

                    <label>Identification Number:
                        <input
                            type="text"
                            id="idNum"
                            name="idNum"
                            required
                            placeholder="e.g. 0123456789123"
                        />
                    </label>
                </form>
            </div>
            
        </div>
    </div>
</main>

<style>
    label{
        font-weight: bold;
        margin-left: 2vh;
    }

    #accsurname{
        margin-top: 2vh;
        padding-left: 2vh;
        padding-top: 2vh;
        padding-bottom: 2vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 6vh;
        width: 47vh;
        border-radius: 10px;
    }

    #accname{
        margin-top: 5vh;
        padding-left: 2vh;
        padding-top: 2vh;
        padding-bottom: 2vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 6vh;
        width: 50vh;
        border-radius: 10px;
    }
    .accussed{
    background-color: #E8E8E8 ;
	height: 113vh;
	align-content: center;
    }

    .body{
        background-color: white;
        width: 180vh;
        height: 60vh;
        margin-top: 5vh;
        margin: auto;
        display: flex;
    }

    .header{
        display: flex;
		background-color: #091D30;
		border-radius: 8px;
		text-align: center;
        margin-bottom: 8vh;
    }

    #cd{
    color: white;
    margin-left: 45vh;
	margin-top: 2vh;
	font-size: 50px;
	margin-bottom: 2vh;
}
</style>