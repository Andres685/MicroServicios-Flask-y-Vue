<template>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PELISCRIPT - Buscador de Películas</title>
    <!-- Linking Unicons For Icons -->
    <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
  </head>
  <body>
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
            </a>
          </div>
          <div class="nav-section">
            <button class="nav-button search-back-button" id="search-back-button">
              <i class="uil uil-arrow-left"></i>
            </button>
          </div>
          <div class="nav-section nav-center">
            <form action="#" class="search-form" id="search-form">
              <input type="search" placeholder="Buscar películas" class="search-input" id="search-input" required />
              <button class="nav-button search-button" type="submit">
                <i class="uil uil-search"></i>
              </button>
              <!-- Auto-sugerencias para búsqueda -->
              <div class="search-suggestions" id="search-suggestions"></div>
            </form>
            <button class="nav-button mic-button">
              <i class="uil uil-microphone"></i>
            </button>
          </div>
          <div class="nav-section nav-right">
            <button class="nav-button search-button" id="search-button">
              <i class="uil uil-search"></i>
            </button>
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
              <router-link to="/catalogo" class="link-item active"> 
                <i class="uil uil-estate"></i> Inicio 
              </router-link>
              <router-link to="/por-ver" class="link-item"> 
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
          <!-- Category List -->
          <div class="category-container">
            <div class="category-list">
            <button class="category-button active" data-category="all">Todo</button>
            <button class="category-button" data-category="accion">Action</button>
            <button class="category-button" data-category="aventura">Adventure</button>
            <button class="category-button" data-category="thriller">Thriller</button>
            <button class="category-button" data-category="fantasia">Fantasy</button>
            <button class="category-button" data-category="terror">Terror</button>
            <button class="category-button" data-category="documentary">Documentales</button>
            <button class="category-button" data-category="animation">Animation</button>
            <button class="category-button" data-category="animation">Crime</button>
            <button class="category-button" data-category="animation">Drama</button>
            <button class="category-button" data-category="animation">Mystery</button>
            <button class="category-button" data-category="animation">Romance</button>
            <button class="category-button" data-category="animation">Sci-Fi</button>
            <button class="category-button" data-category="animation">Comedy</button>
            </div>
          </div>
          <!-- Mensaje para búsqueda -->
          <div id="search-results-info" class="search-results-info" style="display: none;">
            <h3>Resultados para: <span id="search-term"></span></h3>
            <button id="clear-search" class="clear-search-button">Limpiar búsqueda</button>
          </div>
          <!-- Video List -->
          <div class="video-list" id="video-list">
            <!-- Se llenará dinámicamente via JavaScript -->
          </div>
          <!-- Cargando indicador -->
          <div id="loading" class="loading">
            <div class="spinner"></div>
            <p>Cargando películas...</p>
          </div>
        </div> 
      </main>
    </div>
  </body>
</template>
  
<style>
    /* Importing Google Font - Open Sans */
