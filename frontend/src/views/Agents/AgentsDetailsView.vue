<template>
    <div class="row py-3" v-if="$store.getters.getAgentDetails">
        <div class="col-6">
           <agents-details/>
            <notifications
                    class="mt-3"
                    :items="[
                        {
                            agent: {
                                user: {
                                email: 'admin@soft.com',
                                full_name: 'Dennis Pashnev',
                                username: 'admin'
                                }
                                },
                            created_at: '09.26.2019 12:06:38',
                            mess: 'ТЕСТИМ'
                        }
                        ]"
                    :header="'Сообщения'"
                    :icon="['far' ,'envelope']"
            />
        </div>
        <div class="col-6">
            <agents-clients/>
        </div>
    </div>
</template>

<script>
    import AgentsClients from "../../components/Clients/AgentsClients";
    import Notifications from "../../components/Dashboard/Notifications";
    import AgentsDetails from "../../components/Agents/AgentsDetails";
    export default {
        name: "AgentsDetailsView",
        components: {AgentsDetails, Notifications, AgentsClients}
    }
</script>

<style scoped>

</style>