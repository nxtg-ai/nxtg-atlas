# Changelog

All notable changes to `nxtg-atlas` are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Cross-project LLM model-version drift detection.** A new `detect_ai_models()` scanner finds the specific model identifiers a project pins in its source/config (e.g. `claude-opus-4-8`, `gpt-4o`, `gemini-2.0-flash`) — going beyond "this project uses the Anthropic SDK" to "this project pins *this model*". Surfaced per-project in `atlas inspect` (**AI Models**), in `atlas search`, and in JSON/CSV/Markdown export. Cross-project intelligence in `atlas connections`/`atlas doctor` now flags **model drift** (one provider pinned to multiple versions across the portfolio — e.g. `claude-3-opus` in one repo, `claude-opus-4-8` in another) and **older-generation model pins** (`gpt-3.5-turbo`, `claude-instant`, `text-davinci-*`) as upgrade candidates. Detection is bounded for speed (pruned `walk_files` walk + size/file caps, docs and tests excluded) and uses strict version-specific patterns so prose and bogus strings never match. Drift is flagged only when projects genuinely *disagree* on pinned versions — identical model sets, including deliberate tiering (opus + haiku replicated everywhere), are treated as consistency, not drift. 22 tests added (suite 2,983 → 3,005).

## [0.3.2] — 2026-06-12

### Fixed
- **Scanning is dramatically faster on real repos.** `walk_files` now uses `os.walk` with in-place directory pruning instead of `rglob("*")` + post-filter. The old approach still *traversed* `node_modules`/`.venv`/etc. (stat-ing every vendored file) before discarding them — a single repo with `node_modules` took **~110s**; it now takes **~0.5s** (≈220×). Counts are unchanged; only wasted traversal is removed.
- **Virtualenvs with non-standard names are now skipped** via their `pyvenv.cfg` marker (e.g. `venv_linux`, `.env39`), not just the hardcoded `venv`/`.venv` names.

### Added
- Expanded the skip-directory set with common vendored/build/cache dirs: `vendor`, `Pods`, `Carthage`, `bower_components`, `jspm_packages`, `.yarn`, `.pnpm-store`, `.gradle`, `.idea`, `.vs`, `DerivedData`, `.dart_tool`, `.terraform`, `.terragrunt-cache`, `.serverless`, `.turbo`, `.svelte-kit`, `.parcel-cache`, `.astro`, `.output`, `.cache`, `site-packages`.

### Changed
- `atlas batch-add` now **saves the portfolio incrementally** (after each repo). A slow or Ctrl-C-interrupted run no longer loses everything — it keeps what was scanned and tells you to rerun for the rest.

## [0.3.1] — 2026-06-02

### Fixed
- `atlas compare`, `atlas search`, and `atlas top` `--json`/`--format json` output is now emitted via plain `print` instead of the Rich console. The Rich console soft-wraps long strings to the terminal width, which could inject a newline mid-string (e.g. inside a long project path) and produce **invalid JSON** in narrow terminals. Machine-consumable output is now width-independent. Regression test added.

## [0.3.0] — 2026-05-05

Major release. Adds new CLI commands (`ci`, `doctor`, `trends`, `compare`, `config`, `search`), expands detection by ~50 categories, and ships extensive cross-project intelligence. 2,979 tests passing.

### Added — CLI commands
- `atlas ci` — CI/CD gate command. Re-scans portfolio, exits non-zero on health-threshold violations. Outputs structured JSON or one-line summary. `--min-health` and `--min-project-health` thresholds. Powers the new [`atlas-action`](https://github.com/nxtg-ai/atlas-action) GitHub Action.
- `atlas doctor` — actionable per-project and portfolio-wide recommendations (critical / high / medium / low) with specific fix actions across health, security, quality, infrastructure, AI/ML, testing, and documentation dimensions.
- `atlas trends` — scan history and deltas. Compares the last two snapshots showing portfolio direction, per-project up/down/stable/new/removed, and test-count changes. Capped at 100 entries.
- `atlas compare <a> <b>` — side-by-side project comparison. Health breakdown deltas, metrics comparison, tech-stack overlap, version-mismatch detection, actionable insights.
- `atlas config` — persistent TOML configuration at `~/.atlas/config.toml`. Stores CI thresholds and export defaults. Stdlib-only (no new dependencies).
- `atlas search` — search across projects by name, language, framework, or tech.
- `atlas inspect <name>` — detailed per-project card with all detected tech.

### Added — detection (50+ new categories)
Infrastructure (Docker, K8s, Terraform, CI/CD, serverless, cloud providers), security tooling, code-quality tooling, testing frameworks, databases, package managers, licenses, documentation artifacts, CI/CD configuration, runtime versions, AI/ML tooling, monitoring & observability, i18n / localization, geospatial, data visualization, PDF & documents, cryptography, async, media, scraping, compression, accessibility, email, desktop frameworks, file storage, form libraries, animation, routing libraries, game frameworks, CMS, rate limiting, database migrations, gRPC/RPC, code generation, mocking, changelog & release tools, E2E & browser testing, monorepo tools, error tracking & APM, static site generators, mobile frameworks, analytics, workflow engines, secrets management.

### Added — intelligence (cross-project patterns)
Shared-tool detection, divergence warnings, gap detection, and recommendation hooks for every detection category. Connection categories expanded across security, infrastructure, AI/ML, testing, databases, packages, licenses, documentation, CI/CD, monitoring, i18n, geospatial, data viz, PDF, crypto, async, media, scraping, compression, a11y, email, desktop, file storage, forms, animation, routing, game, CMS, rate limiting, migrations, gRPC, codegen, mocking, changelog, E2E, monorepo, error tracking, SSG, mobile, analytics, workflows, secrets.

### Added — experience
- Portfolio summary panel with quick insights.
- Per-category summary panels (testing, database, package manager, license).
- Filterable project list (`--lang`, `--has`, `--grade`, `--min-health`, `--max-health`, sort, limit).
- Rich markdown export.
- Enhanced JSON / CSV export.
- Sort commands across status, search, doctor, compare, connections, and export.

### Added — distribution
- Tag-based release automation: pushing `v*` tags triggers full test matrix → build → twine validate → PyPI publish via Trusted Publisher → GitHub Release.
- CLI integration tests covering every shipped command.

### Changed
- `atlas inspect`, `atlas doctor`, and `atlas status` now surface the full detection footprint across 50+ categories.
- `atlas ci` is the canonical CI integration path; supersedes the prior "CI integration coming soon" FAQ.

### Notes
- Test count: 2,979 passing (up from 30 at 0.1.0, 221 at 0.2.0 baseline).
- ADR-036 release-protocol enforcement (Layer 1 pre-push, Layer 2 nightly drift check) is active for all future releases.

## [0.2.0] — 2026-03-13

Initial public release. Tech stack detection, health scoring, cross-project patterns, terminal dashboard, GitHub CI integration, PyPI publishing.

## [0.1.0] — 2026-03-04

Internal release. 1,814 LOC, 30 tests.
