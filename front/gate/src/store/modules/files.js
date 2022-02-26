import axios from 'axios'

const state = {
  files: []
}

const getters = {
  getFiles: (state, getters) => {
    return state.files
  }
}

const actions = {
  loadFiles: ({ commit }) => {
    axios
      .get('http://127.0.0.1:8000')
      .then(res => commit('setFiles', res.data.data))
  }
}

const mutations = {
  setFiles: (state, data) => {
    state.files = data
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
