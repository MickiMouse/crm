import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueApexCharts from 'vue-apexcharts'
Vue.config.productionTip = false
import VueSession from 'vue-session'

Vue.use(VueSession)
Vue.use(BootstrapVue)
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)
library.add(fas,fab,far);
import 'v2-datepicker/lib/index.css';   // v2 need to improt css
import V2Datepicker from 'v2-datepicker';

Vue.use(V2Datepicker)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.prototype.$hostname = 'http://192.168.31.237:8000';

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
