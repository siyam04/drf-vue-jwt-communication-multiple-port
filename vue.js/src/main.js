/*System Importing*/
import Vue from 'vue'
import App from './App.vue'

/*Custom Router File Importing*/
// Router (const variable array)
import {router} from "./router/router"

/*Production Setting*/
Vue.config.productionTip = false;

/*Vue Framework*/
new Vue({
  render: h => h(App),
  // export const variable array
  router: router
}).$mount('#app');
