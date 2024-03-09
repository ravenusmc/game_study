<template>
  <div>
    <section>
      <div class="form-area">
        <div class="form-input-area">
          <h2 class="center signup-title title-size font">Login</h2>
          <h3 v-if="userNotFound" class="center login-problem">
            User is not found.
            <br>
            <a><router-link class="alert" to="/sign_up"
                >sign up.</router-link
              ></a
            >
          </h3>
          <h1 v-if="passwordNoMatch" class="center login-problem alert">
            Password is Invalid
          </h1>
          <form @submit="login">
            <div class="field">
              <label class='email-input' for="email">email:</label>
              <input
                class="input is-primary is-rounded"
                type="email"
                v-model="email"
                placeholder="email"
              />
            </div>
            <div class="field">
              <label for="password"
                >Password:</label
              >
              <input
                class="input is-primary is-rounded"
                type="password"
                v-model="password"
                placeholder="Password"
              />
            </div>
            <div class="button-div">
              <button class="btn btn-primary form-submit-btn">Login</button>
            </div>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Form",
  computed: {
    ...mapGetters("common", ["userNotFound", "passwordNoMatch"]),
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    ...mapActions("common", ["loginUser"]),
    login(evt) {
      evt.preventDefault();
      const payload = {
        email: this.email,
        password: this.password,
      };
      this.loginUser({ payload });
    },
  },
};
</script>

<style scoped>
section {
  height: 75vh;
  margin: 3%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.signup-title {
  text-transform: uppercase;
  font-weight: bold;
}
.login-problem {
  font-size: 15px;
}
.form-area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form-input-area {
  background-color: rgba(45, 165, 229, 0.7);
  padding: 15px;
  border-radius: 15px;
  width: 350px;
}

.button-div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
}

.email-input {
  margin-right:30px;
}

.field {
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
}

.label {
  width: 100px; /* Adjust the width as needed */
}

.input {
  width: 300px; /* Adjust the width as needed */
}

@media only all and (max-width: 900px) {
  section {
    margin-top: -100px;
  }
}
</style>