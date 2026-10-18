# Logic Nudge — Learning Hub

An independent static learning directory. The first published lessons point to verified JavaScript resources.

**Audience:** Students and developers who want to predict, run and understand real code.

## Publishing on GitHub Pages

- This repository must be named exactly `logicnudge.github.io` under the **Logic Nudge organization** (`logicnudge`).
- The repository already exists as **Public**; do not create it again.
- Push these files to its `main` branch using the dedicated publisher identity.
- In repository **Settings → Pages**, set **Deploy from a branch**, **main**, **/(root)** and Save.
- Verify the live address in a signed-out browser before linking it from any social profile.

The intended URL is `https://logicnudge.github.io/` but it is **not live** until the repository and Pages configuration are successfully published.

No backend, account creation, analytics tracking, cookies, external CSS/JS libraries, paid service, or API keys are required.

## Publishing policy

Only list lessons with verified public resource URLs. Future Python and DSA items remain hidden until actually published and checked. Update this file with the `release-ops/tools/build_hub.py` generator rather than hand-editing cards.

To add Python #011–#020 after learner resources are public, use the verified two-manifest `build_hub.py --online` workflow from the release-ops directory described in `START_HERE.md` of the implementation kit. Never publish draft URLs.
