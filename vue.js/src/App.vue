<template>

  <div id="app"><router-view/></div>

</template>


<script>

  /*JWT integration*/
  const SECRET_KEY = 'ThisIsSecretKey'
  var jwt = require('jsonwebtoken');
  var token = jwt.sign({ username: 'julfikar', password: '123456789' }, SECRET_KEY);
  console.log(token)

  /*Vue.js settings*/
  export default {
    name: 'App',

    data () {
      return {

      }
    },//data

    created() {
      fetch("http://127.0.0.1:8000/api-drf/jwt-communication/",
              {
                method: 'GET',
                headers: {
                  // 'Access-Control-Allow-Origin': true,
                  'Content-Type': 'application/json',
                  'Authorization': token
                },

              }).then((response) => {return response}).then((data) => {console.log(data)})
    }//created

  }
</script>


<style>

</style>
