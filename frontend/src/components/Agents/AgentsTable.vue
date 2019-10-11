<template>
    <div>
        <div class="card">
            <div class="row header-wrapper pl-3">
                <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                    <span class="table__icon"> <font-awesome-icon  :icon="['fas' ,'users']"/></span>
                    <h6 class="header ml-1">Агенты</h6>
                    <div class="header__search ml-auto mr-5 d-flex align-items-center">
                        <h6 class="header">Поиск:</h6>
                        <div class="header__search-inner ml-3">
                            <input type="search" v-model="search">
                            <label>Логин, ФИО</label>
                            <font-awesome-icon class='header__search-icon' :icon="['fas' ,'search']"/>
                        </div>
                    </div>
                    <router-link class="main-btn ml-5" to="/agents/add">Добавить агента</router-link>
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
                        <template v-slot:cell(actions)="data">
                            <div class="text-nowrap" @click="showDetails(data.item.pk)">details</div>


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
        name: "AgentsTable",
        components: {ExpandTable},
        data(){
            return{
                isTableExpanded: false,
                data:[],
                search:'',
                fields: [
                    {
                        key: 'tags',
                        label: 'Тэг',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'user.email',
                        label: 'Логин',
                        class: 'table-header table-accent text-nowrap'
                    },
                    {
                        key: 'user.full_name',
                        label: 'ФИО',
                        class: 'table-header accent text-nowrap'
                    },
                    {
                        key: 'created_at',
                        label: 'Дата создания',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'last_change',
                        label: 'Дата изменения',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'actions',
                        label: 'Действия',
                        class: 'table-header text-nowrap'
                    }
                ],
                items: [
                    {tags: 40, login: 'Dickerson', full_name: 'Macdonald', created_at: '2019/08/16', changed_ad: '2019/08/16',actions:''},
                ],
            }
        },
        computed: {
            visibleItems() {
                return !this.isTableExpanded ? 5 : this.filteredList.length
            },
            filteredList() {
                return this.data.filter(post => {
                    return JSON.stringify(post).toLowerCase().includes(this.search.toLowerCase())
                })
            }
        },
        methods: {
            getData() {
                axios.get(`${this.$hostname}/api/agents/`)
                    .then((response) => {
                        this.data = response.data;
                        console.log(response.data)
                    })
            },
            showDetails(id){
                this.$store.dispatch('loadAgentDetails',id)
                this.$router.push({path:'/agents'});

            }
        },
        mounted() {
            this.getData();
        },
    }
</script>

<style lang="scss" scoped>

</style>