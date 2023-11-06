<template>
  <div>
    <form @submit="submitGameName">
      <label for="GameName">Game Name:</label><br />
      <input type="text" id="GameName" name="GameName" v-model="GameName" /><br />
      <input type="submit" value="Submit" />
    </form>
	</div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Main",
  data() {
    return {
      GameName: "",
    };
  },
  methods: {
  ...mapActions("meta", ["submitGameNameToServer"]),
    submitGameName() {
			event.preventDefault();
      const payload = {
        GameName: this.GameName,
			};
			console.log(payload)
      this.submitGameNameToServer({ payload });
    },
  },
};
</script>

<style scoped>
</style>