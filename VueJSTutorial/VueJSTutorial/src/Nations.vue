<template>
  <ul>
    <li v-for="nation in nations">{{ nation }}</li>
  </ul>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      nations: ['Fiore', 'Limeiro', 'Nirn']
    }
  },
  methods: {

  }
}
</script>

<style>

</style>
