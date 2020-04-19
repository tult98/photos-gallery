import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home';
import PhotosList from './views/PhotosList';
import About from './views/About';
import Upload from './views/Upload';
import NotFound from './components/NotFound';

Vue.use(Router)

export default new Router({
    mode: "history",
    routes: [
        {
            path: '/',
            name: 'home', 
            component: Home
        }, 
        {
            path: '/photos',
            name: 'photos', 
            component: PhotosList,
        }, 
        {
            path: '/about',
            name: 'about',
            component: About
        },
        {
            path: '/upload', 
            name: 'upload', 
            component: Upload
        },
        {
            path: '*', 
            name: 'NotFound',
            component: NotFound
        }
    ]
})

