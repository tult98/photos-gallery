<template>
  <div class="photos-list">
    <div class="container-fluid photos">
      <div class="row align-items-stretch">
        <div v-for="photo in photos" :key="photo.id" class="col-6 col-md-6 col-lg-4" data-aos="fade-up">
          <a v-bind:href="photo.url" class="d-block photo-item" data-fancybox="gallery">
            <img v-bind:src="photo.url" alt="Image" class="img-fluid">
            <div class="photo-text-more">
              <span class="icon icon-search"></span>
            </div>
          </a>
        </div>
      </div>    
    </div>
    <Pagination 
    :currentPage="currentPage"
    :totalPages="totalPages"
    @pagechanged="pagechanged"
    >
    </Pagination>
  </div> <!-- end photos-list -->
</template>

<script>
import { RepositoryFactory } from "../repositories/RepositoryFactory"
import Pagination from '../components/Pagination'

const PhotosRepository = RepositoryFactory.get('photos')

export default {
  name: 'PhotosList',
  components: {
    Pagination,
  },
  data() {
    return {
      currentPage: 1,
      photos: null,
      data: null,
      totalImages: null,
      isLoading: false
    };
  },
  created () {
    this.getPhotos(this.currentPage)
  },
  methods: {
    async getPhotos(currentPage) {
      this.isLoading = true;
      const { data } = await PhotosRepository.get(currentPage);
      this.isLoading = false;
      this.data = data;
      this.totalImages = data.count;
      this.photos = data.results;
    },
    pagechanged(e) {
      this.currentPage = e;
      this.getPhotos(e)
    }
  },
  computed: {
    totalPages() {
      return Math.floor(this.totalImages/30) + 1;
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
