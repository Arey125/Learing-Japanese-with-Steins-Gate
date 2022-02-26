<template>
  <li v-bind:class='{active: in_focus}' class='list-elem'>
    <div class='wrap'>
      <div>
        <router-link v-bind:to="'/sentence/' + sentence.id">
            {{ sentence.sentence }}
        </router-link>
      </div>
      <div class="options">
        <div
          v-on:click="play(sentence.audio)"
          class="btn"
          v-bind:tabindex="sentence.id">
          Аудио
        </div>
        <div v-on:click="closed=!closed" class="btn">
          Перевод
        </div>
        <div v-if="sentence.checked" class="btn">
          ✔
        </div>
      </div>
    </div>
    <div class="translation wrap" v-if="!closed">
      <div>
        {{sentence.translation}}
      </div>
      <div class="options">
        <div v-on:dblclick="merge()" class="btn">
          Объединить со следующим
        </div>
        <div v-on:dblclick="split()" class="btn">
          Разделить
        </div>
      </div>
    </div>
  </li>

</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'

export default {
  data () {
    return {
      closed: true,
      mute: false,
      position: 0
    }
  },
  props: ['sentence', 'in_focus'],
  methods: {
    ...mapActions(['loadSentences', 'markSentence']),
    play (name) {
      let audio = new Audio(`http://127.0.0.1:8000/${name}`)
      audio.play()
    },
    keyFunc (event) {
      if (!this.in_focus || this.mute) {
        return
      }
      let audio = this.sentence.audio
      if (event.code === 'KeyQ') {
        this.play(audio)
      }
      if (event.code === 'KeyE') {
        this.closed = !this.closed
      }
      if (event.code === 'KeyF') {
        this.markSentence(this.sentence.id)
      }
      if (event.code === 'Enter') {
        this.$router.push('/sentence/' + this.sentence.id)
      }
    },
    merge () {
      let id = this.sentence.id
      let fileID = this.sentence.file_id
      axios.get(`http://127.0.0.1:8000/merge?id=${id}`)
        .then(res => { this.loadSentences(fileID) })
    },
    split () {
      let id = this.sentence.id
      let fileID = this.sentence.file_id
      axios.get(`http://127.0.0.1:8000/split?id=${id}`)
        .then(res => { this.loadSentences(fileID) })
    }
  },
  mounted () {
    window.addEventListener('keydown', this.keyFunc)
  },
  beforeDestroy () {
    this.mute = true
  }
}
</script>

<style scoped>
.list-elem {
  display: block;
  text-align: left;
  padding-left: 10px;
  padding-right: 10px;
}

.active {
  background-color:#fafafa;
}

.options {
  display: inline-flex;
}

.translation {
  padding-top: 5px;
  margin-top: 5px;
  border-top: 1px solid #ebebeb
}

:focus {
  outline: none;
}
.wrap {
  padding-left: 30px;
  padding-right: 30px;
}
</style>
