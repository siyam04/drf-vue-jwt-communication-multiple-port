/*System Importing*/
import Vue from 'vue'
import VueRouter from 'vue-router'

/*Custom Components Importing*/
import User from "../components/pages/User";
import Players from "../components/pages/Players";



/*Inserting VueRouter to the Vue Framework*/
Vue.use(VueRouter);

/*Array of Paths*/
const routes = [

    {path: '/', component: User, name: 'User'},
    {path: '/players', component: Players, name: 'Players'},
    // {path: '/posts/:id', component: Posts, name: 'Posts'},

];

/*Exporting Array of Paths*/
export const router = new VueRouter({
    // mode: 'history', //hides hash in url after localhost:8080
    routes: routes
});


