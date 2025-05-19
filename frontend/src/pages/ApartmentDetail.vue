<template>
  <div v-if="apartment">
    <h1 class="text-2xl font-bold">{{ apartment.name }}</h1>
    <p>{{ apartment.description }}</p>
    <p>Ціна: {{ apartment.price }} $</p>
    <p>Кімнат: {{ apartment.number_of_rooms }}</p>
    <p>Площа: {{ apartment.square }} м²</p>
    <p>Статус: {{ apartment.availability ? 'Доступна' : 'Недоступна' }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/api/axios'

const route = useRoute()
const apartment = ref(null)

onMounted(async () => {
  const res = await api.get(`/apartments/${route.params.slug}/`)
  apartment.value = res.data
})
</script>
