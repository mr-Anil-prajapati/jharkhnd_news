import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://mr-anil-prajapati.github.io/jharkhnd_news',
  base: '/jharkhnd_news',
  integrations: [tailwind()]
});
