<template>
  <div>
    <div class="jumbotron">
      <div class="title-div">
        <h1 class="display-4 Jumbo-heading">Game Study</h1>
        <hr />
        <p class="lead">A project examing game data</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Jumbo",
};
</script>

<style scoped>
.jumbotron {
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url("../../assets/images/game_image.jpg");
  height: 550px;
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.title-div {
  background-color: rgba(0, 0, 0, 0.8);
  width: 40%;
  padding: 40px;
}

.Jumbo-heading {
  color: white;
  text-transform: uppercase;
  text-align: center;
}

hr {
  border-color: white;
}

.lead {
  color: white;
  text-align: center;
  text-transform: capitalize;
}
</style>
	