# CLAUDE.md — Atlas

## ASIF Governance

This project is **P-15** in the ASIF portfolio (Portfolio Intelligence vertical). On every session:
1. Read `.asif/NEXUS.md` — check for `## CoS Directives` section
2. Execute any PENDING directives before other work (unless Asif overrides)
3. Write your response inline under each directive
4. Update initiative statuses in NEXUS if your work changes them
5. If you have questions for the CoS, add them under `## Team Questions` in NEXUS


## Release Protocol Enforcement (ASIF Standard, ADR-036)

When you bump the version in `pyproject.toml` (the published `atlas-portfolio` package):
1. **Tag**: `git tag vX.Y.Z && git push origin vX.Y.Z`
2. **GH Release**: `gh release create vX.Y.Z --notes-from-tag`
3. **Publish**: `python -m build && twine upload dist/*` (or via release CI)
4. **CHANGELOG**: roll `[Unreleased]` → `[vX.Y.Z] — YYYY-MM-DD` in CHANGELOG.md
5. **Docs**: update any pinned version references in README.md / docs

Pre-push hook (Layer 1, `.git/hooks/pre-push`) chains CI Gate then runs the release-protocol gate — blocks pushes with a version bump but no git tag or dated CHANGELOG section. The daily `release-protocol-check.yml` workflow (Layer 2) opens a `release-drift` issue and auto-closes on resolve. Wolf's nightly sense pass surfaces drift portfolio-wide via `===SECTION:RELEASE_DRIFT===`.

**Bypass (EMERGENCY ONLY)**: `git push --no-verify` — and document the bypass in NEXUS or HANDOFF.
## Dx3 Brain Integration
On every session start, recall relevant context from Dx3 before starting work:
- Use recall() to check for prior decisions, lessons, and patterns related to your current task
- After shipping work, use remember() to store what you learned
- The brain at dx3-cognitive MCP has context from ALL projects — use it

This is how the portfolio compounds intelligence. Your work benefits from every other team's learning.

## Voice Identity
**Voice**: `bm_lewis`
**Service**: http://100.123.83.34:8880/v1/audio/speech
**Registry**: ~/ASIF/standards/voice-registry.md (canonical SoT — supersedes portfolio-voice-registry.md)
**Use**: every cycle-complete, every P0/P1 completion, every directive response — one-sentence summary in Atlas's voice.

Canonical invocation (do NOT build a new service — use PP's endpoint via the portfolio gateway):
```bash
~/ASIF/scripts/cos-speak-remote --voice bm_lewis "One-sentence summary."
```
Direct endpoint fallback:
```bash
curl -sS -X POST http://100.123.83.34:8880/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"model":"kokoro","input":"...","voice":"bm_lewis","response_format":"wav"}' -o /tmp/voice.wav
```
**Rationale**: "Portfolio intelligence — measured, executive" (canonical registry recommendation for P-15). Adopted over the directive's older `am_adam` suggestion per the directive's push-back clause: the consolidated SoT recommends `bm_lewis` for Atlas and reserves `am_adam` for P-08 Faultline — zero collision.

<!-- ASIF:TEAM-ALIGNMENT-WIRING:START -->
## ASIF Alignment Wiring

@/home/axw/ASIF/standards/claude-team-alignment-wiring.md

- Team alignment id: `atlas`.
- Cross-team room: `/alignment`, written through `~/ASIF/scripts/alignment-say`.
- If an `[ALIGNMENT ...]` message appears, respond through `alignment-say`; do not answer only in this private TUI.
- Deterministic state first: typed Dx3/asifctl, `.asif/NEXUS.md`, git/tests/runtime probes. Prose is backup and local steering only.
<!-- ASIF:TEAM-ALIGNMENT-WIRING:END -->
