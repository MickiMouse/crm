<template>
    <div>
        <div class="card">
            <div class="row header-wrapper pl-3">
                <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                    <span class="table__icon"> <font-awesome-icon :icon="['fas' ,'file-invoice']"/></span>
                    <h6 class="header ml-1">Таблица отчетности работников</h6>
                    <!--<div class="header__search ml-auto mr-5 d-flex align-items-center">-->
                    <!--<h6 class="header">Поиск:</h6>-->
                    <!--<div class="header__search-inner ml-3">-->
                    <!--<input type="search">-->
                    <!--<label>Логин, ФИО</label>-->
                    <!--<font-awesome-icon class='header__search-icon' :icon="['fas' ,'search']"/>-->
                    <!--</div>-->
                    <!--</div>-->
                    <div class="choose-period__wrapper ml-auto">
                        <span>Выбрать период:</span>
                        <select v-model="date_from">
                            <option value="1">Январь</option>
                            <option value="2">Февраль</option>
                            <option value="3">Март</option>
                            <option value="4">Апрель</option>
                            <option value="5">Май</option>
                            <option value="6">Июнь</option>
                            <option value="7">Июль</option>
                            <option value="8">Август</option>
                            <option value="9">Сентябрь</option>
                            <option value="10">Октябрь</option>
                            <option value="11">Ноябрь</option>
                            <option value="12">Декабрь</option>
                        </select>
                        -
                        <select v-model="date_to">
                            <option value="1">Январь</option>
                            <option value="2">Февраль</option>
                            <option value="3">Март</option>
                            <option value="4">Апрель</option>
                            <option value="5">Май</option>
                            <option value="6">Июнь</option>
                            <option value="7">Июль</option>
                            <option value="8">Август</option>
                            <option value="9">Сентябрь</option>
                            <option value="10">Октябрь</option>
                            <option value="11">Ноябрь</option>
                            <option value="12">Декабрь</option>
                        </select>
                    </div>
                    <button class="main-btn ml-3" @click="">Добавить работника</button>
                    <button class="main-btn mx-3" @click="">Редактировать</button>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <b-table striped hover
                             :items="filteredList"
                             :fields="fields"
                             :striped="false"
                             :per-page="visibleItems"
                             class="mb-0"
                             responsive
                             :sticky-header="true"
                    >
                        <template v-slot:cell(actions)="data">
                            <div class="text-nowrap" @click="getDetails(data.item.pk)">details</div>
                        </template>
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ExpandTable from "../Tables/expandTable";
    import axios from 'axios';

    export default {
        name: "ClientsTableWorkers",
        components: {ExpandTable},
        data() {
            return {
                isTableExpanded: false,
                data: {},
                fields: [
                    {
                        key: 'month',
                        label: 'Месяц',
                        class: 'table-header table-accent text-nowrap'
                    },
                    {
                        key: 'worker.last_name',
                        label: 'Работник',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'earn',
                        label: 'ЗП "На руки"',
                        class: 'table-header accent text-nowrap'
                    },
                    {
                        key: 'profit',
                        label: 'ЗП "начисления"',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'adjustment',
                        label: 'Корректировка',
                        class: 'table-header table-accent text-nowrap'
                    },
                    {
                        key: 'pension_contrib',
                        label: 'ОПВ',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'individual_income_tax',
                        label: 'ИПН',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'social_contrib',
                        label: 'СО',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'med_contrib',
                        label: 'ОСМС',
                        class: 'table-header text-nowrap'
                    },
                ],
                items: [
                    {
                        tags: 40,
                        login: 'Dickerson',
                        full_name: 'Macdonald',
                        created_at: '2019/08/16',
                        changed_ad: '2019/08/16',
                        actions: ''
                    },
                ],
                date_from: 1,
                date_to: 12
            }
        },
        computed: {
            visibleItems() {
                return this.isTableExpanded === false ? 5 : this.items.length
            },
            filteredList() {
                return this.$store.getters.getClientTablesDetails.second.filter(post => {
                    return parseInt(post.month.split('.')[1]) >= this.date_from && parseInt(post.month.split('.')[1]) <= this.date_to
                })
            }
        },
        methods: {
            // getData() {
            //     axios.get(`${this.$hostname}/api/clients/`)
            //         .then((response) => {
            //             this.data = response.data;
            //             console.log(response.data)
            //         })
            // },
            // getDetails(id){
            //     this.$store.dispatch('loadClientDetails',id)
            // }
        },
        mounted() {
            console.log(this.$store.getters.getClientTablesDetails.second)
            this.$store.getters.getClientTablesDetails.second.filter(post => {
                console.log(post.month.split('.')[1])
                // return post
                // return JSON.stringify(post.month.split('.')[1]) >= this.date_from && JSON.stringify(post.month.split('.')[1]) <= this.date_to
            })
            // this.getData();
        },
    }
</script>

<style lang="scss" scoped>
    @import "../../scss/main";

</style>
