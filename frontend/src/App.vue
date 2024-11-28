<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import TextAreaEO from "./components/TextAreaEO.vue";
import NavBar from "./components/NavBar.vue";

const rubyCode = ref('')
const outputText = ref('')
const errorList = ref<string[]>([])

const analyzeRubyCode = async () => {
  try {
    const response = await axios.post('http://localhost:5000/analizar-ruby', {
      codigo: rubyCode.value
    })

    if (response.data.status === 'success') {
      outputText.value = 'Código Ruby analizado correctamente 🟢'
      errorList.value = []
    }
  } catch (error: any) {
    if (error.response && error.response.data) {
      errorList.value = error.response.data.errores || ['Error desconocido']
      outputText.value = errorList.value.join('\n')
    } else {
      outputText.value = 'Error de conexión con la API'
    }
  }
}

const copyCode = () => {
  navigator.clipboard.writeText(rubyCode.value)
}
</script>

<template>
  <div class="custom-bg-full h-screen">
  <NavBar/>
  <div class="flex space-x-4 mt-10 mx-4">
    <div class="w-1/2 flex flex-col">
     <h1 class="text-2xl text-red-600">What is Ruby?</h1>
      <p>Ruby is an interpreted object-oriented programming language often used for web development. It also offers many scripting features to process plain text and serialized files, or manage system tasks. It is simple, straightforward, and extensible.</p>
    <img src="../src/assets/rubyy.png" class="h-72 mt-14">
    </div>

    <div class="w-1/2 p-4">
      <TextAreaEO
        v-model="rubyCode"
        message="EDITOR"
      />
      <div class="flex justify-between mb-10">
        <button
          @click="copyCode"
          type="button"
          class="text-white mt-3 custom-bg-copy hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded text-sm px-5 py-2 text-center me-2"
        >
          Copy
        </button>
        <button
          @click="analyzeRubyCode"
          type="button"
          class="text-white mt-3 w-32 custom-bg-run hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded text-sm px-5 py-2 text-center"
        >
          Analyze
        </button>

      </div>
      <p class="font-mono block mb-2 text-sm font-medium text-gray-600">OUTPUT</p>
      <div class="custom-bg-output p-4 h-36 rounded-xl">
      <h2 class="font-bold mb-2">Errores detectados:</h2>
      <div v-if="errorList.length" class="text-red-600">
        <p v-for="(error, index) in errorList" :key="index">
          {{ error }}
        </p>
      </div>
      <p v-else class="text-green-600">No se encontraron errores</p>
    </div>
    </div>
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

.custom-bg-output {
  background-color: #FFDAAD;
}

.custom-bg-full {
  background-color: #FFEAD1;
}
</style>