import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {path: '/', redirect: {name: 'login'}},
        {
            path: '/login',
            name: 'login',
            component: () => import('./views/Login.vue'),
            meta: {
                title: 'Login',
            },
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('./views/Dashboard.vue'),
            meta: {
                title: 'Информационная панель'
            }
        },
        {
            path: '/clients',
            name: 'clients',
            component: () => import('./views/Clients.vue'),
            meta: {
                title: 'Клиенты'
            }
        },
        {
            path: '/agents',
            name: 'agents',
            component: () => import('./views/Agents.vue'),
            meta: {
                title: 'Информационная панель'
            }
        },
        {
            path: '/debtors',
            name: 'debtors',
            component: () => import('./views/Debtors.vue'),
            meta: {
                title: 'Информационная панель'
            }
        },
        {
            path: '/archive',
            name: 'archive',
            component: () => import('./views/Archive.vue'),
            meta: {
                title: 'Информационная панель'
            }
        },
    ]
})
