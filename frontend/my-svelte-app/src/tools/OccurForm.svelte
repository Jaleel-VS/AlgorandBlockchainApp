<script>
    let name =""
    let surname =""
    let id =""
</script>
    

<form on:submit={saveData}>
    
    <div class="names">
        <label>Name:
            <input
                bind:value={name}
                type="text"
                id="name"
                name="name"
                required
                placeholder="e.g. Mmabatho"/>
        </label>
        <label> Surname:
            <input
                bind:value={surname}
                type="text"
                id="surname"
                name="surname"
                required
                placeholder="e.g. Mojapelo"
            /><br /><br />
        </label>
    </div>

    <label>Identification Number:
        <input
            bind:value={id}
            type="text"
            id="idNum"
            name="idNum"
            required
            placeholder="e.g. 0123456789123"/>
    </label>

    <h2>Contact Details</h2>

    <div class="phones">
        <label>Cell:
            <input
                bind:value={id}
                type="phone"
                id="cell"
                name="cell"
                required
                placeholder="e.g. (+27)78 256 7765"/>
        </label>

        <label>Home Phone:
            <input
                bind:value={id}
                type="phone"
                id="cell"
                name="cell"
                required
                placeholder="e.g. (+21)78 256 7765"/>
        </label>   
    </div>

    <label>E-mail address:
        <input
            bind:value={id}
            type="email"
            id="email"
            name="email"
            required
            placeholder="e.g. queen.charlotte@gmail.com"/>
    </label>

    <h2>Residential Address</h2>

    <input
        bind:value={id}
        type="text"
        id="address_1"
        name="address"
        required
    /><br /><br />

    <input
        bind:value={id}
        type="text"
        id="address_2"
        name="address"
        required
    /><br /><br />


</form>

<style>
    
    h2{
        color: #091D30;
        font-size: 15px;
        margin-left: 2vh;
    }
    .names {
        display: flex;
    }

    .phones{
        display: flex;
        margin-bottom: 2vh;
    }

    label{
        font-size: 12px;
        margin-left: 2vh;
        font-weight: bold;
        
    }

    #address_1, #address_2 {
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 10vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 60vh;
        border-radius: 10px;
        margin-bottom: 0%;
    }
    #cell{

        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 22vh;
        border-radius: 10px;

    }
    #idNum, #email{
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 44vh;
        border-radius: 10px;
    }
    #name{
        /* margin-top: 5vh; */
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 20vh;
        border-radius: 10px;
    }

    #surname {
        padding-left: 0.6vh;
        padding-top: 0.6vh;
        padding-bottom: 0.6vh;
        margin-left: 2vh;
        background-color: rgb(207, 207, 207);
        height: 5vh;
        width: 25vh;
        border-radius: 10px;
    }
</style>