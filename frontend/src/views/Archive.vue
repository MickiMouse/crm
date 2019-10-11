<template>
    <div class="card">
        <div class="row header-wrapper pl-3">
            <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                <span class="table__icon"> <font-awesome-icon  :icon="['fas' ,'users']"/></span>
                <h6 class="header ml-1">Клиенты</h6>
                <div class="header__search ml-auto mr-5 d-flex align-items-center">
                    <h6 class="header">Поиск:</h6>
                    <div class="header__search-inner ml-3">
                        <input type="search" v-model="search">
                        <label>Логин, ФИО</label>
                        <font-awesome-icon class='header__search-icon' :icon="['fas' ,'search']"/>
                    </div>
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
                    <template v-slot:cell(kind_of_activity)="data">
                        <div class="text-nowrap" v-for="item in data.kind_of_activity">{{item.activity}}</div>
                    </template>
                    <template v-slot:cell(actions)="data">
                        <div class="text-nowrap" @click="getDetails(data.item.pk)">details</div>
                    </template>
                </b-table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Archive",
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
        data(){
            return{
                isTableExpanded: false,
                data:[],
                search:'',
                fields: [
                    {
                        key: 'short_name',
                        label: 'Наиминование компании',
                        class: 'table-header table-accent text-nowrap'
                    },
                    {
                        key: 'kind_of_activity',
                        label: 'Вид деятельности',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'extra_address',
                        label: 'Доп. адрес',
                        class: 'table-header accent text-nowrap'
                    },
                    {
                        key: 'bin_iin',
                        label: 'БИН/ИНН',
                        class: 'table-header text-nowrap'
                    },
                    {
                        key: 'agent.user.full_name',
                        label: 'Агент',
                        class: 'table-header table-accent text-nowrap'
                    },
                    {
                        key: 'expiration_date',
                        label: 'Дата окончания',
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
                axios.get(`${this.$hostname}/api/clients/`)
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

<style scoped>

</style>