<template>
    <div class="header">
        <div class="site-mobile-menu">
            <div class="site-mobile-menu-header">
            <div class="site-mobile-menu-close mt-3">
                <span class="icon-close2 js-menu-toggle"></span>
            </div>
            </div>
            <div class="site-mobile-menu-body"></div>
        </div>
        <header class="header-bar d-flex d-lg-flex align-items-center inner-page-header" data-aos="fade-down">
            <div class="site-logo">
            <router-link to='/'>Photos Gallery</router-link>
            </div>
            
            <div class="d-inline-block d-xl-block ml-md-0 ml-auto py-3" style="position: relative; top: 3px;"><a href="#" class="site-menu-toggle js-menu-toggle text-white"><span class="icon-upload h3"></span> <span style="position: relative;top: -4px; text-transform: uppercase;">Upload</span></a></div>
            <div class="d-inline-block d-xl-block ml-md-0 ml-auto py-3" style="position: relative; top: 3px;"><a href="#" class="site-menu-toggle js-menu-toggle text-white"><span class="icon-menu h3"></span> <span style="position: relative;top: -4px; text-transform: uppercase;">Menu</span></a></div>

            <div class="main-menu d-none">
            <ul class="js-clone-nav">
                <li><router-link to='/'>Home</router-link></li>
                <li><router-link to='/photos'>Photos</router-link></li>
                <li><router-link to='/about'>About Me</router-link></li>
                <li class="active"><a href="contact.html">Contact</a></li>
            </ul>
            <ul class="social js-clone-nav">
                <li><a href="https://www.facebook.com/le.thanhtu.129"><span class="icon-facebook"></span></a></li>
                <li><a href="https://twitter.com/tult_98"><span class="icon-twitter"></span></a></li>
                <li><a href="https://www.instagram.com/tult_98/"><span class="icon-instagram"></span></a></li>
            </ul>
            </div>
        </header> 
    </div>
</template>

<script>
    export default {
        name: "Header",
    }
</script>

<style scoped>
.header-bar {
    overflow: hidden;
}
</style>