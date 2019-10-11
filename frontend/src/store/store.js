import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axios from 'axios';

export default new Vuex.Store({
    state: {
        isMenuActive: false,
        agentDetails: null,
        clientDetails: null,
        clientTablesDetails:{
            first:{},
            second:{}
        }
    },
    mutations: {
        set(state, {type, items}) {
            state[type] = items;
        }
    },
    getters: {
        getIsMenuActive(state) {
            return state.isMenuActive
        },
        getAgentDetails(state) {
            return state.agentDetails
        },
        getClientDetails(state) {
            return state.clientDetails
        },
        getClientTablesDetails(state){
            return state.clientTablesDetails
        }
    },
    actions: {
        switchMenu({commit}) {
            commit('set', {type: 'isMenuActive', items: !this.getters.getIsMenuActive});
        },
        loadAgentDetails({commit}, id) {
            axios.get(`${Vue.prototype.$hostname}/api/agent/${id}/`)
                .then((response) => {

                    console.log(response.data)
                    commit('set', {type: 'agentDetails', items: response.data});
                })
        },
        loadClientDetails({commit}, id) {
            axios.get(`${Vue.prototype.$hostname}/api/client/${id}/`)
                .then((response) => {

                    console.log(response.data)
                    commit('set', {type: 'clientDetails', items: response.data});
                });
            axios.get(`${Vue.prototype.$hostname}/api/tables/${id}/`)
                .then((response) => {

                    console.log(response.data)
                    commit('set', {type: 'clientTablesDetails', items: response.data});
                })
        }
    }
})
