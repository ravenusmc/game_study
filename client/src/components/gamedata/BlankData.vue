<template>
  <div>
    <section>
      <div>
        <h3 class="center">Currently No Data</h3>
        <p>Please Select a Year and Genre Above</p>
      </div>
    </section>
    <div class="pic-section">
      <div class="pic-one"></div>
      <div class="pic-two"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NoData",
};
</script>

<style scoped>
section {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}

h3 {
  text-transform: uppercase;
}

.pic-section {
  display: flex;
  flex-direction: row;
}

.pic-one {
  background-image: url("../../assets/images/gamer_girl.jpg");
  height: 400px;
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  margin: 30px;
}

.pic-two {
  background-image: url("../../assets/images/street_fighter.jpg");
  height: 400px;
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  margin: 30px;
}
</style>