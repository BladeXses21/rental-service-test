import { createRouter, createWebHistory } from 'vue-router'
import ApartmentsList from '@/pages/ApartmentsList.vue'
import ApartmentDetail from '@/pages/ApartmentDetail.vue'
import LoginView from "@/pages/LoginView.vue";

const routes = [
  { path: '/', name: 'home', component: ApartmentsList, meta: { requiresAuth: true } },
  { path: '/apartments', name: 'apartments', component: ApartmentsList, meta: { requiresAuth: true } },
  { path: '/apartments/:slug', name: 'apartments-slug', component: ApartmentDetail, meta: { requiresAuth: true } },
  { path: '/login', name: 'login', component: LoginView }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token')
  const isAuthenticated = !!token

  if (to.meta.requiresAuth && !isAuthenticated) {
    next({name: 'login', query: { next: to.fullPath }}) // redirect + path mem
  } else if (to.name === 'login' && isAuthenticated ) {
    next({ name: 'home' })
  } else {
    next()
  }
})

export default router
