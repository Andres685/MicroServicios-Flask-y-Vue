<template>
  <div class="container">
    <!-- Header / Navbar -->
    <header>
      <nav class="navbar">
        <div class="nav-section nav-left">
          <button class="nav-button menu-button">
            <i class="uil uil-bars"></i>
          </button>
          <a href="#" class="nav-logo">
            <img src="../assets/logoSoft.png" alt="Logo" class="logo-image" />
            <h2 class="logo-text">PELISCRIPT</h2>
            <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
          </a>
        </div>
        <div class="nav-section nav-right">
          <button class="nav-button theme-button">
            <i class="uil uil-moon"></i>
          </button>
          <img src="../assets/logo.png" alt="User Image" class="user-image" />
        </div>
      </nav>
    </header>
    
    <!-- Main Layout -->
    <main class="main-layout">
      <div class="screen-overlay"></div>
      
      <!-- Sidebar -->
      <aside class="sidebar">
        <div class="nav-section nav-left">
          <button class="nav-button menu-button">
            <i class="uil uil-bars"></i>
          </button>
          <a href="#" class="nav-logo">
            <img src="../assets/logoSoft.png" alt="Logo" class="logo-image" />
            <h2 class="logo-text">PELISCRIPT</h2>
          </a>
        </div>
        <div class="links-container">
          <div class="link-section">
            <router-link to="/catalogo" class="link-item"> 
              <i class="uil uil-estate"></i> Inicio 
            </router-link>
            <router-link to="/por-ver" class="link-item active"> 
              <i class="uil uil-tv-retro"></i> Por Ver 
            </router-link>
          </div>
          <div class="section-separator"></div>
          <div class="link-section">
            <h4 class="section-title">Cuenta</h4>
            <router-link to="/perfil" class="link-item"> 
              <i class="uil uil-user-square"></i> Tu Perfil 
            </router-link>
            <router-link to="/login" class="link-item">
              <i class="uil uil-sign-out-alt"></i> Cerrar Sesión
            </router-link>
          </div>
          <div class="section-separator"></div>
          <div class="link-section">
            <h4 class="section-title">Explorar</h4>
            <router-link to="/tendencias" class="link-item"> 
              <i class="uil uil-fire"></i> Tendencias 
            </router-link>
            <router-link to="/series" class="link-item"> 
              <i class="uil uil-film"></i> Series 
            </router-link>
            <router-link to="/cartelera" class="link-item"> 
              <i class="uil uil-ticket"></i> Cartelera 
            </router-link>
          </div>
          <div class="section-separator"></div>
        </div>
      </aside>
      
      <div class="content-wrapper">
        <h1 class="text-2xl font-bold mb-6 px-4">Mi lista de películas por ver</h1>

        <div v-if="loading" class="loading">
          <div class="spinner"></div>
          <p>Cargando tu lista...</p>
        </div>

        <div v-else-if="movies.length === 0" class="text-center py-10" style="grid-column: 1 / -1;">
          <i class="uil uil-bookmark text-4xl mb-2"></i>
          <h3 class="text-xl font-semibold">No tienes películas en tu lista</h3>
          <p class="text-gray-600">Añade películas desde el catálogo</p>
        </div>

        <div v-else class="video-list">
          <div v-for="movie in movies" :key="movie.imdbID" class="video-card">
            <div class="thumbnail-container">
              <img
                :src="movie.Poster !== 'N/A' ? movie.Poster : 'https://via.placeholder.com/300x450?text=No+Image'"
                alt="movie.Title"
                class="thumbnail"
              />
              <div class="add-to-watchlist" @click.stop="markAsWatched(movie)">
                <i class="uil uil-check"></i>
              </div>
              <p class="duration">{{ movie.imdbRating || 'N/A' }}/10</p>
            </div>
            <div class="video-info">
              <div class="video-details">
                <h2 class="title">{{ movie.Title }}</h2>
                <p class="channel-name">Año: {{ movie.Year }} | {{ movie.Genre || 'Sin género' }}</p>
                <p class="views">{{ movie.Plot ? movie.Plot.slice(0, 60) + '…' : 'Sin descripción' }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const movies = ref([])
const loading = ref(true)
const error = ref(null)
const userData = JSON.parse(localStorage.getItem('currentUser'))

const fetchMovies = async () => {
  try {
    loading.value = true
    error.value = null
    
    const response = await axios.get(`http://localhost:5002/not_watched?user_id=${userData.id}`)
    console.log('Backend response:', response.data)
    
    const movieTitles = response.data.not_watched_movies
    if (!movieTitles || !Array.isArray(movieTitles)) {
      throw new Error('Formato de respuesta inesperado del backend')
    }

    const searchPromises = movieTitles.map(async (title) => {
      try {
        const cleanTitle = title.trim()
        const response = await axios.get(
          `http://localhost:5001/api/movie/search?query=${encodeURIComponent(cleanTitle)}`
        )
        
        const exactMatch = response.data.find(m => m.Title.toLowerCase() === cleanTitle.toLowerCase())
        return exactMatch || response.data[0] || {
          Title: cleanTitle,
          Year: 'N/A',
          Poster: 'https://via.placeholder.com/300x450?text=Poster+no+disponible',
          imdbID: `custom-${Math.random().toString(36).substr(2, 9)}`,
          Genre: 'N/A',
          Plot: 'Sin descripción disponible',
          imdbRating: 'N/A'
        }
      } catch (err) {
        console.error(`Error buscando "${title}":`, err)
        return {
          Title: title,
          Year: 'N/A',
          Poster: 'https://via.placeholder.com/300x450?text=Error+cargando',
          imdbID: `error-${Math.random().toString(36).substr(2, 9)}`,
          Genre: 'N/A',
          Plot: 'Sin descripción disponible',
          imdbRating: 'N/A'
        }
      }
    })

    const movieDetails = await Promise.all(searchPromises)
    movies.value = movieDetails.filter(movie => movie)
    
  } catch (err) {
    console.error('Error general:', err)
    error.value = `Error al cargar la lista: ${err.message}`
    movies.value = []
  } finally {
    loading.value = false
  }
}

const markAsWatched = async (movie) => {
  try {
    await axios.post('http://localhost:5002/mark_as_watched', {
      user_id: userData.id,
      movie_title: movie.Title,
    })
    await fetchMovies()
  } catch (error) {
    console.error('Error marking as watched:', error)
    alert('Error al marcar como vista')
  }
}

onMounted(fetchMovies)
</script>

<style scoped>
.container {
  max-width: 100%;
  padding: 0;
}

.content-wrapper {
  padding: 0 16px;
  overflow-x: hidden;
  width: 100%;
}

.video-list {
  display: grid;
  gap: 16px;
  padding: 20px 0 64px;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}

.video-card {
  text-decoration: none;
  cursor: pointer;
  transition: transform 0.2s;
}

.video-card:hover {
  transform: translateY(-5px);
}

.thumbnail-container {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
}

.thumbnail {
  width: 100%;
  height: auto;
  aspect-ratio: 2/3;
  object-fit: cover;
  background: #f0f0f0;
}

.duration {
  position: absolute;
  right: 10px;
  bottom: 12px;
  color: #fff;
  font-size: 0.875rem;
  padding: 2px 5px;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.7);
}

.add-to-watchlist {
  position: absolute;
  right: 10px;
  top: 10px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  z-index: 5;
}

.add-to-watchlist:hover {
  background: #3b82f6;
  transform: scale(1.1);
}

.add-to-watchlist i {
  font-size: 1rem;
}

.video-info {
  padding: 8px 0;
}

.title {
  font-size: 1rem;
  color: #333;
  font-weight: 600;
  line-height: 1.375;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  margin-bottom: 4px;
}

.channel-name, .views {
  font-size: 0.875rem;
  color: #666;
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 50px 0;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e5e5e5;
  border-radius: 50%;
  border-top-color: #3b82f6;
  animation: spin 1s ease-in-out infinite;
  margin-bottom: 15px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .video-list {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 12px;
    padding: 15px 0;
  }
}
</style>