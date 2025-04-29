<template>
    <div class="body">
        <nav>
            <a href="#"><img src="../assets/pelisScript.png" alt="logo" /></a>
        </nav>

        <div v-if="mostrarLogin" class="form-wrapper">
            <h2>Iniciar Sesión</h2>
            <form @submit.prevent="iniciarSesion">
            <div class="form-control">
                <input type="text" v-model="correo" required />
                <label>Correo</label>
            </div>
            <div class="form-control">
                <input type="password" v-model="contrasena" required />
                <label>Contraseña</label>
            </div>
            <button type="submit">INICIAR SESIÓN</button>
            </form>
            <p>¿Nuevo en PeliScript? <a href="#" @click.prevent="mostrarLogin = false">Regístrate Ahora</a></p>
        </div>

        <div v-else class="form-wrapper">
            <h2>Crear Cuenta</h2>
            <form @submit.prevent="registrarCuenta">
            <div class="form-control">
                <input type="text" v-model="nombre" required />
                <label>Nombre</label>
            </div>
            <div class="form-control">
                <input type="text" v-model="correo" required />
                <label>Correo</label>
            </div>
            <div class="form-control">
                <input type="password" v-model="contrasena" required />
                <label>Contraseña</label>
            </div>
            <button type="submit">REGISTRARTE</button>
            </form>
            <p>¿Ya tienes una cuenta? <a href="#" @click.prevent="mostrarLogin = true">Iniciar Sesión</a></p>
        </div>
    </div>
</template>

<style scoped>
    @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&display=swap");
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Roboto', sans-serif;
    }
    .body {
        background: #000;
    }
    .body::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        opacity: 0.5;
        width: 100%;
        height: 100%;
        background: url("../assets/hero-img.jpg") no-repeat center center/cover;
        background-position: center;
    }
    nav {
        position: fixed;
        padding: 25px 60px;
        z-index: 1;
    }
    nav a img {
        width: 167px;
    }
    .form-wrapper {
        position: absolute;
        left: 50%;
        top: 50%;
        border-radius: 4px;
        padding: 70px;
        width: 450px;
        transform: translate(-50%, -50%);
        background: rgba(0, 0, 0, .75);
    }
    .form-wrapper h2 {
        color: #fff;
        font-size: 2rem;
    }
    .form-wrapper form {
        margin: 25px 0 65px;
    }
    form .form-control {
        height: 50px;
        position: relative;
        margin-bottom: 16px;
    }
    .form-control input {
        height: 100%;
        width: 100%;
        background: #333;
        border: none;
        outline: none;
        border-radius: 4px;
        color: #fff;
        font-size: 1rem;
        padding: 0 20px;
    }
    .form-control input:is(:focus, :valid) {
        background: #444;
        padding: 16px 20px 0;
    }
    .form-control label {
        position: absolute;
        left: 20px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 1rem;
        pointer-events: none;
        color: #8c8c8c;
        transition: all 0.1s ease;
    }
    .form-control input:is(:focus, :valid)~label {
        font-size: 0.75rem;
        transform: translateY(-130%);
    }
    form button {
        width: 100%;
        padding: 16px 0;
        font-size: 1rem;
        background: #e50914;
        color: #fff;
        font-weight: 500;
        border-radius: 4px;
        border: none;
        outline: none;
        margin: 25px 0 10px;
        cursor: pointer;
        transition: 0.1s ease;
    }
    form button:hover {
        background: #c40812;
    }
    .form-wrapper a {
        text-decoration: none;
    }
    .form-wrapper a:hover {
        text-decoration: underline;
    }
    .form-wrapper :where(label, p, small, a) {
        color: #b3b3b3;
    }
    .form-wrapper p a {
        color: #fff;
    }
    .form-wrapper small {
        display: block;
        margin-top: 15px;
        color: #b3b3b3;
    }
    .form-wrapper small a {
        color: #0071eb;
    }
    @media (max-width: 740px) {
        body::before {
            display: none;
        }
        nav, .form-wrapper {
            padding: 20px;
        }
        nav a img {
            width: 140px;
        }
        .form-wrapper {
            width: 100%;
            top: 43%;
        }
        .form-wrapper form {
            margin: 25px 0 40px;
        }
    }
</style>

<script>
    export default {
        data() {
        return {
            mostrarLogin: true,
            nombre: "",
            correo: "",
            contrasena: ""
        };
        },  
        methods: {
            async iniciarSesion() {
                try {
                    const res = await fetch("http://localhost:5000/login", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            email: this.correo,
                            password: this.contrasena
                        })
                    });
                    const data = await res.json();
                    if (res.ok) {
                        this.$router.push("/catalogo");
                    } 
                    else {
                        alert(data.message || "Correo o contraseña incorrectos.");
                    }
                }
                catch (error) {
                    console.error("Error al iniciar sesión:", error);
                    alert("Error de conexión con el servidor.");
                }
            },
            async registrarCuenta() {
                try {
                    const res = await fetch("http://localhost:5000/register", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            username: this.nombre,
                            email: this.correo,
                            password: this.contrasena
                        })
                    });
                    const data = await res.json();
                    if (res.ok) {
                        this.$router.push("/catalogo");
                    } 
                    else {
                        alert(data.message || "No se pudo registrar.");
                    }
                } 
                catch (error) {
                    console.error("Error al registrar:", error);
                    alert("Error de conexión con el servidor.");
                }
            }
        }
    };
</script>