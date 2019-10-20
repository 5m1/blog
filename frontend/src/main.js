// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import moment from 'moment'
import App from './App'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import VueToasted from 'vue-toasted'
import axios from './http'

Vue.config.productionTip = false

Vue.use(VueToasted, {
  theme: 'bubble',
  position: 'top-center',
  duration: 3000,
  iconPack: 'material',
  action: {
    text: 'Cancel',
    onClick: (e, toastObject) => {
      toastObject.goAway(0)
    }
  }
});

Vue.prototype.$axios = axios
Vue.prototype.$moment = moment

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


