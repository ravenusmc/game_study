<template>
  <div>
    <form @submit="submitGameName">
      <label for="GameName">Game Name:</label><br />
      <input type="text" id="GameName" name="GameName" v-model="GameName" />
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
      this.submitGameNameToServer({ payload });
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 50px 0 50px 0;
}

label {
  margin-right: 5px;
}

input {
  margin-right: 5px;
}

</style>