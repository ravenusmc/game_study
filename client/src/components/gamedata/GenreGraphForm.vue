<template>
  <div>
    <form class="contact-form">
      <input
        type="checkbox"
        id="Role-Playing"
        value="Role-Playing"
        v-model="selectedGenres"
      />
      <label for="Role-Playing">Role-Playing</label>
      <input
        type="checkbox"
        id="Action"
        value="Action"
        v-model="selectedGenres"
      />
      <label for="Action">Action</label>
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
      //   "Role-Playing",
      //   "Action",
      //   "Racing",
      //   "Misc",
      //   "Adventure",
      //   "Simulation",
      //   "Sports",
      //   "Shooter",
      //   "Puzzle",
      //   "Platform",
      //   "Strategy",
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