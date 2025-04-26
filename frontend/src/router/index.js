import { createRouter, createWebHistory } from 'vue-router'
import LoginPelis from '@/components/LoginPelis.vue'
import CatalogoPro from '@/components/CatalogoPro.vue'

const routes = [
    {
        path: '/login',
        component: LoginPelis
    },
    {
        path: '/catalogo',
        component: CatalogoPro
    },
    {
        path: '/',
        redirect: '/login'
    }
]

const router = createRouter({
history: createWebHistory(),
routes
})

export default router
