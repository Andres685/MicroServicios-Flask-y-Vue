<template>
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PELISCRIPT - Buscador de Películas</title>
    <!-- Linking Unicons For Icons -->
    <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
  </head>
    <div class="container">
        <!-- Header / Navbar -->
        <header>
        <nav class="navbar">
            <div class="nav-section nav-left">
            <button class="nav-button menu-button" @click="toggleSidebar">
                <i class="uil uil-bars"></i>
            </button>
            <a href="#" class="nav-logo">
                <img src="../assets/logoSoft.png" alt="Logo" class="logo-image" />
                <h2 class="logo-text">PELISCRIPT</h2>
            </a>
            </div>
            <div class="nav-section nav-right">
            <button class="nav-button theme-button" @click="toggleTheme">
                <i class="uil uil-moon"></i>
            </button>
            <img src='../assets/logo.png' alt="User Image" class="user-image" />
            </div>
        </nav>
        </header>
        <!-- Main Layout -->
        <main class="main-layout">
        <div class="screen-overlay" @click="closeSidebar"></div>
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="nav-section nav-left">
            <button class="nav-button menu-button" @click="toggleSidebar">
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
                <router-link to="/por-ver" class="link-item"> 
                <i class="uil uil-tv-retro"></i> Por Ver 
                </router-link>
            </div>
            <div class="section-separator"></div>
            <div class="link-section">
                <h4 class="section-title">Cuenta</h4>
                <router-link to="/perfil" class="link-item active"> 
                <i class="uil uil-user-square"></i> Tu Perfil 
                </router-link>
                <a href="#" id="logout-link" class="link-item" @click="logout">
                <i class="uil uil-sign-out-alt"></i> Cerrar Sesión
                </a>
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
            <!-- Perfil de Usuario -->
            <div class="profile-container">
            <div class="profile-header">
                <div class="profile-avatar">
                <img src="@/assets/hero-img.jpg" alt="Avatar" class="avatar-image" />
                <button class="change-avatar-btn">
                    <i class="uil uil-camera"></i>
                </button>
                </div>
                <h1 class="profile-title">Mi Perfil</h1>
            </div>
            
            <div class="profile-info">
                <form @submit.prevent="updateProfile" class="profile-form">
                <div class="form-group">
                    <label for="username">Nombre de usuario</label>
                    <input 
                    type="text" 
                    id="username" 
                    v-model="userData.username" 
                    :disabled="!isEditing" 
                    class="profile-input"
                    />
                </div>
                
                <div class="form-group">
                    <label for="email">Correo electrónico</label>
                    <input 
                    type="email" 
                    id="email" 
                    v-model="userData.email" 
                    :disabled="!isEditing" 
                    class="profile-input"
                    />
                </div>
                
                <div class="form-group">
                    <label for="password">Contraseña</label>
                    <div class="password-field">
                    <input 
                        :type="showPassword ? 'text' : 'password'" 
                        id="password" 
                        v-model="userData.password" 
                        :disabled="!isEditing" 
                        placeholder="••••••••"
                        class="profile-input"
                    />
                    <button 
                        type="button" 
                        class="toggle-password" 
                        @click="showPassword = !showPassword"
                    >
                        <i :class="showPassword ? 'uil uil-eye-slash' : 'uil uil-eye'"></i>
                    </button>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="bio">Descripción personal</label>
                    <textarea 
                    id="bio" 
                    v-model="userData.bio" 
                    :disabled="!isEditing" 
                    rows="4" 
                    placeholder="Escribe algo sobre ti..."
                    class="profile-textarea"
                    ></textarea>
                </div>
                
                <div class="form-actions">
                    <button 
                    v-if="!isEditing" 
                    type="button" 
                    class="edit-button" 
                    @click="startEditing"
                    >
                    <i class="uil uil-edit"></i> Editar perfil
                    </button>
                    <template v-else>
                    <button type="submit" class="save-button">
                        <i class="uil uil-check"></i> Guardar cambios
                    </button>
                    <button type="button" class="cancel-button" @click="cancelEditing">
                        <i class="uil uil-times"></i> Cancelar
                    </button>
                    </template>
                </div>
                </form>
            </div>
            
            <div class="profile-stats">
                <div class="stat-box">
                <i class="uil uil-eye"></i>
                <div class="stat-info">
                    <h3>{{ stats.peliculasVistas }}</h3>
                    <p>Películas vistas</p>
                </div>
                </div>
                <div class="stat-box">
                <i class="uil uil-heart"></i>
                <div class="stat-info">
                    <h3>{{ stats.favoritas }}</h3>
                    <p>Favoritas</p>
                </div>
                </div>
                <div class="stat-box">
                <i class="uil uil-clock"></i>
                <div class="stat-info">
                    <h3>{{ stats.porVer }}</h3>
                    <p>Por ver</p>
                </div>
                </div>
            </div>
            </div>
        </div>
        </main>
    </div>
