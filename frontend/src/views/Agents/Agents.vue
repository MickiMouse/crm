<template>
    <div class="content">
        <div class="row">
            <div class="col-12">

                <agents-table/>
            </div>
        </div>
        <router-view/>

    </div>

</template>

<script>
    import AgentsTable from "../../components/Agents/AgentsTable";
    import AgentsClients from "../../components/Agents/AgentsClients";
    import Notifications from "../../components/Dashboard/Notifications";
    import AgentsDetails from "../../components/Agents/AgentsDetails";

    export default {
        name: "Agents",
        components: {AgentsDetails, Notifications, AgentsClients, AgentsTable},
        data() {
            return {
                data: []
            }
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
            console.log(this.$store.getters.getAgentDetails)
        },
    }
</script>

<style scoped>

</style>