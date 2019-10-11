<template>
    <nav class="w-100 h-100">
        <div class="nav-header text-center" :class="{'nav-header--hidden':$store.getters.getIsMenuActive}">
            <h3 class="nav-header__name">crm obsr</h3>
            <div class="nav-header__toggle" @click="$store.dispatch('switchMenu')">
                <span></span><span></span><span></span>
            </div>
        </div>
        <div class="nav" :class="{'nav--hidden':$store.getters.getIsMenuActive}">
            <ul class="nav__body">
                <li class="nav__body__link">
                    <router-link to="/dashboard">
                        <span class="icon"> <font-awesome-icon :icon="['fas' ,'tachometer-alt']"/></span> <span
                            class="ml-2">Dashboard</span>
                    </router-link>
                </li>
                <li class="nav__body__link">
                    <router-link to="/clients">
                        <span class="icon"> <font-awesome-icon :icon="['fas' ,'users']"/></span> <span
                            class="ml-2">Клиенты</span>
                    </router-link>
                </li>
                <li class="nav__body__link">
                    <router-link to="/agents">
                        <span class="icon"> <font-awesome-icon :icon="['fas' ,'users']"/></span> <span
                            class="ml-2">Агенты</span>
                    </router-link>
                </li>
                <li class="nav__body__link">
                    <router-link to="/debtors">
                        <span class="icon"> <font-awesome-icon :icon="['fas' ,'file-invoice']"/></span> <span
                            class="ml-2">Дебиторы</span>
                    </router-link>
                </li>
                <li class="nav__body__link">
                    <router-link to="/archive">
                        <span class="icon"> <font-awesome-icon :icon="['fas' ,'archive']"/></span> <span
                            class="ml-2">Архив</span>
                    </router-link>
                </li>
                <li class="nav__body__link nav__body__link--off">
                    <a href="#" @click.prevent.stop="logout">
                        <span class="icon"> <font-awesome-icon :icon="['fas' ,'power-off']"/></span> <span
                            class="ml-2">Выход</span>
                    </a>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Navigation",
        methods: {
            logout() {
                axios.post(`${this.$hostname}/api/logout/`)
                    .then((response) => {
                        console.log(response.data)
                        if (response.status === 200) {
                            this.$session.destroy();
                            this.$router.push('/');
                            axios.defaults.headers.common['Authorization'] = '';
                        }
                    }).catch((error) => {
                    console.log(error)
                    this.$session.destroy();
                    this.$router.push('/');
                    axios.defaults.headers.common['Authorization'] = '';
                });
            }
        },

    }
</script>

<style lang="scss" scoped>
    @import "../scss/main";

    nav {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        .nav-header {
            background: $primary;
            padding: 25px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            min-height: 85px;
            &--hidden{
                .nav-header__name{
                    display: none;
                }
            }
            &__name {
                color: $white;
                font-size: convertFontToRem(23);
                text-transform: uppercase;
            }
            &__toggle {
                width: 20px;
                height: 20px;
                position: relative;
                display: flex;
                align-items: flex-start;
                justify-content: center;
                cursor: pointer;
                > span {
                    display: block;
                    width: 100%;
                    position: absolute;
                    height: 3px;
                    background: $white;
                    &:nth-child(2) {
                        top: 7px;
                    }
                    &:nth-child(3) {
                        top: 14px;
                    }
                }
            }
        }
        .nav {
            padding-top: 21px;
            background: $darkgray;
            color: $white;
            flex: 1;
            &--hidden{
                .nav__body{
                    &__link {
                        a{
                            span:last-child{
                                display: none;
                            }
                        }
                    }
                }
            }
            &__body {
                padding-left: 0;
                min-width: 100%;
                &__link {
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                    transition: background-color .1s linear;
                    a {
                        padding: 17px 45px;
                        min-width: 100%;
                        min-height: 55px;
                        font-size: convertFontToRem(14.65);
                        color: $white;
                        display: flex;
                        align-items: center;
                        justify-content: flex-start;
                        &:hover {
                            text-decoration: none;
                        }
                        i {
                            display: flex;
                            width: 35px;
                            height: 35px;
                            align-items: center;
                            justify-content: center;
                        }
                        .icon {
                            transition: color .1s linear;
                            display: flex;
                            align-items: center;
                            justify-content: flex-start;
                            width: 25px;
                        }
                    }
                    &--active, &:hover {
                        background: #3e4247;
                        a {
                            color: rgba($white, .9);
                            .icon {
                                color: $primary !important;
                            }
                        }
                    }
                    .router-link-active {
                        color: rgba($white, .9);
                        background: #3e4247;
                        .icon {
                            color: $primary !important;
                        }
                    }
                    &--off {
                        border-top: 1px solid rgba($white, .1);
                    }
                }
            }
        }
    }
</style>