<template>
  <div v-if="sentence !== null">
    <Sentence
      v-bind:sentence="sentence"
      v-bind:in_focus="false"
    />
    <ul>
      <li v-for="word in words.words" v-bind:key="word.id">
          {{ word.word }}
      </li>
    </ul>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import Sentence from './Sentence.vue'

export default {
  components: { Sentence },
  name: 'Words',
  data () {
    return {
      sentence: null
    }
  },
  computed: {
    ...mapState(['words', 'sentences'])
  },
  methods: {
    ...mapActions(['loadWords', 'loadSentences'])
  },
  mounted () {
    let id = this.$route.params.id
    this.loadWords(id)
      .then(this.sentence = this.sentences.sentences[id - 1])
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
