<script>
	//import officeer details from store
	import { officer, occurrence} from "./stores.js";

	import Router from "svelte-spa-router";
	import Login from "./routes/login.svelte";
	import Welcome from "./routes/welcome.svelte";
    import ReviseDocket from "./routes/senior/revise_docket.svelte";
    import SubmitDocket from "./routes/submit_docket.svelte";
    import ReviewDocket from "./routes/review_docket.svelte";
    import ViewDocket from "./routes/view_docket.svelte";
    import ViewDockets from "./routes/view_dockets.svelte";
    import ViewTasks from "./routes/view_tasks.svelte";
    import SubmitOccurrence from "./routes/submit_occurrence.svelte";
    import WelcomeSenior from "./routes/senior/welcome_senior.svelte";
    import ReviewDockets from "./routes/senior/revise_dockets.svelte";
	import PopUp from "./tools/Pop_Up.svelte";


	let routes = {
		"/": Login,
		"/welcome": Welcome,
		"/welcome_senior": WelcomeSenior,
		"/submit_occurrence": SubmitOccurrence,
		"/revise_docket/:id": ReviseDocket,
		"/submit_docket": SubmitDocket,
		"/view_docket/:id": ViewDocket,
		"/view_dockets": ViewDockets,
		"/view_tasks": ViewTasks,
		"/review_dockets": ReviewDockets,
		"/review_docket/:id": ReviewDocket,
	}

	officer.set({})
	occurrence.set("")
</script>

<main>
	<Router {routes}/> 
</main>

