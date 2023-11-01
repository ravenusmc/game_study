<template>
  <div>
    <Jumbo/>
    <Center/>
  </div>
</template>

<script>
// @ is an alias to /src
import Jumbo from '@/components/home/Jumbo.vue'
import Center from '@/components/home/Center.vue'

export default {
  name: "HomeView",
  components: {
    Jumbo,
    Center,
  }
};
</script>

<style scoped>

</style>
