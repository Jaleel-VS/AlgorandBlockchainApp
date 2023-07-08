<script>
	//import officeer details from store
	import { officer } from "./store.js";

	import Router from "svelte-spa-router";
	import Login from "./routes/login.svelte";
	import Welcome from "./routes/welcome.svelte";
	import Occurrence from "./routes/occurrence.svelte";

	let routes = {
		"/": Login,
		"/welcome": Welcome,
		"/occurrence": Occurrence
	}

	officer.set({})
</script>

<main>
	<Router {routes}/> 
</main>

