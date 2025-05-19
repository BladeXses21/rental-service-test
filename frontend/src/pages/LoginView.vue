<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <form @submit.prevent="login" class="bg-white p-6 rounded shadow-md w-full max-w-sm">
      <h2 class="text-2xl font-bold mb-4 text-center">Вхід</h2>

      <input v-model="email" type="text" placeholder="Логін"
             class="w-full border p-2 rounded mb-3" required />
      <input v-model="password" type="password" placeholder="Пароль"
             class="w-full border p-2 rounded mb-4" required />

      <button type="submit" class="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700">
        Увійти
      </button>

      <p v-if="error" class="text-red-500 text-sm mt-2">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()
const API_URL = import.meta.env.VITE_API_URL

const login = async () => {
  try {
    const res = await axios.post(`${API_URL}/users/api/token/`, {
      email: email.value,
      password: password.value
    })
    localStorage.setItem('access_token', res.data.access)
    axios.defaults.headers.common['Authorization'] = `Bearer ${res.data.access}`
    const nextUrl = router.currentRoute.value.query.next || '/'
    await router.push(nextUrl)
  } catch (err) {
    error.value = 'Invalid login or password'
  }
}
</script>
