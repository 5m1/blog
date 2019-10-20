<template>
  <div class="container">
    <alert
      v-for="(alert, index) in activeAlerts" :key="index"
      v-bind:variant="alert.alertVariant"
      v-bind:message="alert.alertMessage">
    </alert>
    <button type="button" class="btn btn-primary">Homepage</button>
  </div>
</template>

<script>
import Alert from './Alert'

export default {
  name: 'Home',
  components: {
    alert: Alert
  },
  computed: {
    activeAlerts: function() {
      return this.alerts.filter(function(alert) {
        return alert.showAlert
      })
    }
  },
  data () {
    return {
      alerts: [
        {
          showAlert: false,
          alertVariant: 'danger',
          alertMessage: 0
        },
        {
          showAlert: true,
          alertVariant: 'info',
          alertMessage: 1
        },
        {
          showAlert: false,
          alertVariant: 'dark',
          alertMessage: 2
        }
      ]
    }
  }
}
</script>