/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,njk,md}",
    "./src/_includes/**/*.{html,js,njk,md}",
    "./src/assets/css/**/*.css"
  ],
  theme: {
    extend: {
      colors: {
        primary: '#007bff',
      },
      typography: {
        DEFAULT: {
          css: {
            'h1, h2, h3, h4': {
              color: '#1a202c',
            },
            ul: {
              'list-style-type': 'disc',
            },
            li: {
              '&::marker': {
                color: '#007bff',
              },
            },
            a: {
              color: '#007bff',
              '&:hover': {
                color: '#0056b3',
              },
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
