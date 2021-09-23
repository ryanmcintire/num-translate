<template>
  <div id="app" class="bg-dark">
    <NumberForm />
  </div>
</template>

<script>
import NumberForm from "./components/NumberForm"

export default {
  name: 'App',
  components: {
    NumberForm: NumberForm
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
