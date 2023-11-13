<template>
  <div>
    <div class='title-div'>
      <h1 class='center change-text'>MetaCritic Game Analysis</h1>
    </div>
		<Form />
    <hr>
    <NoData v-if="NoData" />
    <BasicGameAnalysis v-if="!NoData" />
	</div>
</template>

<script>
import { mapGetters } from "vuex";

import Form from "@/components/metaanalysis/Form.vue";
import NoData from "@/components/metaanalysis/NoData.vue";
import BasicGameAnalysis from "@/components/metaanalysis/BasicGameAnalysis.vue";

export default {
  name: "Analysis",
  components: {
    Form,
    NoData,
    BasicGameAnalysis,
  },
  computed: {
    ...mapGetters("meta", ["NoData"]),
  },
};
</script>

<style scope
    BasicGameAnalysisd>
.title-div {
  margin-top: 50px;
}

.change-text {
  text-transform: uppercase;
}

hr {
  border-top: 1px dashed black;
}

</style>