<template>
<div>
	<p>Critic Data</p>
</div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "CriticData",
  computed: {
    ...mapGetters("meta", ["NoData"]),
  },
};

</script>

<style scoped>

</style>