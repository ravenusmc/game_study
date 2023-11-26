<template>
<div>
	<p>User Data</p>
</div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserData",
  computed: {
    ...mapGetters("meta", ["NoData"]),
  },
};

</script>

<style scoped>

</style>