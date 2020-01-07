<template>
    <div class="col-full">
        <h1>Not Found</h1>
        <p>Ooops, We couldn't find what you are looking for. Why you dont go
            <router-link :to="{name: 'home'}">
                Home
            </router-link> instead?
        </p>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    h1 {
        font-size: 100px;
    }
    p {
        font-size: 50px;
        font-weight: 100;
    }
    div {
        text-align: center;
    }
</style>