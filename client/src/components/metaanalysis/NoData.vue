<template>
<div>
	<section>
		<div>
			<h3 class='center'>Currently No Data</h3>
			<p class='center'>Please Enter a Game Title Above</p>
		</div>
		<div class='pic-section'>
			<div class='pic-one'></div>
			<div class='pic-two'></div>
		</div>
	</section>
</div>
</template>

<script>
export default {
  name: "NoData",
};
</script>

<style scope>
section {
  height: 600px;
}

.pic-section {
	display: flex; 
	flex-direction: row;
}

.pic-one {
	background-image: url("../../assets/images/image_one.jpg");
  height: 400px;
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
	margin: 30px;
}

.pic-two {
	background-image: url("../../assets/images/image_two.jpg");
  height: 400px;
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
	margin: 30px;
}
</style>