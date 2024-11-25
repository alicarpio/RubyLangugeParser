<script setup lang="ts">
import TextAreaEO from "./components/TextAreaEO.vue";
import NavBar from "./components/NavBar.vue";
</script>

<template>
  <NavBar/>
  <div class="flex space-x-4 mt-10 mx-4">
    <div class="w-1/2 bg-gray-200 p-4">
      <p>Contenido del Div 1</p>
      </div>

    <div class="w-1/2 p-4">
      <TextAreaEO message="EDITOR"/>
      <div class="flex justify-between mb-10">
        <button type="button" class="text-white mt-3 custom-bg-copy hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded text-sm px-5 py-2 text-center me-2">Copy</button>
        <button type="button" class="text-white mt-3 w-32 custom-bg-run hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded text-sm px-5 py-2 text-center">Run</button>
      </div>

      <TextAreaEO message="OUTPUT" output="true" />
    </div>
  </div>

</template>

<style scoped>
.custom-bg-run {
  background-color: #EE0B10;
}

.custom-bg-copy {
  background-color: #FF8C00;
}

</style>
