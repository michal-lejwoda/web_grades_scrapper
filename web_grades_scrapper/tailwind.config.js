/** @type {import('tailwindcss').Config} */
export default {
  content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
        width: {
                '700': '700px',
                '500': '500px',
            },
    },
  },
  plugins: [],
}

