# Atlas Launch Day Checklist

> **Status (2026-06-02, Atlas team)**: Launch-copy refreshed to current ground truth
> (PyPI v0.3.0 live, repo = nxtg-atlas, 2,979 tests, atlas-action@v1 install funnel proven —
> B+ 86% dogfood on PR #8). Copy is **queued for Asif** — the actual HN/Reddit/X/PH posts are
> Asif's one-click (speaking as us to third parties; agent-hands-boundary). Atlas team does NOT post.
>
> **ONE ASIF DECISION before launch**: messaging is now **open-core** ("free CLI; Pro tier on
> roadmap") not "free forever, no tiers", because N-09 Pro Tier is DECIDED and the CLI already
> ships `license`/`activate`. Confirm open-core framing, or say "free forever" and we'll retire N-09.

## Pre-Launch (day before)

- [x] PyPI published and `pip install nxtg-atlas` works (N-06) — **v0.3.0 live, verified 2026-06-02**
- [ ] **Cut v0.3.1 before launch** — includes the `--json` width-wrap fix (commit e8b2498). PyPI v0.3.0 currently ships invalid-JSON-in-narrow-terminal for `compare/search/top --json`; the launch audience pipes `--json | jq`, so publish the patch so `pip install` serves the fix.
- [x] Capture rendered sticky PR comment as a launch-bundle screenshot — **launch/assets/atlas-action-pr-comment-proof.png**
- [ ] README GIF renders correctly on GitHub (N-07)
- [x] `atlas --help` shows clean output — verified, 25 commands
- [x] `atlas init && atlas add . && atlas scan && atlas status` works end-to-end — commands verified present
- [x] GitHub Action consumable cross-repo (`uses: nxtg-ai/atlas-action@v1`) — **proven, PR #8 merged**
- [ ] GitHub repo description and topics set
- [ ] GitHub social preview image uploaded (terminal screenshot)
- [ ] Asif: publish atlas-action to GitHub Marketplace (one-click on v0.1.2 release page)
- [ ] Asif: confirm open-core vs free-forever messaging (see decision above)
- [ ] Asif: review + finalize all launch posts (copy refreshed 2026-06-02)

## Launch Day (T+0)

### Morning (9-10am ET)
- [ ] Post Show HN (see `show-hn.md`)
- [ ] Post to r/Python with "I Made This" flair (see `reddit.md`)
- [ ] Post Twitter/X thread (see `twitter.md`)
- [ ] Post to r/commandline (see `reddit.md`)

### First 2 Hours (critical)
- [ ] Reply to every HN comment
- [ ] Reply to every Reddit comment
- [ ] Engage with Twitter replies
- [ ] Monitor GitHub issues for new user problems
- [ ] Check PyPI download count

### Afternoon
- [ ] Cross-post to Dev.to (adapted from HN text)
- [ ] Share in relevant Discord servers (Python, DevOps, CLI tools)
- [ ] LinkedIn post (shorter, more professional tone)

## Day 2-3
- [ ] Submit to Product Hunt (see `product-hunt.md`)
- [ ] Reply to any late HN/Reddit comments
- [ ] Write up learnings

## Metrics to Track
- GitHub stars (target: 50 day 1, 200 week 1)
- PyPI installs (target: 100 day 1)
- HN points (target: 50+)
- GitHub issues opened (engagement signal)

## Emergency Playbook
- **Bug reported**: Fix within 1 hour, release patch, reply with fix link
- **Install fails**: Check PyPI, test on clean venv, update README
- **Negative feedback**: Thank them, ask what they'd improve, log for roadmap
