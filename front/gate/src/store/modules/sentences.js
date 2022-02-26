import axios from 'axios'

const state = {
  sentences: []
}

const actions = {
  loadSentences: ({ commit }, id) => {
    commit('setSentences', [])
    axios
      .get(`http://127.0.0.1:8000/file?id=${id}`)
      .then(res => commit('setSentences', res.data.data))
  },
  markSentence: ({ commit }, id) => {
    axios
      .get(`http://127.0.0.1:8000/mark?id=${id}`)
      .then(res => commit('setSentences', res.data.data))
  }
}

const mutations = {
  setSentences: (state, data) => {
    state.sentences = data
  }
}

export default {
  state,
  actions,
  mutations
}
