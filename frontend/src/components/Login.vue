<template>
  <div class="container">
    <h1>Sign In</h1>
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="onSubmit">
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" v-model="loginForm.username" class="form-control" v-bind:class="{'is-invalid': loginForm.usernameError}" id="username" placeholder="">
            <div v-show="loginForm.usernameError" class="invalid-feedback">{{ loginForm.usernameError }}</div>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" v-model="loginForm.password" class="form-control" v-bind:class="{'is-invalid': loginForm.passwordError}" id="password" placeholder="">
            <div v-show="loginForm.passwordError" class="invalid-feedback">{{ loginForm.passwordError }}</div>
          </div>
          <button type="submit" class="btn btn-primary">Sign In</button>
        </form>
      </div>
    </div>
    <br>
    <p>New User? <router-link to="/register">Click to Register!</router-link></p>
    <p>
        Forgot Your Password?
        <a href="#">Click to Reset It</a>
    </p>
  </div>
</template>

<script>
import store from '../store.js'

export default {
  name: 'Login',
  data () {
    return {
      sharedState: store.state,
      loginForm: {
        username: '',
        password: '',
        submitted: false,  // Whether submit button is pressed
        errors: 0,  // Whether form is verified successfully in frontend, 0 means a successful verification
        usernameError: null,
        passwordError: null
      }
    }
  },
  methods: {
    onSubmit (e) {
      this.loginForm.submitted = true
      this.loginForm.errors = 0
      if (!this.loginForm.username) {
        this.loginForm.errors++
        this.loginForm.usernameError = 'Username required.'
      } else {
        this.loginForm.usernameError = null
      }
      if (!this.loginForm.password) {
        this.loginForm.errors++
        this.loginForm.passwordError = 'Password required.'
      } else {
        this.loginForm.passwordError = null
      }
      if (this.loginForm.errors > 0) {
        // program will not be executed further if form verification is not successful, API calling will be passed to axios
        return false
      }
      const path = '/tokens'
      // auth property should be configured in config to realize Basic Auth
      this.$axios.post(path, {}, {
        auth: {
          'username': this.loginForm.username,
          'password': this.loginForm.password
        }
      }).then((response) => {
          // handle success
          window.localStorage.setItem('blog-token', response.data.token)
          store.loginAction()
          const name = JSON.parse(atob(response.data.token.split('.')[1])).name
          this.$toasted.success(`Welcome ${name}`, { icon: 'fingerprint' })
          if (typeof this.$route.query.redirect == 'undefined') {
            this.$router.push('/')
          } else {
            this.$router.push(this.$route.query.redirect)
          }
        })
        .catch((error) => {
          // handle error
          if (error.response.status == 401) {
            this.loginForm.usernameError = 'Invalid username or password.'
            this.loginForm.passwordError = 'Invalid username or password.'
          } else {
            console.log(error.response)
          }
        })
    }
  }
}
</script>