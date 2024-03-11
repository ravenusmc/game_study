<template>
  <div>
    <section>
      <div class='image-div'></div>
      <div class='paragraph-div'>
				<h2 class='paragraph-heading center'>Purpose</h2>
				<p>
					Now, this is the third time, maybe the fourth, that I've done a project like this. Why come back to it?
					Well, I really like games. I've also spent the last few months working on learning pygame. Even though I 
					enjoyed doing that I thought that I'd stick with web development. I also like the idea of this project 
					because it can allow one to get into some basic statistics. 
				</p>

				<p>
					I also had a big urge to review some game ratings scores. I've always been interested in the IGN score for
					the game Alien Isolation. They gave it like a 5.9 which really turned a lot of people off to not buy it. 
					This is what happened to me. Then I decided to go out and play it and found that I really enjoyed it. Currently,
					on Metacritic, the metascore is 79 and the user score is an 8.4. This game shows a lot about what scores can do 
					and also a great way to understand the statistics of the range of scores. 
				</p>

				<p>
					So, I return, once again, to this study. We'll see how the project goes as I work on it. 
				</p>
				<p>
				<div>
					<p>
						<router-link class="alert" to="/login">Login</router-link>
					</p>
				</div>
				</p>
			</div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin: 50px;
}

.image-div {
  background-image: url("../../assets/images/mario.jpg");
  height: 500px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  border-radius: 12px;
}

.paragraph-div {
  margin: 0 30px 0 30px;
}

.paragraph-heading {
  text-transform: uppercase;
}
</style>