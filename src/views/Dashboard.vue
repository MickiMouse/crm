<template>
    <div class="content">
        <div class="row">
            <div class="col-5">
                <paid-contracts class="h-100"/>
            </div>
            <div class="col-7">
                <dynamics-clients class="h-100"/>
            </div>
        </div>
        <div class="row py-4">
            <div class="col-4">
                <info-card :icon="['fas' ,'dollar-sign']" :value="3000001" :header="'Общая сумма'"/>
            </div>
            <div class="col-4">
                <info-card :icon="['fas' ,'users']" :value="22" :header="'Клиентов'"/>
            </div>
            <div class="col-4">
                <info-card :icon="['fas' ,'users']" :value="50" :header="'Агентов'"/>
            </div>
        </div>
        <div class="row">
            <div class="col-7">
                <expand-table :items="client_items" :fields="client_fields"
                              :header="'Агенты с низкой оценкой'"
                              :icon="['fas' ,'users']"
                              class="mb-3"/>
                <expand-table :items="agent_items" :fields="agent_fields"
                              :header="'Клиенты с истикающими договорами'"
                              :icon="['fas' ,'users']"
                              class="mb-3"/>
            </div>
            <div class="col-5">
                <notifications
                        :items="client_items"
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

    export default {
        name: "Dashboard",
        components: {Notifications, ExpandTable, InfoCard, DynamicsClients, PaidContracts},
        data() {
            return {
                client_fields: [
                    {
                        key: 'last_name',
                        label: '№',
                        class: 'table-header'
                    },
                    {
                        key: 'first_name',
                        label: 'ФИО агента',
                        class: 'table-header table-accent'
                    },
                    {
                        key: 'age',
                        label: 'Оценка',
                        class: 'table-header'
                    }
                ],
                client_items: [
                    {age: 40, first_name: 'Dickerson', last_name: 'Macdonald',},
                    {age: 21, first_name: 'Larsen', last_name: 'Shaw'},
                    {age: 89, first_name: 'Geneva', last_name: 'Wilson'},
                    {age: 38, first_name: 'Jami', last_name: 'Carney' },
                    {age: 89, first_name: 'Geneva', last_name: 'Wilson'},
                    {age: 38, first_name: 'Jami', last_name: 'Carney'}
                ],
                agent_fields: [
                    {
                        key: 'last_name',
                        label: '№',
                        class: 'table-header'
                    },
                    {
                        key: 'first_name',
                        label: 'Компания',
                        class: 'table-header table-accent'
                    },
                    {
                        key: 'age',
                        label: 'Агент',
                        class: 'table-header table-accent'
                    },
                    {
                        key: 'date',
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
                ]
            }
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
    .table-header{
        font-size: convertFontToRem(12);
        font-weight: 100;
    }
    .table-accent{
        color: $accent;
    }
    th[role='columnheader']{
        color: $black;
        font-weight: bolder;
    }
</style>