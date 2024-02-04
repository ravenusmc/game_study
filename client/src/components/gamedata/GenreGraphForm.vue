<template>
  <div>
    <form>
      <h4>Please Select Genre(s):</h4>
      <div class="genre-selection-area">
        <div>
          <input
            type="checkbox"
            id="Role-Playing"
            value="Role-Playing"
            v-model="selectedGenres"
          />
          <label for="Role-Playing">Role-Playing</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Action"
            value="Action"
            v-model="selectedGenres"
          />
          <label for="Action">Action</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Racing"
            value="Racing"
            v-model="selectedGenres"
          />
          <label for="Racing">Racing</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Misc"
            value="Misc"
            v-model="selectedGenres"
          />
          <label for="Misc">Misc</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Adventure"
            value="Adventure"
            v-model="selectedGenres"
          />
          <label for="Adventure">Adventure</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Sports"
            value="Sports"
            v-model="selectedGenres"
          />
          <label for="Sports">Sports</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Simulation"
            value="Simulation"
            v-model="selectedGenres"
          />
          <label for="Simulation">Simulation</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Shooter"
            value="Shooter"
            v-model="selectedGenres"
          />
          <label for="Shooter">Shooter</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Puzzle"
            value="Puzzle"
            v-model="selectedGenres"
          />
          <label for="Puzzle">Puzzle</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Platform"
            value="Platform"
            v-model="selectedGenres"
          />
          <label for="Platform">Platform</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Strategy"
            value="Strategy"
            v-model="selectedGenres"
          />
          <label for="Strategy">Strategy</label>
        </div>
        <div>
          <input
            type="checkbox"
            id="Fighting"
            value="Fighting"
            v-model="selectedGenres"
          />
          <label for="Fighting">Fighting</label>
        </div>
      </div>
      <div class="form-group">
        <button
          type="button"
          class="btn btn-primary"
          @click="submitSelectedGenres"
        >
          Submit
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "GenreGraphForm",
  data() {
    return {
      selectedGenres: [],
      // genres: [
      //   "Fighting",
      // ],
    };
  },
  methods: {
    // ...mapActions("csv", ["submitSelectionToServer"]),
    submitSelectedGenres() {
      event.preventDefault();
      console.log(this.selectedGenres);
      // const payload = {
      //   year: this.selectedYear,
      //   genre: this.selectedGenre,
      // };
      // this.submitSelectionToServer({ payload });
    },
  },
};
</script>

<style scoped>
form {
  display: grid;
  align-items: center;
  justify-content: center;
}

.genre-selection-area {
	display: grid;
	grid-template-columns: 1fr 1fr 1fr 1fr;
}
</style>