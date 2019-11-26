<template>
  <div class="hello">
    <ul>
      <li v-for="post in posts" v-bind:key="post">
        <img v-bind:src="post.url" alt="">
      </li>
    </ul>
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
      posts: null,
    };
  },
  created: function() {
    axios
      .get("http://127.0.0.1:8000/api/v1/photos/")
      .then(res => {
        this.posts = res.data;
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
