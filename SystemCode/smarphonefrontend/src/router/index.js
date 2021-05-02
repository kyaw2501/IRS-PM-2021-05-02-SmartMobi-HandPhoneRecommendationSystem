import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
//import Zh from "@/views/Zh";
//import Zh2 from "@/views/Zh2";
import En from "@/views/En";
//import En2 from "@/views/En2";
//import Output from "@/components/Output";
import OutputEn from "@/components/OutputEn";
// import HelloWorld from "@/components/HelloWorld";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            title: 'Smart Phone Recommender',
        },
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
        meta: {
            title: 'About'
        }
    },

    {
        path: '/en-1',
        name: 'QuestionnaireEn',
        component: En,
        meta: {
            title: 'Smartphone Recommender',
        }
    },

    {
        path: '/output-en',
        name: 'OutputEn',
        component: OutputEn,
        meta: {
            title: 'Result'
        },
    },

]


const router = new VueRouter({
    routes,
})

router.beforeEach((to, from, next) => {
    /* 路由发生变化修改页面title */
    if (to.meta.title) {
        document.title = to.meta.title
    }
    next()
})

export default router
