import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        isMenuActive: false
    },
    mutations: {
        set(state, {type, items}) {
            state[type] = items;
        }
    },
    getters: {
        getIsMenuActive(state){
            return state.isMenuActive
        }
    },
    actions: {
        switchMenu({commit}) {
            commit('set', {type: 'isMenuActive', items: !this.getters.getIsMenuActive});
        }
    }
})
