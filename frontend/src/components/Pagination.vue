<template>
<div class="pagination justify-content-center">
  <div class="my_pagination">
  <a :disabled="isInFirstPage"
    @click="onClickFirstPage"
    class="pagination-action">
      <i class="fa fa-angle-double-left" aria-hidden="true"></i>
  </a>

  <a :disabled="isInFirstPage"
    @click="onClickPreviousPage"
    class="pagination-action">
      <i class="fa fa-angle-left" aria-hidden="true"></i>
  </a>
  <div v-for="page in pages" :key="page.name">
    <span v-if="isPageActive(page.name)" class="pagination-number pagination-current">{{page.name}}</span>
    <a v-else @click="onClickPage(page.name)" class="pagination-number">{{ page.name }}</a>
  </div>
  <a :disabled="isInLastPage"
    @click="onClickNextPage"
    class="pagination-action">
      <i class="fa fa-angle-right" aria-hidden="true"></i>
  </a>

  <a :disabled="isInLastPage"
    @click="onClickLastPage"
    class="pagination-action">
      <i class="fa fa-angle-double-right" aria-hidden="true"></i>
  </a>
  </div>
  </div>
</template>

<script>
export default {
    props: {
    maxVisibleButtons: {
      type: Number,
      required: false,
      default: 5 
    },
    totalPages: {
      type: Number,
      required: true
    },
    total: {
      type: Number,
    },
    currentPage: {
      type: Number,
      required: true
    }
  },
  computed: {
    startPage() {
      if (this.currentPage === 1) {
        return 1;
      }
      if (this.currentPage === this.totalPages) {
        return this.totalPages - this.maxVisibleButtons+1;
      }
      let startPage = this.currentPage - 2;
      if(startPage <=0) return 1;
      return startPage;
    },
    pages() {
      const range = [];

      for (let i = this.startPage;
        i <= Math.min(this.startPage + this.maxVisibleButtons-1, this.totalPages);
        i+= 1 ) {
        range.push({
          name: i,
          isDisabled: i === this.currentPage
        });
      }
      return range;
    },
    isInFirstPage() {
      return this.currentPage === 1;
    },
    isInLastPage() {
      return this.currentPage === this.totalPages;
    },
  }, 
  methods: {
    isPageActive(page) {
      return this.currentPage === page;
    },
    onClickFirstPage() {
      this.$emit('pagechanged', 1);
    },
    onClickPreviousPage() {
      this.$emit('pagechanged', this.currentPage - 1);
    },
    onClickPage(page) {
      this.$emit('pagechanged', page);
    },
    onClickNextPage() {
      this.$emit('pagechanged', this.currentPage + 1);
    },
    onClickLastPage() {
      this.$emit('pagechanged', this.totalPages);
    }
  }
}
</script>

<style>
  /* .pagination {
  list-style-type: none;
}

  .pagination-item {
    display: inline-block;
  } */

  /* .active {
    background-color: #4AAE9B;
    color: #ffffff;
  } */
</style>