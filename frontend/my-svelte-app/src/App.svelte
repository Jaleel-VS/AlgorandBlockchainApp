<script>
	//export let name;

	import Router from "svelte-spa-router";
	import Login from "./routes/login.svelte";
	import Welcome from "./routes/welcome.svelte";
	import Occurrence from "./routes/occurrence.svelte";

	let routes = {
		"/": Login,
		"/welcome": Welcome,
		"/occurrence": Occurrence
	}
</script>

<main>
	<Router {routes}/> 
</main>

