<template>
    <div id="app">
        <div class="container-fluid">
            <div class="row">
                <div class="px-0 fixed-top" v-show="show"
                     :class="{'col-sm-3':!$store.getters.getIsMenuActive,'col-sm-1':$store.getters.getIsMenuActive}">
                    <navigation/>
                </div>
                <div class="main-container" :class="{'col-sm-9 offset-sm-3':show && !$store.getters.getIsMenuActive,'col-sm-11 offset-sm-1':show && $store.getters.getIsMenuActive,'col-sm-12':!show}">
                    <main-header v-show="show"/>
                    <div class="row main-row">
                        <div class="col-12">
                            <router-view/>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<style lang="scss">
    @import "../src/scss/main";




</style>
<script>
    import Navigation from "./components/Navigation";
    import MainHeader from "./components/MainHeader";
    import axios from 'axios';

    export default {
        components: {MainHeader, Navigation},
        computed: {
            show: function () {
                return this.$route.name !== 'login';
            }
        },
        beforeCreate(){
            axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('jwt');
        }
    }
</script>