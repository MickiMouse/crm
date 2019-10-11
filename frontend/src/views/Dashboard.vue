<template>
    <div class="content">
        <div class="row">
            <div class="col-5">
                <paid-contracts class="h-100" :data="data.pie_chart"/>
            </div>
            <div class="col-7">
                <dynamics-clients class="h-100" :x="data.line_chart.x" :y="data.line_chart.y"/>
            </div>
        </div>
        <div class="row py-4">
            <div class="col-4">
                <info-card :icon="['fas' ,'dollar-sign']" :value="data.total_amount" :header="'Общая сумма'"/>
            </div>
            <div class="col-4">
                <info-card :icon="['fas' ,'users']" :value="data.count_clients" :header="'Клиентов'"/>
            </div>
            <div class="col-4">
                <info-card :icon="['fas' ,'users']" :value="data.agents_count" :header="'Агентов'"/>
            </div>
        </div>
        <div class="row">
            <div class="col-7">
                <expand-table :items="data.rating" :fields="raiting_fields"
                              :header="'Агенты с низкой оценкой'"
                              :icon="['fas' ,'users']"
                              class="mb-3"/>
                <expand-table :items="data.clients" :fields="clients_fields"
                              :header="'Клиенты с истикающими договорами'"
                              :icon="['fas' ,'users']"
                              class="mb-3"/>
            </div>
            <div class="col-5" v-if="data.messages">
                <notifications
                        :items="data.messages"
                        :header="'Уведомления'"
                        :icon="['far' ,'bell']"
                />
            </div>
        </div>
    </div>
</template>

<script>
    import PaidContracts from "../components/Dashboard/paidContracts";
    import DynamicsClients from "../components/Dashboard/dynamicsClients";
    import InfoCard from "../components/Dashboard/infoCard";
    import ExpandTable from "../components/Tables/expandTable";
    import Notifications from "../components/Dashboard/Notifications";
    import axios from 'axios';

    export default {
        name: "Dashboard",
        components: {Notifications, ExpandTable, InfoCard, DynamicsClients, PaidContracts},
        data() {
            return {
                raiting_fields: [
                    {
                        key: 'pk',
                        label: '№',
                        class: 'table-header'
                    },
                    {
                        key: 'username',
                        label: 'ФИО агента',
                        class: 'table-header table-accent'
                    },
                    {
                        key: 'mark',
                        label: 'Оценка',
                        class: 'table-header'
                    }
                ],
                client_items: [
                ],
                clients_fields: [
                    {
                        key: 'pk',
                        label: '№',
                        class: 'table-header'
                    },
                    {
                        key: 'first_name',
                        label: 'Компания',
                        class: 'table-header table-accent'
                    },
                    {
                        key: 'full_name',
                        label: 'Агент',
                        class: 'table-header table-accent'
                    },
                    {
                        key: 'expiration_date',
                        label: 'Дата окончания',
                        class: 'table-header'
                    }
                ],
                agent_items: [
                    {age: 40, first_name: 'Dickerson', last_name: 'Macdonald', date: '2019/08/16'},
                    {age: 21, first_name: 'Larsen', last_name: 'Shaw', date: '2019/08/16'},
                    {age: 89, first_name: 'Geneva', last_name: 'Wilson', date: '2019/08/16'},
                    {age: 38, first_name: 'Jami', last_name: 'Carney', date: '2019/08/16'},
                    {age: 89, first_name: 'Geneva', last_name: 'Wilson', date: '2019/08/16'},
                    {age: 38, first_name: 'Jami', last_name: 'Carney', date: '2019/08/16'}
                ],

                data: {
                    agents_count: 2,
                    clients: [],
                    count_clients: 3,
                    line_chart: {
                        x:[],
                        y:[]
                    },
                    messages: [],
                    pie_chart: [44, 56],
                    rating: [],
                    total_amount: 491792,

                },

            }
        },
        methods: {
            getData() {
                axios.get(`${this.$hostname}/api/dashboard/`)
                    .then((response) => {
                        if(response.status === 200){
                            this.data = response.data;
                            console.log(response.data)
                        }

                    })
            }
        },
        mounted() {
            this.getData();
        },
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
    }
</script>

<style lang="scss">
    @import "../scss/main";


</style>