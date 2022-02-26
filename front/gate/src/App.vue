<template>
  <div id="app">
    <div id="wrapper">
      <header>
        <router-link to="/">Steins gate</router-link>
      </header>
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  margin: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  font-size: 18px;
  color: #2c3e50;
  margin: 0;
}
#wrapper {
  max-width: 960px;
  min-width: 300px;
  margin: auto;
}
header {
  padding: 10px 40px;
  margin: 0;
  border-bottom: 1px solid #b0b0b0;
}
.btn {
  cursor: pointer;
  color: #aaa;
  font-size: 13px;
  width: fit-content;
  margin: 1px 40px 1px 0;
}
.btn:hover {
  color: #888;
}
ul {
    list-style-type: none;
    margin-top: 0;
    padding: 0;
}
li {
  display: flex;
  padding: 5px 2px;
  padding-left: 40px;
  border-bottom: 1px solid #ddd
}
a {
  text-decoration: none;
  color:#2c3e50;
}
header a {
  text-decoration: none;
  display: flex;
  color:#2c3e50;
  font-size: 30px;
}
</style>
