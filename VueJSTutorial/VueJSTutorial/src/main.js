import Vue from 'vue'
import App from './App.vue'
import Nations from './Nations.vue'

Vue.component('nations', Nations)

new Vue({
  el: '#app',
  render: h => h(App)

})
