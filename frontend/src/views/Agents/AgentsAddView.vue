<template>
    <div class="row py-3">
        <div class="col-6">
         <agents-add/>
        </div>

    </div>
</template>

<script>
    import AgentsClients from "../../components/Clients/AgentsClients";
    import Notifications from "../../components/Dashboard/Notifications";
    import AgentsDetails from "../../components/Agents/AgentsDetails";
    import AgentsAdd from "../../components/Agents/AgentsAdd";
    export default {
        name: "AgentsAddView",
        components: {AgentsAdd},
    }
</script>

<style scoped>

</style>