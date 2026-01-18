import { defineConfig } from "vite";
import { tanstackStart } from "@tanstack/react-start/plugin/vite";
import viteReact from "@vitejs/plugin-react";
import viteTsConfigPaths from "vite-tsconfig-paths";
import tailwindcss from "@tailwindcss/vite";
import mdx from "fumadocs-mdx/vite";
import * as sourceConfig from "./source.config";

export default defineConfig({
  plugins: [
    tailwindcss(),
    mdx(sourceConfig),
    tanstackStart(),
    viteReact(),
    viteTsConfigPaths({
      projects: ["./tsconfig.json"],
    }),
  ],
});
