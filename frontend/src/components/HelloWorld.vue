<template>
  <div class="hello">
    <div class="site-wrap">
    <main class="main-content">
      <div class="container-fluid photos">
        <div class="row align-items-stretch">
          <div v-for="photo in photos" v-bind:key="photo" class="col-6 col-md-6 col-lg-4" data-aos="fade-up">
            <a v-bind:href="photo.url" class="d-block photo-item" data-fancybox="gallery">
              <img v-bind:src="photo.url" alt="Image" class="img-fluid">
              <div class="photo-text-more">
                <span class="icon icon-search"></span>
              </div>
            </a>
          </div>
        </div>    
      </div>
    </main>

  </div> <!-- .site-wrap -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      photos: null,
    };
  },
  created: function() {
    axios
      .get("http://127.0.0.1:8000/api/v1/photos/")
      .then(res => {
        this.photos = res.data;
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
