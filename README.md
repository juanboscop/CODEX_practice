# Interactive Historical Earth

This project aims to visualize Earth's history on an interactive 3‑D globe. Built with React, Three.js, and Zustand, it provides a foundation for exploring geologic and cultural events over time.

## Getting Started

```bash
pnpm install
pnpm --filter client dev
```

This installs all workspace dependencies and starts the Vite dev server at [http://localhost:5173](http://localhost:5173).

## Scripts

- `pnpm lint` – run ESLint across the workspace
- `pnpm format` – check code formatting with Prettier
- `pnpm --filter client test` – run Vitest tests
- `pnpm --filter client build` – create a production build

CI runs lint, test, and build on every push via GitHub Actions.
