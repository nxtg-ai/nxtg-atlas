# Atlas Launch Day Checklist

> **Status (2026-06-02, Atlas team)**: Copy refreshed to ground truth. Messaging = **open-core**
> (Asif confirmed 2026-06-02 — "build a nice community around it"). Marketplace listing is **LIVE**
> (https://github.com/marketplace/actions/atlas-portfolio-health — verified 200; the old "pending
> Asif click" gate was STALE prose, corrected).
>
> 🚫 **NOT launch-ready.** The HN copy must clear the portfolio standing-order gate before posting —
> see "HN gate" below. This is the gap that killed the last 3 attempts: the
> `~/ASIF/learning/hn-launch-engineering/` rubric exists but wasn't applied. Routing to Emma (CoS),
> who owns the rubric, so it's gated deterministically this time.
>
> **Posting boundary**: Asif posts (or names a pre-approved channel). Atlas drafts + gates; does not
> post as Asif to strangers.

## HN gate (STANDING ORDER — blocks the Show HN post)

- [ ] **Emma runs the 53-item HN-SURVIVABILITY-RUBRIC** on `show-hn.md` (`~/ASIF/learning/hn-launch-engineering/02-HN-SURVIVABILITY-RUBRIC.md`). No lock without it.
- [ ] **G1 — external adversarial review** ("what would HN's filter flag in this?") captured in an `external-review-<date>.md`.
- [ ] **A7 account check** — posting account has karma/age and NO flag-dead submission in the last 14 days (hard-block).
- [ ] Hard-block scan green: D1 (no curl|bash), D14 (single mode — body is tool-launch only), D13 (no unearned headline numbers), I7 (not "AI growth marketing"), H6 ("would a senior HN reader flag this?" = no).
- Note: Atlas's first draft is already written TO the rubric (single mode, no number buffet, one link, conversational) — Emma's pass should be fast, not a rewrite.

## Pre-Launch (day before)

- [x] PyPI published and `pip install nxtg-atlas` works (N-06) — **v0.3.0 live, verified 2026-06-02**
- [x] **v0.3.1 published** — `pip install nxtg-atlas` now serves the `--json` width-wrap fix. PyPI 0.3.1 live + GH release v0.3.1; verified on a clean-venv install (0 `console.print(json`, fix present). Run 26857037685 green.
- [x] Capture rendered sticky PR comment as a launch-bundle screenshot — **launch/assets/atlas-action-pr-comment-proof.png**
- [ ] README GIF renders correctly on GitHub (N-07)
- [x] `atlas --help` shows clean output — verified, 25 commands
- [x] `atlas init && atlas add . && atlas scan && atlas status` works end-to-end — commands verified present
- [x] **Buyer first-run validated on a real 33-repo machine (v0.3.2)** — found+fixed a launch-killer: `batch-add ~/projects` hung past 2min and persisted nothing because the scanner traversed `node_modules`/`.venv` (rglob, not pruned). Fixed → ~220× faster per repo; `batch-add` now completes + saves incrementally. **This is the install-then-scan experience a HN reader actually hits.**
- [ ] _(follow-up, non-blocking)_ Parallelize `batch-add`/`scan` across cores — would cut a 33-repo scan from ~133s → ~17s. Strong "wow" enhancement (v0.3.3), not a launch blocker.
- [x] GitHub Action consumable cross-repo (`uses: nxtg-ai/atlas-action@v1`) — **proven, PR #8 merged**
- [x] GitHub repo description and topics set — verified good (8 topics, homepage set)
- [x] atlas-action published to GitHub Marketplace — **LIVE** (listing returns 200), prior "pending click" was stale
- [x] Open-core messaging confirmed (Asif, 2026-06-02)
- [ ] GitHub social preview image uploaded (terminal screenshot)
- [ ] **HN gate cleared** (see "HN gate" section above) — the real pre-post blocker
- [ ] Asif: post (or name a pre-approved channel) once the HN gate is green

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
