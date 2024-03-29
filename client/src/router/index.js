import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index';
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
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
  },
  {
    path: '/analysis',
    name: 'analysis',
    component: () => import(/* webpackChunkName: "about" */ '../views/Analysis.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
  },
  {
    path: '/gamedata',
    name: 'GameData',
    component: () => import(/* webpackChunkName: "about" */ '../views/GameData.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.common.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
  },
  {
    path: '/sign_up',
    name: 'signup',
    component: () => import('../views/SignUp.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue'),
  },
  //This was used for problem solving purposes on an issue that I had...
  // {
  //   path: '/gamecsv',
  //   name: 'GameCSV',
  //   component: () => import(/* webpackChunkName: "about" */ '../views/GameCSV.vue'),
  //   beforeEnter: (to, from, next) => {
  //     if (store.state.common.loginFlag === false) {
  //       next('/login');
  //     } else {
  //       next();
  //     }
  //   },
  //   beforeRouteLeave: (to, from, next) => {
  //     if (store.state.common.loginFlag === false) {
  //       next('/login');
  //     } else {
  //       next();
  //     }
  //   },
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
