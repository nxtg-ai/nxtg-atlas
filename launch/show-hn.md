# Show HN: Atlas -- Scan all your repos, score health, find cross-project patterns

**Title** (80 char max):
> Show HN: Atlas -- Portfolio intelligence for your repos (health, deps, patterns)

**URL**: https://github.com/nxtg-ai/nxtg-atlas

**Text** (HN post body):

---

I built Atlas because I manage 10+ repos and no tool gives me a cross-project view. Every AI coding tool works inside one repo. Nobody tells you:

- Which repos have zero tests
- Whether your React versions are consistent across projects
- Where you're duplicating FastAPI patterns instead of sharing them
- Which repos haven't been touched in weeks

Atlas scans your local directories -- no network calls, no cloud, no telemetry. It reads pyproject.toml, package.json, Cargo.toml, runs git commands, counts files, and scores health across 4 dimensions (tests, git hygiene, docs, structure).

What it does:

    pip install nxtg-atlas
    atlas init
    atlas batch-add ~/projects
    atlas scan
    atlas status

30 seconds later you get a full dashboard: A-F health grades, tech stack detection (Python/TS/Rust/Go/Java + frameworks), cross-project intelligence (shared deps, version mismatches, health gaps).

Scanned 8 repos with 1.25M LOC in 31 seconds. State lives in ~/.atlas/portfolio.json -- portable, inspectable, no database.

It also runs in CI. Drop the GitHub Action into any repo and every PR gets a sticky portfolio-health comment:

    - uses: nxtg-ai/atlas-action@v1

(This repo dogfoods its own action -- the health comment on nxtg-atlas PRs reads "🟢 B+ (86%)".)

2,979 tests. MIT licensed, open-core: the full CLI is free and always will be; a Pro tier for heavier cross-project intelligence is on the roadmap.

Built with Python, Typer, and Rich. Would love feedback on what cross-project signals would be most useful to detect next.

---

**Posting notes**:
- Post Tuesday-Thursday, 9-10am ET (HN peak)
- First comment: brief technical detail about how scanning works (file parsing + git probes + a weighted health formula, all local)
- Respond to every comment within 2 hours
