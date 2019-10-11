<template>
    <div class="card">
        <div class="row header-wrapper pl-3">
            <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                <span class="table__icon"> <font-awesome-icon :icon="['fas' ,'file-invoice']"/></span>
                <h6 class="header ml-1">Дебиторы</h6>
                <div class="header__search ml-auto mr-5 d-flex align-items-center">
                    <h6 class="header">Поиск:</h6>
                    <div class="header__search-inner ml-3">
                        <input type="search" v-model="search">
                        <label>Логин, ФИО</label>
                        <font-awesome-icon class='header__search-icon' :icon="['fas' ,'search']"/>
                    </div>
                </div>
                <div class="choose-period__wrapper mx-2">
                    <span>Выбрать период:</span>
                    <select>
                        <option value="0">Январь</option>
                    </select>
                    -
                    <select>
                        <option value="0">Январь</option>
                    </select>
                </div>
                <button class="more-btn ml-2" @click="isTableExpanded = !isTableExpanded">Все</button>
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
                </b-table>
            </div>
        </div>
    </div>
</template>

<script>
    import ExpandTable from "../Tables/expandTable";
    import axios from 'axios';
    export default {
        name: "DebtorsTable",
        components: {ExpandTable},
        data(){
            return{
                isTableExpanded: false,
                data:[],
                search:'',
                fields: [
                    {
                        key: 'agent',
                        label: 'Агент',
                        class: 'table-header table-accent text-nowrap'
                    },
                    {
                        key: 'clients',
                        label: 'Количество клиентов',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'accruals',
                        label: 'Начисления',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'paid',
                        label: 'Оплачено',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'arrears',
                        label: 'Задолженность',
                        class: 'table-header text-nowrap'
                    },

                    {
                        key: 'mark',
                        label: 'Оценка агента',
                        class: 'table-header text-nowrap'
                    }
                ],

            }
        },
        computed: {
            visibleItems() {
                return this.isTableExpanded === false ? 5 : this.items.length
            },
            filteredList() {
                return this.data.filter(post => {
                    return JSON.stringify(post).toLowerCase().includes(this.search.toLowerCase())
                })
            }
        },
        methods: {
            getData() {
                axios.get(`${this.$hostname}/api/debtors/`)
                    .then((response) => {
                        this.data = response.data;
                        console.log(response.data)
                    })
            },
            getDetails(id){
                this.$store.dispatch('loadClientDetails',id);
            }
        },
        mounted() {
            this.getData();
        },
    }
</script>

<style lang="scss" scoped>

</style>