<script setup>
import { ref } from 'vue'

const emit = defineEmits(['applyFilters'])

const price_min = ref(null)
const price_max = ref(null)
const rooms = ref(null)
const available = ref(false)
const search = ref('')

function apply() {
  emit('applyFilters', {
    price_min: price_min.value,
    price_max: price_max.value,
    rooms: rooms.value,
    available: available.value,
    search: search.value,
  })
}
</script>

<template>
  <div>
    <input v-model="price_min" placeholder="Minimum Price" type="number" />
    <input v-model="price_max" placeholder="Maximum Price" type="number" />
    <input v-model="rooms" placeholder="Number of Rooms" type="number" />
    <label>
      <input type="checkbox" v-model="available" />
      Available
    </label>
    <input v-model="search" placeholder="Search" />
    <button @click="apply">Apply</button>
  </div>
</template>
