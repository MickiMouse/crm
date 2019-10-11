<template>
    <div class="content">
        <div class="row">
            <div class="col-12">
                <clients-table/>
            </div>
        </div>
        <div class="row py-3" v-if="$store.getters.getClientDetails">
            <div class="col-12">
                <clients-details class="mb-3"/>
                <clients-table-i-p class="mb-3"/>
                <clients-table-workers class="mb-3"/>
            </div>
            <div class="col-6">
                <notifications
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
                        :header="'Комментарии'"
                        :icon="['far' ,'comment-alt']"
                />

            </div>
            <div class="col-6">
                <notifications
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
                        :header="'Последние уведомления'"
                        :icon="['far' ,'bell']"
                />

            </div>
        </div>
    </div>

</template>

<script>
    import AgentsTable from "../components/Agents/AgentsTable";
    import AgentsClients from "../components/Agents/AgentsClients";
    import Notifications from "../components/Dashboard/Notifications";
    import AgentsDetails from "../components/Agents/AgentsDetails";
    import ClientsTable from "../components/Clients/ClientsTable";
    import ClientsDetails from "../components/Clients/ClientsDetails";
    import ClientsTableIP from "../components/Clients/ClientsTableIP";
    import ClientsTableWorkers from "../components/Clients/ClientsTableWorkers";

    export default {
        name: "Clients",
        components: {ClientsTableWorkers, ClientsTableIP, ClientsDetails, ClientsTable, Notifications},
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