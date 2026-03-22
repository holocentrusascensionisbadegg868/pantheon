/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        pantheon: {
          bg: '#0a0a0f',
          card: '#12121a',
          border: '#1e1e2e',
          accent: '#c9a84c',
          accentDim: '#8a6d2b',
          text: '#e4e4e7',
          muted: '#71717a',
          gem: '#c9a84c',
          practitioner: '#6ee7b7',
          event: '#93c5fd',
        },
      },
    },
  },
  plugins: [],
};