@import url("https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Open Sans", sans-serif;
}
/* Color variables for light theme */
:root {
  --white-color: #fff;
  --black-color: #000;
  --light-white-color: #f0f0f0;
  --light-gray-color: #e5e5e5;
  --border-color: #ccc;
  --primary-color: #3b82f6;
  --secondary-color: #404040;
  --overlay-dark-color: rgba(0, 0, 0, 0.6);
}
/* Color variables for dark theme */
.dark-mode {
  --white-color: #171717;
  --black-color: #d4d4d4;
  --light-white-color: #333;
  --light-gray-color: #404040;
  --border-color: #808080;
  --secondary-color: #d4d4d4;
}
body {
  background: var(--white-color);
}
.container {
  display: flex;
  overflow: hidden;
  max-height: 100vh;
  flex-direction: column;
}
header .sidebar .nav-left,
.category-list {
  position: sticky;
  top: 0;
  z-index: 1;
  background: var(--white-color);
}
.navbar {
  display: flex;
  gap: 32px;
  align-items: center;
  padding: 8px 16px;
  justify-content: space-between;
}
:where(.navbar, .sidebar) .nav-section {
  gap: 16px;
}
:where(.navbar, .sidebar) :where(.nav-section, .nav-logo, .search-form) {
  display: flex;
  align-items: center;
}
:where(.navbar, .sidebar) :where(.logo-image, .user-image) {
  width: 32px;
  cursor: pointer;
  border-radius: 50%;
}
:where(.navbar, .sidebar) .nav-section .nav-button {
  border: none;
  height: 40px;
  width: 40px;
  cursor: pointer;
  background: none;
  border-radius: 50%;
}
:where(.navbar, .sidebar) .nav-section .nav-button:hover {
  background: var(--light-gray-color) !important;
}
:where(.navbar, .sidebar) .nav-button i {
  font-size: 1.5rem;
  display: flex;
  color: var(--black-color);
  align-items: center;
  justify-content: center;
}
:where(.navbar, .sidebar) .nav-logo {
  display: flex;
  gap: 8px;
  text-decoration: none;
}
:where(.navbar, .sidebar) .nav-logo .logo-text {
  color: var(--black-color);
  font-size: 1.25rem;
}
.navbar .search-back-button {
  display: none;
}
.navbar .nav-center {
  gap: 8px;
  width: 100%;
  display: flex;
  justify-content: center;
  position: relative;
}
.navbar .search-form {
  flex: 1;
  height: 40px;
  max-width: 550px;
  position: relative;
}
.navbar .search-form .search-input {
  width: 100%;
  height: 100%;
  font-size: 1rem;
  padding: 0 16px;
  outline: none;
  color: var(--black-color);
  background: var(--white-color);
  border-radius: 49px 0 0 49px;
  border: 1px solid var(--border-color);
}
.navbar .search-form .search-input:focus {
  border-color: var(--primary-color);
}
.navbar .search-form .search-button {
  height: 40px;
  width: auto;
  padding: 0 20px;
  border-radius: 0 49px 49px 0;
  border: 1px solid var(--border-color);
  border-left: 0;
}
.navbar .nav-center .mic-button {
  background: var(--light-white-color);
}
.navbar .nav-right .search-button {
  display: none;
}
/* Estilo para las sugerencias de búsqueda */
.search-suggestions {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  max-height: 300px;
  overflow-y: auto;
  background: var(--white-color);
  border: 1px solid var(--border-color);
  border-radius: 0 0 15px 15px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  z-index: 100000;
  display: none;
}
.search-suggestions.show {
  display: block;
}
.suggestion-item {
  padding: 10px 15px;
  cursor: pointer;
  display: flex;
  align-items: center;
}
.suggestion-item:hover {
  background-color: var(--light-gray-color);
}
.suggestion-item i {
  margin-right: 10px;
  color: var(--secondary-color);
}
/* Estilo para la información de búsqueda */
.search-results-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 5px;
  margin-top: 10px;
  border-bottom: 1px solid var(--border-color);
  
}
.clear-search-button {
  padding: 6px 12px;
  background-color: var(--light-gray-color);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
}
.clear-search-button:hover {
  background-color: var(--border-color);
}
/* Estilo para el cargador */
.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 50px 0;
  display: none;
}
.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid var(--light-gray-color);
  border-radius: 50%;
  border-top-color: var(--primary-color);
  animation: spin 1s ease-in-out infinite;
  margin-bottom: 15px;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}
.main-layout {
  display: flex;
  overflow-y: auto;
  scrollbar-color: #a6a6a6 transparent;
}
.main-layout .sidebar {
  width: 280px;
  overflow: hidden;
  padding: 0 11px 0;
  background: var(--white-color);
}
.main-layout .sidebar .nav-left {
  display: none;
  padding: 8px 5px;
}
body.sidebar-hidden .main-layout .sidebar {
  width: 0;
  padding: 0;
}
.sidebar .links-container {
  padding: 16px 0 32px;
  overflow-y: auto;
  height: calc(100vh - 60px);
  scrollbar-width: thin;
  scrollbar-color: transparent transparent;
}
.sidebar .links-container:hover {
  scrollbar-color: #a6a6a6 transparent;
}
.sidebar .link-section {
  list-style: none;
}
.sidebar .link-section .link-item {
  display: flex;
  cursor: pointer;
  color: var(--black-color);
  white-space: nowrap;
  align-items: center;
  font-size: 0.938rem;
  padding: 5px 12px;
  margin-bottom: 4px;
  border-radius: 8px;
  text-decoration: none;
}
.sidebar .link-section .link-item:hover {
  background: var(--light-gray-color);
}
.sidebar .link-section .link-item i {
  font-size: 1.4rem;
  margin-right: 10px;
}
.sidebar .link-section .section-title {
  color: var(--black-color);
  font-weight: 600;
  font-size: 0.938rem;
  margin: 16px 0 8px 8px;
}
.sidebar .section-separator {
  height: 1px;
  margin: 10px 0;
  background: var(--light-gray-color);
}
.main-layout .content-wrapper {
  padding: 0 16px;
  overflow-x: hidden;
  width: 100%;
}
.content-wrapper .category-list {
  display:flex;
  overflow-x: auto;
  gap: 12px;
  padding: 12px 0 11px;
  scrollbar-width:auto;
}

.category-container {
  position: relative;
  margin: 0 15px;
}

.category-list {
  scroll-behavior: smooth;
  scrollbar-width: none; /* Para Firefox */
  -ms-overflow-style: none; /* Para IE y Edge */
}

.category-list::-webkit-scrollbar {
  display: none; /* Para Chrome, Safari y Opera */
}

