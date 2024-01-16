<template>
  <div>
    <form class="contact-form">
      <div class="form-group">
        <label for="party">Select Year:</label>
        <select v-model="selectedYear">
          <option disabled value="">Please select one</option>
          <option v-for="year in years" :key="year" :value="year">
            {{ year }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="genres">Select Genre:</label>
        <select v-model="selectedGenre">
          <option disabled value="">Please select one</option>
          <option v-for="genre in genres" :key="genre" :value="genre">
            {{ genre }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <button type="button" class="btn btn-primary" @click="submitSelectedOptions">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "AnalysisForm",
  data() {
    return {
      years: [
        1985,
        1988,
        1992,
        1994,
        1996,
        1997,
        1998,
        1999,
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
      ],
      selectedYear: 1985,
      genres: [
        "Role-Playing",
        "Action",
        "Racing",
        "Misc",
        "Adventure",
        "Simulation",
        "Sports",
        "Shooter",
        "Puzzle",
        "Platform",
        "Strategy",
        "Fighting",
      ],
      selectedGenre: "Role-Playing",
    };
  },
  methods: {
    ...mapActions("csv", ["submitSelectionToServer"]),
    submitSelectedOptions() {
      event.preventDefault();
      const payload = {
        year: this.selectedYear,
        genre: this.selectedGenre,
      };
      this.submitSelectionToServer({ payload });
    },
  },
};
</script>

<style scoped>
.form-group {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>