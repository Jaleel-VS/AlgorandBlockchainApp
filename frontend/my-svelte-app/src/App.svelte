<script>
	//export let name;

	import Router from "svelte-spa-router";
	import Login from "./routes/login.svelte";
	import Welcome from "./routes/welcome.svelte";
	import Occurrence from "./routes/occurrence.svelte";
	import Case from "./routes/case.svelte";
	import Accussed from "./routes/accussed.svelte";

	let routes = {
		"/": Login,
		"/welcome": Welcome,
		"/occurrence": Occurrence,
		"/case": Case,
		"/accussed": Accussed
	}
</script>

<main>
	<Router {routes}/> 
</main>

