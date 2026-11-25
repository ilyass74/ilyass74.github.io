# Ilyass Chakir — Engineering Portfolio

Public portfolio: https://ilyass74.github.io/

ANSUF leads the collection as an independent entrepreneurial tourism technology
project for Morocco. The portfolio includes detailed studies for all 13 original
projects, implementation references, scoped results and a downloadable CV.

## Edit and build

Requires Node.js 20+ and Python 3.10+. No dependency installation is needed.

```sh
npm run build
python scripts/verify-content.py
npm run preview
```

The preview runs at http://127.0.0.1:4173 (override with PORT).

- `content/projects.json`: technical studies and evidence links.
- `src/editorial.py`: homepage and entrepreneurial product composition.
- `scripts/build.py`: static page generation.
- `src/style.css` and `src/interactions.js`: responsive design and interactions.
- `public/`: portfolio media and the current owner-supplied PDF CV.
- `docs/`: complete generated website; GitHub Pages publishes `main` → `/docs`.
- `.site/public.json`: public origin used for canonical and sharing metadata.

After editing, rebuild, verify and commit the updated source and docs directory.
`.nojekyll` preserves the generated files. All project narratives are readable
without JavaScript; filtering and diagram exploration are progressive enhancements.

## Content and privacy

This repository contains an explicitly allowlisted portfolio and its public assets.
It does not include research clones, private ANSUF code, candidate datasets, internal
reports, credentials or client records. ANSUF's stage remains private preview; this
website's publication does not activate the ANSUF product. Historical experimental
results retain their test scope. The CV is copied unchanged from the owner's file.

Website content and original diagrams: Ilyass Chakir. Existing project screenshots
and experiment plots retain their original project context. No new blanket license
is implied for third-party material.
