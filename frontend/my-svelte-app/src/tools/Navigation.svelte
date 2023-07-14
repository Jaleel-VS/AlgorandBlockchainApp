<!-- This is a navigation bar -->

<!-- <script>
    import { page } from "$app/stores"

    const tabs = [
        {
            title: "HOME",
            href:"/#/welcome"
        },

        {
            title: "LOG OCCURRENCE",
            href:"/#/occurrence"
        },

        {
            title: "VIEW DOCKETS",
            href:"/#/occurrence"
        },

        {
            title: "TASKS",
            href:"/#/occurrence"
        },
    ]

    let routeID;
    $:  routeID = $page.route.id;
</script> -->

<nav>
    
    <ul class="bar">

        <!-- {#each tabs as {title, href}}
            <li>
                <a {href} class:active={routeID = href}>{title}</a>
            </li>
        {/each} -->

        <li>
             <a href="/#/welcome">HOME</a>
             
        </li>
        <li>|</li>
        <li>
            <a href="/#/occurrence">LOG OCCURRENCE</a>
        </li>
        <li>|</li>
        <li>
            <a href="/#/dockets">VIEW DOCKETS</a>
        </li>
        <li>|</li>
        <li>
            <a href="/#/tasks">TASKS</a>
        </li>
    </ul>
        
    
</nav>

<style>

    a {
        color: white;
    }
    ul{
        margin-left: 47.5vh;
        display: flex;
        flex-wrap: wrap;
    }

    li{
        list-style: none;
        margin-left: 2vh;
    }
</style>