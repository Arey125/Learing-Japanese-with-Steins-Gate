<template>
    <ul>
        <li v-for="file in files.files" v-bind:key="file.id">
            <router-link v-bind:to="'/file/' + file.id">{{ file.filename }}</router-link>
            <div v-if="file.checked" class="mark">
              ✔
            </div>
        </li>
    </ul>
</template>

<script>
import {mapActions, mapState} from 'vuex'

export default {
  name: 'Files',
  computed: {
    ...mapState(['files'])
  },
  methods: {
    ...mapActions(['loadFiles'])
  },
  mounted () {
    this.loadFiles()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mark {
  font-size: 14px;
  padding-left: 10px;
  color: #777;
}
</style>