</template>

<script>
export default {
    name: 'UserProfile',
    data() {
        return {
        isEditing: false,
        showPassword: true,
        userAvatar: null,
        userData: {
            username: '',
            email: '',
            password: '',
            bio: ''
        },
        originalUserData: {}, // Para restaurar datos si cancela la edición
        stats: {
            peliculasVistas: 0,
            favoritas: 0,
            porVer: 0
        }
        };
    },
    mounted() {
        this.fetchUserData();
        this.fetchUserStats();
        
        // Comprobar si está en modo oscuro
        const isDarkMode = localStorage.getItem('darkMode') === 'true';
        if (isDarkMode) {
        document.body.classList.add('dark-mode');
        }
        
        // Comprobar si la barra lateral debe estar oculta en móvil
        if (window.innerWidth <= 768) {
        document.body.classList.add('sidebar-hidden');
        }
    },
    methods: {
        fetchUserData() {
        // Obtener ID de usuario del localStorage
        /*
        const userId = localStorage.getItem('user_id');
        const token = localStorage.getItem('token');
        if (!userId || !token) {
            this.$router.push('/login');
            return;
        }
        */
        // Simulación de datos - reemplazar con llamada API real
        // .then(response => response.json())
        // .then(data => {
        //   this.userData = data;
        //   this.originalUserData = {...data};
        // });
        
        // Datos simulados mientras tanto
        setTimeout(() => {
            this.userData = {
            username: 'Usuario123',
            email: 'usuario@ejemplo.com',
            password: '••••••••',
            bio: 'Me encanta el cine de ciencia ficción y las películas de aventuras.'
            };
            this.originalUserData = {...this.userData};
        }, 500);
        },
        
        fetchUserStats() {
        // Simulación de estadísticas - reemplazar con llamada API real
        setTimeout(() => {
            this.stats = {
            peliculasVistas: 42,
            favoritas: 15,
            porVer: 8
            };
        }, 500);
        },
        
        startEditing() {
        this.isEditing = true;
        // Guardar datos originales para restaurar si cancela
        this.originalUserData = {...this.userData};
        },
        
        cancelEditing() {
        this.isEditing = false;
        // Restaurar datos originales
        this.userData = {...this.originalUserData};
        },
        
        updateProfile() {
        // Implementar lógica para actualizar perfil
        // fetch('/api/update-profile', {
        //   method: 'POST',
        //   headers: {
        //     'Content-Type': 'application/json',
        //     'Authorization': `Bearer ${localStorage.getItem('token')}`
        //   },
        //   body: JSON.stringify(this.userData)
        // })
        // .then(response => response.json())
        // .then(data => {
        //   if (data.success) {
        //     this.isEditing = false;
        //     this.originalUserData = {...this.userData};
        //     // Mostrar mensaje de éxito
        //   }
        // });
        
        // Simulación de actualización exitosa
        setTimeout(() => {
            this.isEditing = false;
            this.originalUserData = {...this.userData};
            alert('Perfil actualizado con éxito');
        }, 800);
        },
        
        toggleSidebar() {
        document.body.classList.toggle('sidebar-hidden');
        },
        
        closeSidebar() {
        document.body.classList.add('sidebar-hidden');
        },
        
        toggleTheme() {
        document.body.classList.toggle('dark-mode');
        // Guardar preferencia en localStorage
        const isDarkMode = document.body.classList.contains('dark-mode');
        localStorage.setItem('darkMode', isDarkMode);
        },
        
        logout() {
        // Implementar lógica de cierre de sesión
        localStorage.removeItem('token');
        localStorage.removeItem('user_id');
        this.$router.push('/login');
        }
    }
    };
    </script>

    <style scoped>
    /* Importing Google Font - Open Sans */
    @import url("https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&display=swap");

    /* Color variables for light theme */
    :root {
    --white-color: #fff;
    --black-color: #000;
    --light-white-color: #f0f0f0;
    --light-gray-color: #e5e5e5;
    --border-color: #ccc;
    --primary-color: #e10ce9;
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

    .container {
    display: flex;
    overflow: hidden;
    max-height: 100vh;
    flex-direction: column;
    }

    header .sidebar .nav-left {
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

    .main-layout {
    display: flex;
    overflow-y: auto;
    scrollbar-color: #a6a6a6 transparent;
    height: calc(100vh - 57px);
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

    .sidebar .link-section .link-item.active {
    background: var(--primary-color);
    color: white;
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

    /* Estilos específicos para el perfil */
    .profile-container {
    max-width: 800px;
    margin: 20px auto;
    background: var(--white-color);
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    }

    .profile-header {
    display: flex;
    align-items: center;
    padding: 30px;
    background: linear-gradient(to right, var(--primary-color), #8700fd);
    color: white;
    }

    .profile-avatar {
    position: relative;
    margin-right: 20px;
    }

    .avatar-image {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid white;
    }

    .change-avatar-btn {
    position: absolute;
    right: 0;
    bottom: 0;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: var(--primary-color);
    border: 2px solid white;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    }

    .profile-title {
    font-size: 1.8rem;
    font-weight: 600;
    }

    .profile-info {
    padding: 30px;
    }

    .profile-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    }

    .form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
    }

    .form-group label {
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--secondary-color);
    }

    .profile-input, .profile-textarea {
    width: 100%;
    padding: 12px 15px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: var(--white-color);
    color: var(--black-color);
    font-size: 1rem;
    }

    .profile-input:disabled, .profile-textarea:disabled {
    background: var(--light-white-color);
    cursor: not-allowed;
    }

    .password-field {
    position: relative;
    display: flex;
    align-items: center;
    }

    .toggle-password {
    position: absolute;
    right: 15px;
    background: none;
    border: none;
    color: var(--secondary-color);
    cursor: pointer;
    }

    .form-actions {
    display: flex;
    gap: 15px;
    margin-top: 10px;
    }

    .edit-button, .save-button, .cancel-button {
    padding: 10px 20px;
    border-radius: 8px;
    border: none;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    }

    .edit-button {
    background: var(--primary-color);
    color: white;
    }

    .save-button {
    background: #10b981;
    color: white;
    }

    .cancel-button {
    background: var(--light-gray-color);
    color: var(--black-color);
    }

    .profile-stats {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    padding: 20px 30px 30px;
    border-top: 1px solid var(--light-gray-color);
    }

    .stat-box {
    flex: 1;
    min-width: 150px;
    background: var(--light-white-color);
    border-radius: 12px;
    padding: 20px;
    display: flex;
    align-items: center;
    gap: 15px;
    }

    .stat-box i {
    font-size: 2.5rem;
    color: var(--primary-color);
    }

    .stat-info h3 {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--black-color);
    }

    .stat-info p {
    color: var(--secondary-color);
    font-size: 0.9rem;
    }

    /* Screen overlay for mobile */

    body.sidebar-hidden .main-layout .screen-overlay {
    opacity: 0;
    pointer-events: none;
    }


    /* Responsive media code for small devices */
    @media (max-width: 768px) {
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
    
    .profile-header {
        flex-direction: column;
        text-align: center;
    }
    
    .profile-avatar {
        margin-right: 0;
        margin-bottom: 15px;
    }
    
    .profile-stats {
        flex-direction: column;
    }
    
    .stat-box {
        width: 100%;
    }
    
    .form-actions {
        flex-direction: column;
    }
    }
</style>