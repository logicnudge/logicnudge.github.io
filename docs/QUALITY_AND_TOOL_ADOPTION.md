# Logic Nudge: minimal-dependency quality gates

This site is static HTML/CSS/JavaScript published via GitHub Pages. Preserve that architecture unless an approved feature justifies changing it.

## Adopted workflow
- Test-first source checks (inspired by Agent Skills / Superpowers).
- Review design against the existing Logic Nudge brand and real-device usability, inspired by Impeccable and Taste Skill.
- Run source tests and actual-page static checks on PRs and main pushes.
- Never insert a library just because it is popular; pilot separately and document the licence and size cost.

## Run locally
```sh
python -m unittest discover -s tests -v
python scripts/site_audit.py index.html
```

The audit checks document language, exactly one h1, title, description, canonical, duplicate IDs, missing image alt attributes, and broken same-page fragments. Source checks **cannot** detect CSS visual clipping, mobile accessibility, WCAG contrast, runtime JavaScript failures, external URL 404s, or real device problems. Those remain manual/browser QA requirements.

## Future tool trials
- **Video only:** benchmark GSAP, Bang Motion, Remotion/HyperFrames against an identical, approved 30fps LN scene; no runtime website dependency.
- **Audio only:** trial Earshot against an actual encoded MP4 and compare results with FFmpeg loudness measurement.
- **Editorial:** test Harper on English copy; human review required for Romanized Hindi.
- **Security:** scan any downloaded agent skill (for example SkillSpector), inspect installation scripts, pin source revisions.

Do not add unverified #031+ episode links to the public directory. Publication records must contain real URLs.
