<template>
    <div class="div">
        <form class="card container-fluid" @submit.prevent="create">
            <div class="row card__header header-wrapper">
                <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                    <!--<input type="text" class="header">-->
                    <h6 class="header pr-1">Добавить агента</h6>
                    <!--<div class="header-border"></div>-->
                    <!--<span class="card__header__email ml-1">-->
                   <!--{{$store.getters.getAgentDetails.agent.user.email}}-->
                <!--</span>-->
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <label for="full_name" class="header">ФИО:</label>
                </div>
                <div class="col-8 py-3 card__header justify-content-start">
                    <input type="text" class="header" id="full_name" v-model="data.full_name">
                    <!--<h6 class="header">{{$store.getters.getAgentDetails.agent.user.full_name}}</h6>-->
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <label for="email" class="header">E-mail:</label>
                </div>
                <div class="col-8 py-3 card__header justify-content-start">
                    <!--<h6 class="header">{{$store.getters.getAgentDetails.agent.user.email}}</h6>-->
                    <input type="email" class="header" id="email" v-model="data.email">
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <label for="phone" class="header">Номер телефона:</label>
                </div>
                <div class="col-8 py-3 card__header justify-content-start">
                    <!--<h6 class="header">{{$store.getters.getAgentDetails.agent.phone}}</h6>-->
                    <input type="tel" class="header" id="phone" v-model="data.phone">
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <label for="password" class="header">Пароль:</label>
                </div>
                <div class="col-8 py-3 card__header justify-content-start">
                    <!--<h6 class="header">{{$store.getters.getAgentDetails.agent.clients.length}}</h6>-->
                    <input type="password" class="header" id="password" v-model="data.password">
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <label for="password2" class="header">Повторите пароль:</label>
                </div>
                <div class="col-8 py-3 card__header justify-content-start">
                    <!--<h6 class="header">{{$store.getters.getAgentDetails.agent.clients.length}}</h6>-->
                    <input type="password" class="header" id="password2" v-model="data.password2">
                </div>
            </div>
            <div class="row">

                <div class="col-8 offset-4 py-3 card__header justify-content-start">
                  <button type="submit" class="main-btn ml-auto">Создать</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "AgentsAdd",
        data(){
            return{
                data:{
                    full_name:'',
                    email:'',
                    phone:'',
                    password:'',
                    password2:''
                }
            }
        },
        methods:{
            create(){
                axios.post(`${this.$hostname}/api/create/agent/`,{
                    user:{email:this.data.email,password:this.data.password,full_name:this.data.full_name},
                    phone:this.data.phone,
                    password2:this.data.password2
                }
                )
                    .then((response) => {
                        this.data = '';
                        console.log(response.data);
                        this.$store.commit('set', {type: 'agentDetails', items: {}});
                        this.$router.push({path:'/agents'});
                    })
            }
        }
    }
</script>

<style scoped>

</style>