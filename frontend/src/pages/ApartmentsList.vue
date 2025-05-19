<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="container mx-auto px-4">
      <h1 class="text-3xl font-bold mb-6 text-center text-gray-800">Apartment Rental</h1>

      <FilterPanel @applyFilters="onApplyFilters"/>

      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 mt-6">
        <router-link
          v-for="apartment in apartments"
          :key="apartment.id"
          :to="apartment.availability ? `/apartments/${apartment.slug}` : ''"
          class="block group transition duration-300"
          :class="!apartment.availability ? 'opacity-50 blur-lg' : ''"
        >
          <div
            :class="[
              'relative border rounded-2xl p-4 bg-white shadow-md hover:shadow-lg transition-all duration-300',
              !apartment.availability ? 'opacity-60 blur-[1px]' : ''
            ]"
          >
            <h2 class="text-xl font-semibold text-gray-800 mb-2">
              {{ apartment.name }}
            </h2>
            <p class="text-gray-600 mb-1">{{ apartment.description }}</p>
            <p class="text-gray-700">Price: <strong>{{ apartment.price }}$</strong></p>
            <p class="text-gray-700">Number of Rooms: {{ apartment.number_of_rooms }}</p>
            <p class="text-gray-700">Area: {{ apartment.square }} м²</p>
            <p>
              Available:
              <span :class="apartment.availability ? 'text-green-600' : 'text-red-600 font-medium'">
                {{ apartment.availability ? 'Yes' : 'No' }}
              </span>
            </p>

            <!-- Badge Unavailable -->
            <div
              v-if="!apartment.availability"
              class="absolute top-2 right-2 bg-red-500 text-white px-2 py-1 text-xs rounded shadow"
            >
              Unavailable
            </div>
          </div>
        </router-link>
      </div>

      <!-- Pagination -->
      <div class="mt-10 flex justify-center gap-4">
        <button
          @click="goToPage(currentPage - 1)"
          :disabled="currentPage === 1"
          class="px-4 py-2 rounded bg-blue-500 text-white disabled:bg-gray-300"
        >
          Previous
        </button>
        <button
          @click="goToPage(currentPage + 1)"
          :disabled="!nextPage"
          class="px-4 py-2 rounded bg-blue-500 text-white disabled:bg-gray-300"
        >
          Next
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import FilterPanel from '../components/FilterPanel.vue'
import axios from 'axios'

const apartments = ref([])
const filters = ref({})
const currentPage = ref(1)
const nextPage = ref(false)
const API_URL = import.meta.env.VITE_API_URL

async function fetchApartments() {
  const cleanedFilters = Object.fromEntries(
    Object.entries(filters.value).filter(([_, v]) => v !== null && v !== '')
  )
  const params = new URLSearchParams({ ...cleanedFilters, page: currentPage.value }).toString()
  const url = `${API_URL}/apartments/?${params}`

  try {
    const res = await axios.get(url)
    apartments.value = res.data.results
    nextPage.value = !!res.data.next
  } catch (err) {
    console.error('Error fetching apartments:', err)
    apartments.value = []
  }
}

function onApplyFilters(newFilters) {
  filters.value = newFilters
  currentPage.value = 1
  fetchApartments()
}

function goToPage(page) {
  if (page < 1) return
  currentPage.value = page
  fetchApartments()
}

onMounted(() => {
  fetchApartments()
})
</script>