.category-nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: var(--white-color);
  border: 1px solid var(--border-color);
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 5;
}

.category-prev-btn {
  left: -15px;
}

.category-next-btn {
  right: -15px;
}

.category-nav-btn i {
  font-size: 1.2rem;
  color: var(--black-color);
}
.category-list .category-button {
  border: none;
  cursor: pointer;
  font-weight: 500;
  font-size: 0.94rem;
  border-radius: 8px;
  white-space: nowrap;
  color: var(--black-color);
  padding: 6px 12px;
  background: var(--light-gray-color);
}
.category-list .category-button.active {
  color: var(--white-color);
  background: var(--black-color);
  pointer-events: none;
}
.dark-mode .category-list .category-button.active {
  filter: brightness(120%);
}
.category-list .category-button:not(.active):hover {
  background: var(--border-color);
}
.content-wrapper .video-list {
  display: grid;
  gap: 16px;
  padding: 20px 0 64px;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}
.content-wrapper .video-list .video-card {
  text-decoration: none;
}
.content-wrapper .video-list .video-card .thumbnail-container {
  position: relative;
}
.content-wrapper .video-list .video-card .thumbnail {
  width: 100%;
  object-fit: contain;
  border-radius: 8px;
  aspect-ratio: auto;
  background: var(--light-white-color);
}
.content-wrapper .video-list .video-card .duration {
  position: absolute;
  right: 10px;
  bottom: 12px;
  color: #fff;
  font-size: 0.875rem;
  padding: 0 5px;
  border-radius: 5px;
  background: var(--overlay-dark-color);
}
.content-wrapper .video-list .video-card .video-info {
  display: flex;
  gap: 11px;
  padding: 11px 8px;
}
.content-wrapper .video-list .video-card .icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
}
.content-wrapper .video-list .video-card .title {
  font-size: 1rem;
  color: var(--black-color);
  font-weight: 600;
  line-height: 1.375;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}
.content-wrapper .video-list .video-card:hover .title {
  color: var(--primary-color);
}
.content-wrapper .video-list .video-card p {
  font-size: 0.875rem;
  color: var(--secondary-color);
}
.content-wrapper .video-list .video-card .channel-name {
  margin: 4px 0 2px;
}
/* Responsive media code for small devices */
@media (max-width: 768px) {
  .navbar {
    gap: 1rem;
  }
  .navbar .nav-center,
  body.show-mobile-search .navbar .nav-left,
  body.show-mobile-search .navbar .nav-right {
    display: none;
  }
  .navbar .nav-right .search-button,
  body.show-mobile-search .navbar .search-back-button,
  body.show-mobile-search .navbar .nav-center {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .main-layout .screen-overlay {
    position: absolute;
    left: 0;
    top: 0;
    z-index: 15;
    width: 100%;
    height: 100vh;
    background: var(--overlay-dark-color);
    transition: 0.2s ease;
  }
  body.sidebar-hidden .main-layout .screen-overlay {
    opacity: 0;
    pointer-events: none;
  }
  .main-layout .sidebar {
    position: absolute;
    left: 0;
    top: 0;
    z-index: 20;
    height: 100vh;
    transition: 0.2s ease;
  }
  body.sidebar-hidden .main-layout .sidebar {
    left: -280px;
  }
  .main-layout .sidebar .nav-left {
    display: flex;
  }

  /* Añade esto a tu CSS */
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
  background: var(--primary-color);
  transform: scale(1.1);
}

.add-to-watchlist.added {
  background: var(--primary-color);
}


/* Contenedor para los botones de navegación de categorías */
.category-container {
  position: relative;
  margin: 0 15px;
}

.category-list {
  scroll-behavior: smooth;
  scrollbar-width: none; /* Para Firefox */
  -ms-overflow-style: none; /* Para IE y Edge */
}

.category-list::-webkit-scrollbar {
  display: none; /* Para Chrome, Safari y Opera */
}

.category-nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: var(--white-color);
  border: 1px solid var(--border-color);
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 5;
}

.category-prev-btn {
  left: -15px;
}

.category-next-btn {
  right: -15px;
}

.category-nav-btn i {
  font-size: 1.2rem;
  color: var(--black-color);
}

/* Estilos para el botón "Añadir a Por Ver" */
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
  background: var(--theme-color);
  transform: scale(1.1);
}

