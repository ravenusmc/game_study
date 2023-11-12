<template>
  <div>
    <div class='title-div'>
      <h1 class='center change-text'>MetaCritic Game Analysis</h1>
    </div>
		<Form />
    <hr>
    <BasicGameAnalysis />
	</div>
</template>

<script>
import Form from "@/components/metaanalysis/Form.vue";
import BasicGameAnalysis from "@/components/metaanalysis/BasicGameAnalysis.vue";

export default {
  name: "Analysis",
  components: {
    Form,
    BasicGameAnalysis,
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