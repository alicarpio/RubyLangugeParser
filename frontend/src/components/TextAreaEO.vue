<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
    modelValue: {
    type: String,
    required: false,
    default: '',
  },
  output: {
    type: Boolean,
    required: false
},
  message:{
    type: String,
    required: true
  }

});

</script>

<template>
  <label for="message"
         class="font-mono block mb-2 text-sm font-medium text-gray-600">{{message}}</label>
  <textarea id="message"
            rows="6"
            :class="{'custom-bg-output border-gray-500 rounded-lg border p-2.5 w-full text-sm': output, 'block p-2.5 w-full text-sm text-gray-900 bg-white rounded-lg border border-red-400 focus:ring-red-500 focus:border-red-500 ': !output}"
            :disabled="output"
            @input="$emit('update:modelValue', $event.target.value)"
            placeholder="Write your thoughts here..."></textarea>
</template>

<style scoped>
.custom-bg-output {
  background-color: #FEE4C4;
}
</style>