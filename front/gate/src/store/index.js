import Vue from 'vue'
import Vuex from 'vuex'
import files from './modules/files'
import sentences from './modules/sentences'
import words from './modules/words'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    files,
    sentences,
    words
  }
})
