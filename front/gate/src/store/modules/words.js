import axios from 'axios'

const state = {
  words: [],
  sentence: []
}

const actions = {
  loadWords: ({ commit }, id) => {
    commit('setWords', [])
    axios
      .get(`http://127.0.0.1:8000/sentence?id=${id}`)
      .then(res => commit('setWords', res.data.data))
  }
}

const mutations = {
  setWords: (state, data) => {
    state.words = data
  }
}

export default {
  state,
  actions,
  mutations
}
