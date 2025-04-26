<template>
    <div class="p-4 max-w-3xl mx-auto">
      <img :src="movie.Poster" class="w-full mb-4 rounded shadow" />
      <h1 class="text-2xl font-bold">{{ movie.Title }}</h1>
      <p class="mt-2"><strong>Año:</strong> {{ movie.Year }}</p>
      <p><strong>Actores:</strong> {{ movie.Actors }}</p>
      <p><strong>Género:</strong> {{ movie.Genre }}</p>
      <p><strong>Sinopsis:</strong> {{ movie.Plot }}</p>
    </div>
</template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  const movie = ref({})
  
  const fetchMovie = async () => {
    const res = await axios.get(`https://www.omdbapi.com/?apikey=TU_API_KEY&i=${route.params.id}&plot=full`)
    movie.value = res.data
  }
  
  onMounted(fetchMovie)
  </script>
  