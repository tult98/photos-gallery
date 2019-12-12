<template>
  <div id="app">
    <div class="site-wrap">
      <Header/>
      <main class="main-content">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue';

export default {
  name: 'app',
  components: {
    Header,
  },
}
</script>

<style>

</style>
