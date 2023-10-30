<template>
  <div>
    <div class="jumbotron">
      <h1 class="display-4 Jumbo-heading">Game Study</h1>
      <p class="lead">
        This is a simple hero unit, a simple jumbotron-style component for
        calling extra attention to featured content or information.
      </p>
      <hr class="my-4" />
      <p>
        It uses utility classes for typography and spacing to space content out
        within the larger container.
      </p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "HomeView",
  // components: {
  //   HelloWorld
  // }
};
</script>

<style scoped>
.jumbotron {
  background-image: url("../assets/images/game_image.jpg");
  height: 550px;
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.Jumbo-heading {
  color: white;
  text-transform: uppercase;
}
</style>
