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
            component: () => import('./views/Agents/Agents.vue'),
            meta: {
                title: 'Агенты'
            },
            children: [
                {
                    path: '',
                    component: () => import('./views/Agents/AgentsDetailsView.vue')
                },

                {
                    path: '/agents/add',
                    component: () => import('./views/Agents/AgentsAddView.vue')
                },
            ]
        },
        {
            path: '/debtors',
            name: 'debtors',
            component: () => import('./views/Debtors.vue'),
            meta: {
                title: 'Дебиторы'
            }
        },
        {
            path: '/archive',
            name: 'archive',
            component: () => import('./views/Archive.vue'),
            meta: {
                title: 'Архив'
            }
        },
        {
            path: '/payments',
            name: 'payments',
            component: () => import('./views/Archive.vue'),
            meta: {
                title: 'Платежи'
            }
        },
        {
            path: '/payments',
            name: 'payments',
            component: () => import('./views/Payments.vue'),
            meta: {
                title: 'Платежи'
            }
        },
        {
            path: '/accruals',
            name: 'accruals',
            component: () => import('./views/Accruals.vue'),
            meta: {
                title: 'Начисления'
            }
        },
        {
            path: '/circulation',
            name: 'circulation',
            component: () => import('./views/Circulation.vue'),
            meta: {
                title: 'Обороты'
            }
        },
        {
            path: '/declarations',
            name: 'declarations',
            component: () => import('./views/Declarations.vue'),
            meta: {
                title: 'Декларации'
            }
        },
        {
            path: '/reports',
            name: 'reports',
            component: () => import('./views/Reports.vue'),
            meta: {
                title: 'Форма отчета'
            }
        },
    ]
})