.add-to-watchlist.added {
  background: var(--theme-color);
}

}
</style>
<script>
document.addEventListener("DOMContentLoaded", function() {
  const API_BASE_URL = 'http://localhost:5001';
  let allMovies = []; 
  let currentMovies = [];
  let currentCategory = 'all';
  let currentSearchTerm = '';
  
  // --- Elementos del DOM ---
  const menuButtons = document.querySelectorAll(".menu-button");
  const screenOverlay = document.querySelector(".main-layout .screen-overlay");
  const themeButton = document.querySelector(".navbar .theme-button i");
  const searchButton = document.getElementById("search-button");
  const searchBackButton = document.getElementById("search-back-button");
  const searchInput = document.getElementById("search-input");
  const searchForm = document.getElementById("search-form");
  const searchSuggestions = document.getElementById("search-suggestions");
  const videoListContainer = document.getElementById("video-list");
  const categoryButtons = document.querySelectorAll(".category-button");
  const searchResultsInfo = document.getElementById("search-results-info");
  const searchTermDisplay = document.getElementById("search-term");
  const clearSearchButton = document.getElementById("clear-search");
  const loadingIndicator = document.getElementById("loading");
  const categoryPrevBtn = document.querySelector('.category-prev-btn');
  const categoryNextBtn = document.querySelector('.category-next-btn');
  const categoryList = document.querySelector('.category-list');
  const themeOptions = document.querySelectorAll('.theme-option');

  // --- Títulos de películas para cargar (reducidos a 10) ---
  const titles = [
  'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction',
  'The Lord of the Rings: The Return of the King', 'Forrest Gump', 'Inception', 'Fight Club',
  'The Matrix', 'Interstellar', 'The Matrix Reloaded', 'The Matrix Revolutions',
  'The Godfather Part II', 'The Dark Knight Rises', 'The Lord of the Rings: The Fellowship of the Ring',
  'The Lord of the Rings: The Two Towers', 'The Silence of the Lambs', 'Se7en', 'The Usual Suspects',
  'Saving Private Ryan', 'The Avengers', 'The Departed', 'Gladiator']/*, 'The Lion King', 'Titanic',
  'Jurassic Park', 'Star Wars: Episode IV - A New Hope', 'Star Wars: Episode V - The Empire Strikes Back',
  'Star Wars: Episode VI - Return of the Jedi', 'The Prestige', 'The Green Mile', 'The Intouchables',
  'The Pianist', 'The Social Network', 'The Wolf of Wall Street', 'Django Unchained',
  'The Shape of Water', 'Parasite', 'The Grand Budapest Hotel', 'Mad Max: Fury Road',
  'Spider-Man: Into the Spider-Verse', 'Coco', 'The Revenant', 'Avatar', 'Avengers: Endgame',
  'Avengers: Infinity War', 'Black Panther', 'Joker', 'Toy Story', 'Toy Story 2', 'Toy Story 3',
  'Toy Story 4', 'Up', 'Finding Nemo', 'Inside Out', 'Monsters, Inc.', 'Shrek', 'Shrek 2',
  'Shrek the Third', 'Frozen', 'Frozen II', 'Beauty and the Beast', 'Aladdin', 'Mulan',
  'Moana', 'Encanto', 'Ratatouille', 'Soul', 'Luca', 'Turning Red', 'Brave', 'Big Hero 6',
  'Zootopia', 'The Incredibles', 'The Incredibles 2', 'Despicable Me', 'Despicable Me 2',
  'Minions', 'Despicable Me 3', 'Kung Fu Panda', 'Kung Fu Panda 2', 'How to Train Your Dragon',
  'How to Train Your Dragon 2', 'How to Train Your Dragon: The Hidden World',
  'Spider-Man: No Way Home', 'Doctor Strange', 'Doctor Strange in the Multiverse of Madness',
  'Thor: Ragnarok', 'Thor: Love and Thunder', 'Iron Man', 'Iron Man 2', 'Iron Man 3',
  'Captain America: The First Avenger', 'Captain America: The Winter Soldier',
  'Captain America: Civil War', 'Guardians of the Galaxy', 'Guardians of the Galaxy Vol. 2',
  'Ant-Man', 'Ant-Man and the Wasp', 'Deadpool', 'Deadpool 2', 'Logan', 'X-Men: Days of Future Past',
  'X-Men: First Class', 'Venom', 'Venom: Let There Be Carnage', 'The Hunger Games',
  'The Hunger Games: Catching Fire', 'The Hunger Games: Mockingjay Part 1',
  'The Hunger Games: Mockingjay Part 2', 'Twilight', 'New Moon', 'It', 'It Chapter Two', 'A Quiet Place', 'A Quiet Place Part II',
  'The Conjuring', 'The Conjuring 2', 'Annabelle', 'Annabelle: Creation', 'Top Gun',
  'Top Gun: Maverick', 'Oppenheimer', 'Barbie', 'The Super Mario Bros. Movie',
  'John Wick', 'John Wick: Chapter 2', 'John Wick: Chapter 3 – Parabellum',
  'John Wick: Chapter 4', 'The Batman', 'Batman Begins', 'Man of Steel',
  'Zack Snyder’s Justice League', 'Aquaman', 'The Flash', 'The Lego Movie',
  'The Lego Batman Movie', 'The Lego Ninjago Movie', 'The Croods', 'The Croods: A New Age',
  'Sing', 'Sing 2', 'The Secret Life of Pets', 'The Secret Life of Pets 2',
  'Tangled', 'The Good Dinosaur'
  ]*/;

  // --- Funciones de la interfaz de usuario ---
  if (menuButtons.length > 0) {
    menuButtons.forEach(btn => btn.addEventListener("click", () => document.body.classList.toggle("sidebar-hidden")));
  }
  
  if (screenOverlay) {
    screenOverlay.addEventListener("click", () => document.body.classList.toggle("sidebar-hidden"));
  }
  
  // Manejo del tema oscuro/claro
  if (themeButton) {
    if (localStorage.getItem("darkMode") === "enabled") {
      document.body.classList.add("dark-mode");
      themeButton.classList.replace("uil-moon", "uil-sun");
    } else {
      themeButton.classList.replace("uil-sun", "uil-moon");
    }
    
    themeButton.addEventListener("click", () => {
      const isDark = document.body.classList.toggle("dark-mode");
      localStorage.setItem("darkMode", isDark ? "enabled" : "disabled");
      themeButton.classList.toggle("uil-sun", isDark);
      themeButton.classList.toggle("uil-moon", !isDark);
    });
  }
  
  // Cargar tema de color guardado
  const savedTheme = localStorage.getItem('colorTheme') || 'blue';
  document.body.className = document.body.className.replace(/theme-\w+/g, '');
  document.body.classList.add(`theme-${savedTheme}`);

  // Actualizar UI de temas
  if (themeOptions && themeOptions.length > 0) {
    themeOptions.forEach(option => {
      const theme = option.getAttribute('data-theme');
      if (theme === savedTheme) {
        option.classList.add('active');
      } else {
        option.classList.remove('active');
      }
      
      option.addEventListener('click', () => {
        // Actualizar tema
        document.body.className = document.body.className.replace(/theme-\w+/g, '');
        document.body.classList.add(`theme-${theme}`);
        localStorage.setItem('colorTheme', theme);
        
        // Actualizar UI
        themeOptions.forEach(opt => opt.classList.remove('active'));
        option.classList.add('active');
      });
    });
  }
  
  if (window.innerWidth >= 768) { 
    document.body.classList.remove("sidebar-hidden"); 
  }
  
  const toggleSearch = () => document.body.classList.toggle("show-mobile-search");
  if (searchButton) searchButton.addEventListener("click", toggleSearch);
  if (searchBackButton) searchBackButton.addEventListener("click", () => searchButton.click());

  // Navegación de categorías
  if (categoryPrevBtn && categoryList) {
    categoryPrevBtn.addEventListener('click', () => {
      categoryList.scrollBy({ left: -200, behavior: 'smooth' });
    });
  }
  
  if (categoryNextBtn && categoryList) {
    categoryNextBtn.addEventListener('click', () => {
      categoryList.scrollBy({ left: 200, behavior: 'smooth' });
    });
  }

  // --- Funciones para la búsqueda y autocompletado ---
  
  // Manejador para el formulario de búsqueda
  if (searchForm) {
    searchForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const searchTerm = searchInput.value.trim();
      if (searchTerm) {
        currentSearchTerm = searchTerm;
        searchTermDisplay.textContent = searchTerm;
        searchResultsInfo.style.display = 'flex';
        filterMovies();
        searchSuggestions.classList.remove('show');
      }
    });
  }
  
  // Manejador para el input de búsqueda (autocompletado)
  if (searchInput) {
    searchInput.addEventListener('input', function() {
      const term = this.value.trim();
      if (term.length > 1) {
        const suggestions = getSuggestions(term);
        updateSuggestions(suggestions);
        searchSuggestions.classList.add('show');
      } else {
        searchSuggestions.classList.remove('show');
      }
    });
    
    // Ocultar sugerencias al perder el foco
    searchInput.addEventListener('blur', function() {
      // Pequeño retraso para permitir hacer clic en una sugerencia
      setTimeout(() => {
        searchSuggestions.classList.remove('show');
      }, 200);
    });
    
    // Mostrar sugerencias al enfocar si hay texto
    searchInput.addEventListener('focus', function() {
      if (this.value.trim().length > 1) {
        const suggestions = getSuggestions(this.value.trim());
        updateSuggestions(suggestions);
        searchSuggestions.classList.add('show');
      }
    });
  }
  
  // Limpiar búsqueda
  if (clearSearchButton) {
    clearSearchButton.addEventListener('click', function() {
      currentSearchTerm = '';
      searchInput.value = '';
      searchResultsInfo.style.display = 'none';
      filterMovies();
    });
  }
  
  // Obtener sugerencias basadas en el término de búsqueda
  function getSuggestions(term) {
    if (!allMovies.length) return [];
    
    term = term.toLowerCase();
    return allMovies
      .filter(movie => 
        movie.Title.toLowerCase().includes(term) || 
        (movie.Genre && movie.Genre.toLowerCase().includes(term)) ||
        (movie.Director && movie.Director.toLowerCase().includes(term)) ||
        (movie.Actors && movie.Actors.toLowerCase().includes(term))
      )
      .slice(0, 6) // Limitar a 6 sugerencias
      .map(movie => movie.Title);
  }
  
  // Actualizar la lista de sugerencias en el DOM
  function updateSuggestions(suggestions) {
    searchSuggestions.innerHTML = '';
    
    suggestions.forEach(suggestion => {
      const item = document.createElement('div');
      item.className = 'suggestion-item';
      item.innerHTML = `<i class="uil uil-search"></i> ${suggestion}`;
      
      item.addEventListener('click', function() {
        searchInput.value = suggestion;
        currentSearchTerm = suggestion;
        searchTermDisplay.textContent = suggestion;
        searchResultsInfo.style.display = 'flex';
        filterMovies();
        searchSuggestions.classList.remove('show');
      });
      
      searchSuggestions.appendChild(item);
    });
  }
  
  // --- Funciones para filtrado de categorías ---
  
  // Manejador para botones de categoría
  if (categoryButtons.length > 0) {
    categoryButtons.forEach(button => {
      button.addEventListener('click', function() {
        // Actualizar botones activos
        categoryButtons.forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');
        
        // Establecer categoría actual
        currentCategory = this.getAttribute('data-category');
        filterMovies();
      });
    });
  }
  
  // Filtrar películas por categoría y término de búsqueda
  function filterMovies() {
    if (!allMovies.length) return;
    
    currentMovies = allMovies.filter(movie => {
      const matchesCategory = currentCategory === 'all' || 
        (movie.Genre && movie.Genre.toLowerCase().includes(currentCategory.toLowerCase()));
      
      const matchesSearch = !currentSearchTerm || 
        movie.Title.toLowerCase().includes(currentSearchTerm.toLowerCase()) ||
        (movie.Genre && movie.Genre.toLowerCase().includes(currentSearchTerm.toLowerCase())) ||
        (movie.Director && movie.Director.toLowerCase().includes(currentSearchTerm.toLowerCase())) ||
        (movie.Actors && movie.Actors.toLowerCase().includes(currentSearchTerm.toLowerCase())) ||
        (movie.Plot && movie.Plot.toLowerCase().includes(currentSearchTerm.toLowerCase()));
      
      return matchesCategory && matchesSearch;
    });
    
    renderMovies(currentMovies);
  }
  
  // --- Funciones para cargar y renderizar películas ---
  
  // Cargar película por título usando la API de OMDb
  /*
  function loadMovie(title) {
  return fetch(`${API_BASE_URL}/api/movie/title?title=${encodeURIComponent(title)}`)
    .then(res => res.json())
    .then(movie => {
      if (movie.Response === 'True' || movie.Title) {
        return movie;
      }
      return null;
    })
    .catch(err => {
      console.error('Error cargando película:', err);
      return null;
    });
  }*/
  
  // Cargar todas las películas en lotes
  async function loadAllMovies() {
  loadingIndicator.style.display = 'flex';
  videoListContainer.innerHTML = '';
  
  try {
    const response = await fetch(`${API_BASE_URL}/api/listar/todo`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ titles: titles })
    });
    
    const data = await response.json();
    
    if (data && data.movies) {
      allMovies = data.movies;
      currentMovies = [...allMovies];
      renderMovies(currentMovies);
    } else {
      allMovies = [];
      videoListContainer.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 50px;">
          <i class="uil uil-sad" style="font-size: 48px;"></i>
          <h3>No se pudieron cargar las películas</h3>
          <p>Intente nuevamente más tarde.</p>
        </div>
      `;
    }
  } catch (error) {
    console.error('Error cargando películas:', error);
    videoListContainer.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 50px;">
        <i class="uil uil-sad" style="font-size: 48px;"></i>
        <h3>Error al cargar películas</h3>
        <p>Por favor intente nuevamente más tarde.</p>
      </div>
    `;
  } finally {
    loadingIndicator.style.display = 'none';
    filterMovies(); // Aplicar filtros iniciales
  }
}
  
  // Renderizar las películas en el DOM
  function renderMovies(movies) {
    videoListContainer.innerHTML = '';
    
    if (movies.length === 0) {
      videoListContainer.innerHTML =`
        <div style="grid-column: 1 / -1; text-align: center; padding: 50px;">
          <i class="uil uil-sad" style="font-size: 48px;"></i>
          <h3>No se encontraron películas</h3>
          <p>Intenta con otra búsqueda o selecciona otra categoría.</p>
        </div>
      `;
      return;
    }
    
    movies.forEach(movie => {
      const card = document.createElement('a');
      card.href = '#';
      card.className = 'video-card';
      
      // Validar la URL del poster antes de mostrarla
      const posterUrl = movie.Poster && movie.Poster !== 'N/A' 
        ? movie.Poster 
        : 'https://via.placeholder.com/300x450?text=No+Image';
      
      card.innerHTML = `
        <div class="thumbnail-container">
          <img src="${posterUrl}" alt="${movie.Title}" class="thumbnail" />
          <div class="add-to-watchlist" data-id="${movie.imdbID}">
            <i class="uil uil-plus"></i>
          </div>
          <p class="duration">${movie.imdbRating}/10</p>
        </div>
        <div class="video-info">
          <div class="video-details">
            <h2 class="title">${movie.Title}</h2>
            <p class="channel-name">Año: ${movie.Year} | ${movie.Genre || 'Sin género'}</p>
            <p class="views">${movie.Plot ? movie.Plot.slice(0, 60) + '…' : 'Sin descripción'}</p>
          </div>
        </div>
      `;
      
      videoListContainer.appendChild(card);
      
      // Evento para el modal de detalles 
      card.addEventListener('click', function(e) {
        // Prevenir que el clic en el botón de watchlist abra el modal
        if (e.target.closest('.add-to-watchlist')) {
          e.preventDefault();
          return;
        }
        e.preventDefault();
        showMovieDetails(movie);
      });
      
      // Evento para añadir a "Por Ver"
      const addButton = card.querySelector('.add-to-watchlist');
      addButton.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        toggleWatchlist(movie);
      });
    });
    
    // Marcar las películas que ya están en "Por Ver"
    updateWatchlistUI();
  }
  
  // Funciones para gestionar la lista "Por Ver"
  function toggleWatchlist(movie) {
    let watchlist = JSON.parse(localStorage.getItem('watchlist') || '[]');
    
    const index = watchlist.findIndex(item => item.imdbID === movie.imdbID);
    
    if (index === -1) {
      watchlist.push({
        imdbID: movie.imdbID,
        Title: movie.Title,
        Poster: movie.Poster,
        Year: movie.Year
      });
      showToast(`${movie.Title} añadida a Por Ver`);
    } else {
      watchlist.splice(index, 1);
      showToast(`${movie.Title} eliminada de Por Ver`);
    }
    
    localStorage.setItem('watchlist', JSON.stringify(watchlist));
    updateWatchlistUI();
  }

  function updateWatchlistUI() {
    let watchlist = JSON.parse(localStorage.getItem('watchlist') || '[]');
    
    document.querySelectorAll('.add-to-watchlist').forEach(button => {
      const movieId = button.getAttribute('data-id');
      const isInWatchlist = watchlist.some(item => item.imdbID === movieId);
      
      if (isInWatchlist) {
        button.classList.add('added');
        button.innerHTML = '<i class="uil uil-check"></i>';
      } else {
        button.classList.remove('added');
        button.innerHTML = '<i class="uil uil-plus"></i>';
      }
    });
  }

  // Función para cargar películas en "Por Ver"
  function loadWatchlistMovies() {
    const watchlist = JSON.parse(localStorage.getItem('watchlist') || '[]');
    
    // Solo si estamos en la página de "Por Ver"
    if (document.querySelector('.link-item.watchlist-page.active')) {
      if (watchlist.length === 0) {
        videoListContainer.innerHTML = `
          <div style="grid-column: 1 / -1; text-align: center; padding: 50px;">
            <i class="uil uil-bookmark" style="font-size: 48px;"></i>
            <h3>No tienes películas guardadas</h3>
            <p>Añade películas a tu lista "Por Ver" haciendo clic en el botón + de cualquier película.</p>
          </div>
        `;
      } else {
        renderMovies(watchlist);
      }
    }
  }
  
  // Mostrar detalles de la película (modal)
  function showMovieDetails(movie) {
    // Crear un modal para mostrar detalles de la película
    const modal = document.createElement('div');
    modal.className = 'movie-modal';
    
    const posterUrl = movie.Poster && movie.Poster !== 'N/A' 
      ? movie.Poster 
      : 'https://via.placeholder.com/300x450?text=No+Image';
    
    modal.innerHTML = `
      <div class="movie-modal-content">
        <span class="close-modal">&times;</span>
        <div class="movie-details">
          <div class="movie-poster">
            <img src="${posterUrl}" alt="${movie.Title}" />
          </div>
          <div class="movie-info">
            <h2>${movie.Title} <span>(${movie.Year})</span></h2>
            <p class="rating"><strong>Rating:</strong> ${movie.imdbRating}/10</p>
            <p><strong>Género:</strong> ${movie.Genre || 'N/A'}</p>
            <p><strong>Director:</strong> ${movie.Director || 'N/A'}</p>
            <p><strong>Actores:</strong> ${movie.Actors || 'N/A'}</p>
            <p><strong>Duración:</strong> ${movie.Runtime || 'N/A'}</p>
            <p class="plot"><strong>Sinopsis:</strong> ${movie.Plot || 'Sin descripción disponible'}</p>
            <button class="watch-later-btn" data-id="${movie.imdbID}">
              ${isInWatchlist(movie.imdbID) ? 'Quitar de Por Ver' : 'Añadir a Por Ver'}
            </button>
          </div>
        </div>
      </div>
    `;
    
    document.body.appendChild(modal);
    
    // Añadir estilo al modal
    const style = document.createElement('style');
    style.innerHTML = `
      .movie-modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
      }
      .movie-modal-content {
        background-color: var(--white-color);
        border-radius: 8px;
        max-width: 90%;
        max-height: 90%;
        width: 800px;
        overflow: auto;
        position: relative;
      }
      .close-modal {
        position: absolute;
        top: 15px;
        right: 15px;
        font-size: 28px;
        cursor: pointer;
        color: var(--black-color);
      }
      .movie-details {
        display: flex;
        padding: 20px;
        gap: 20px;
        flex-direction: column;
      }
      @media (min-width: 768px) {
        .movie-details {
          flex-direction: row;
        }
      }
      .movie-poster {
        flex: 0 0 auto;
        max-width: 300px;
      }
      .movie-poster img {
        width: 100%;
        border-radius: 8px;
      }
      .movie-info {
        flex: 1;
      }
      .movie-info h2 {
        margin-bottom: 15px;
        color: var(--black-color);
      }
      .movie-info h2 span {
        font-weight: normal;
        font-size: 0.8em;
      }
      .movie-info p {
        margin-bottom: 10px;
        color: var(--black-color);
      }
      .movie-info .rating {
        font-size: 1.1em;
        color: var(--theme-color);
      }
      .movie-info .plot {
        line-height: 1.6;
        margin-top: 15px;
      }
      .watch-later-btn {
        margin-top: 20px;
        padding: 10px 20px;
        background-color: var(--theme-color);
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.2s ease;
      }
      .watch-later-btn:hover {
        opacity: 0.9;
      }
    `;
    
    document.head.appendChild(style);
    
    // Evento para el botón "Añadir a Por Ver" del modal
    const watchLaterBtn = modal.querySelector('.watch-later-btn');
    watchLaterBtn.addEventListener('click', function() {
      toggleWatchlist(movie);
      this.textContent = isInWatchlist(movie.imdbID) ? 'Quitar de Por Ver' : 'Añadir a Por Ver';
    });
    
    // Cerrar modal al hacer clic en X o fuera del contenido
    const closeBtn = modal.querySelector('.close-modal');
    closeBtn.addEventListener('click', () => {
      document.body.removeChild(modal);
    });
    
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        document.body.removeChild(modal);
      }
    });
  }
  
  // Verificar si una película está en la lista "Por Ver"
  function isInWatchlist(movieId) {
    const watchlist = JSON.parse(localStorage.getItem('watchlist') || '[]');
    return watchlist.some(item => item.imdbID === movieId);
  }
  
  // Función para mostrar notificaciones temporales
  function showToast(message) {
    // Eliminar toast anterior si existe
    const existingToast = document.querySelector('.toast-notification');
    if (existingToast) {
      document.body.removeChild(existingToast);
    }
    
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
      toast.classList.add('show');
    }, 10);
    
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => {
        if (document.body.contains(toast)) {
          document.body.removeChild(toast);
        }
      }, 300);
    }, 3000);
  }
  
  // --- Inicializar la aplicación ---
  loadAllMovies();
  
  // Agregar manejadores para navegación de secciones
  const navLinks = document.querySelectorAll('.link-item');
  if (navLinks.length > 0) {
    navLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Actualizar clases activas
        navLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
        
        // Manejar navegación a diferentes secciones
        if (this.classList.contains('watchlist-link')) {
          loadWatchlistMovies();
        } else {
          // Si es la página de inicio, mostrar todas las películas
          currentCategory = 'all';
          currentSearchTerm = '';
          searchInput.value = '';
          searchResultsInfo.style.display = 'none';
          
          // Actualizar UI para los botones de categoría
          categoryButtons.forEach(btn => {
            if (btn.getAttribute('data-category') === 'all') {
              btn.classList.add('active');
            } else {
              btn.classList.remove('active');
            }
          });
          
          filterMovies();
        }
      });
    });
  }
});
</script>