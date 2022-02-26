<template>
  <div>
    <ul>
      <div
        v-for="sent in sentences.sentences"
        v-bind:key="sent.id"
        v-on:click='index=sent.index'
      >
        <Sentence
          v-bind:sentence="sent"
          v-bind:in_focus="sent.index === index"
        />
      </div>
    </ul>
    <router-link v-if='prevFile > 1' v-bind:to="'/file/' + prevFile" class="footer">
      Предыдущий
    </router-link>
    <div class="footer" v-on:click='exportBtn()'>
      Экспорт
    </div>
    <router-link v-bind:to="'/file/' + nextFile" class="footer">
      Следующий
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'
import {mapActions, mapState} from 'vuex'
import Sentence from './Sentence.vue'

export default {
  name: 'Files',
  data () {
    return {
      index: 0
    }
  },
  computed: {
    ...mapState(['sentences']),
    nextFile () {
      return Number(this.$route.params.id) + 1
    },
    prevFile () {
      return Number(this.$route.params.id) - 1
    }
  },
  methods: {
    ...mapActions(['loadSentences']),
    keyFunc (e) {
      if (e.code === 'KeyS' && this.index < this.sentences.sentences.length - 1) {
        this.index++
      }
      if (e.code === 'KeyW' && this.index > 0) {
        this.index--
      }
      if (e.code === 'KeyO') {
        axios.get(
          'http://127.0.0.1:8000/export',
          {
            responseType: 'blob'
          }).then((response) => {
          var fileURL = window.URL.createObjectURL(new Blob([response.data]))
          var fileLink = document.createElement('a')
          fileLink.href = fileURL
          fileLink.setAttribute('download', 'export.txt')
          document.body.appendChild(fileLink)
          fileLink.click()
        })
      }
    },
    exportBtn () {
      axios.get(
        'http://127.0.0.1:8000/export',
        {
          responseType: 'blob'
        }).then((response) => {
        var fileURL = window.URL.createObjectURL(new Blob([response.data]))
        var fileLink = document.createElement('a')
        fileLink.href = fileURL
        fileLink.setAttribute('download', 'export.txt')
        document.body.appendChild(fileLink)
        fileLink.click()
      })
    }
  },
  mounted () {
    this.loadSentences(this.$route.params.id)
      .then(document.addEventListener('keydown', this.keyFunc))
  },
  beforeRouteUpdate (to, from, next) {
    this.loadSentences(to.params.id)
    next()
  },
  components: {
    Sentence
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.footer {
  width: 100%;
  padding-bottom: 200px;
  margin: 0 30px 0 30px;
  display: inline;
  cursor: pointer;
}
</style>
