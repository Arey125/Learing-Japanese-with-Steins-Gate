import Vue from 'vue'
import Router from 'vue-router'
import Files from '@/components/Files'
import Sentences from '@/components/Sentences'
import Words from '@/components/Words'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/file/:id',
      name: 'Sentences',
      component: Sentences
    },
    {
      path: '/sentence/:id',
      name: 'Words',
      component: Words
    },
    {
      path: '/',
      name: 'Files',
      component: Files
    }
  ]
})
