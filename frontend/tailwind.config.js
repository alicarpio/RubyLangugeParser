/** @type {import('tailwindcss').Config} */
export default {
  content: [
      "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        peach: "#FFE8CD",
      },
      fontFamily: {
        cursive: ['Just Me Again Down Here', 'cursive'],
        mono: ['Inconsolata', 'monospace'],
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

