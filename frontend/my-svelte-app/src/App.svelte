<script>
	//import officeer details from store
	import { officer } from "./stores.js";

	import Router from "svelte-spa-router";
	import Login from "./routes/login.svelte";
	import Welcome from "./routes/welcome.svelte";
	import Occurrence from "./routes/occurrence.svelte";
	import Case from "./routes/case.svelte";
	import Accused from "./routes/accused.svelte";
	import Dockets from "./routes/dockets.svelte";

	let routes = {
		"/": Login,
		"/welcome": Welcome,
		"/occurrence": Occurrence,
		"/case": Case,
		"/accussed": Accused,
		"/dockets": Dockets,
	}

	officer.set({})
</script>

<main>
	<Router {routes}/> 
</main>

