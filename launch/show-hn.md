# Show HN — Atlas (DRAFT — pending HN-survivability rubric pass + external review)

> ⚠️ **NOT launch-ready until gated.** Per the portfolio standing order
> (`~/ASIF/learning/hn-launch-engineering/`), no Show HN locks without:
> (1) a pass of the 53-item HN-SURVIVABILITY-RUBRIC (owned by Emma/CoS), and
> (2) G1 — an external adversarial review ("what would HN's filter flag here?").
> The previous portfolio HN attempt (Runtime Diet) died in 13 min on mode-mixing +
> gratuitous numbers. This draft is written to the rubric (single mode, no number
> buffet, one canonical link, conversational), but still must clear the formal gate.
> Also confirm the posting account's karma/age (A7 hard-block: no flag-dead post in 14d).

**Title** (descriptive, man-page register — CR-2):
> Show HN: A local CLI that scans all your git repos and scores their health

**URL** (single canonical link — CR-3 / D11): https://github.com/nxtg-ai/nxtg-atlas

**Text** (HN post body — ONE mode: tool launch):

---

I have a folder of git repos that's grown over a couple of years, and I'd lost track of the state of them — which ones still had tests, which hadn't been touched in months, whether I was on three different versions of the same dependency across them.

So I wrote a small CLI that reads each repo locally and gives me one view across all of them. It parses pyproject.toml / package.json / Cargo.toml, runs a few git commands, counts source and test files, and prints a dashboard with a rough health grade per repo plus a few cross-repo notes (shared dependencies, version mismatches, repos with no tests).

    pip install nxtg-atlas
    atlas init
    atlas batch-add ~/projects
    atlas scan
    atlas status

It runs entirely on your machine — no network calls, no account, no telemetry. State is a single JSON file under ~/.atlas you can read or delete.

It's deliberately simple: the "health score" is just a weighted count of things like test presence and git hygiene, so treat it as a rough signal, not a verdict. It won't understand your code — it only sees structure and metadata.

It's MIT licensed. I'd genuinely like to know what cross-repo signals you'd find useful — that's the part I'm least sure I've got right.

---

**Posting notes**:
- Post Tue–Thu, ~9–10am ET (per playbook; Tuesday historically strongest).
- ONE mode only — this body is tool-launch. Do NOT add metrics, the CI action, or
  monetization here (that's mode-mixing, a hard-block). Put the GitHub Action and any
  numbers in the FIRST COMMENT or the README, not the submission body.
- First comment (after post lands): brief technical note on how the health formula
  works, and mention the optional GitHub Action for CI as a "by the way."
- Respond to every comment within ~2 hours, plainly, no marketing register.
