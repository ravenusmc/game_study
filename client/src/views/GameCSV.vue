<template>
  <div>
    <section>
      <div class="title-div">
        <h2 class="center">Game Data Analysis</h2>
      </div>

      <form class="contact-form">
        <div class="selector-fix">
          <label for="party">Select Year:</label>
          <select v-model="selectedYear">
            <option disabled value="">Please select one</option>
            <option v-for="year in years" :key="year" :value="year">
              {{ year }}
            </option>
          </select>
        </div>
        <div class="selector-fix">
          <label for="genres">Select Genre:</label>
          <select v-model="selectedGenre">
            <option disabled value="">Please select one</option>
            <option v-for="genre in genres" :key="genre" :value="genre">
              {{ genre }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <button
            type="button"
            class="btn btn-primary"
            @click="submitSelectedOptions"
          >
            Submit
          </button>
        </div>
      </form>

      <div class="no-info-section">
        <div>
          <h3 class="center">Currently No Data</h3>
          <p class="center">Please Select a Year and Genre Above</p>
        </div>
      </div>

      <div>
        <h1>test</h1>
        <!-- <div class="pic-one"></div>
        <div class="pic-two"></div> -->
      </div>

    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
// import GameDataForm from "@/components/gamedata/GameDataForm.vue";
// import BlankData from "@/components/gamedata/BlankData.vue";
// import Results from "@/components/gamedata/Results.vue";

export default {
  name: "GameCSV",
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
  computed: {
    ...mapGetters("csv", ["dataReceived"]),
  },
};
</script>

<style scoped>
.title-div {
  margin-top: 50px;
  text-transform: uppercase;
}

.contact-form {
  display: flex;
  justify-content: center;
  align-items: center;
}

.selector-fix {
  margin-right: 10px;
}

.no-info-section {
  margin-top: 30px;
}

/* CSS On pic section */
.pic-section-csv {
  display: flex;
  flex-direction: row;
}

.pic-one {
  background-image: url("../assets/images/gamer_girl.jpg");
  /* height: 400px; */
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  margin: 30px;
}

.pic-two {
  background-image: url("../assets/images/street_fighter.jpg");
  /* height: 400px; */
  width: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  margin: 30px;
}
</style>