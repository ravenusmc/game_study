import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/analysis',
    name: 'analysis',
    component: () => import(/* webpackChunkName: "about" */ '../views/Analysis.vue')
  },
  {
    path: '/gamedata',
    name: 'GameData',
    component: () => import(/* webpackChunkName: "about" */ '../views/GameData.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
