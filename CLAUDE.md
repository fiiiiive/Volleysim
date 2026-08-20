# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Volleysim is a text-based, CLI-driven volleyball league simulator written in pure Python (stdlib only —
`random`, `os`, `datetime`, `time`; no third-party dependencies, no package manager, no test suite).
See `README.md` for the pitch and `VOLLEYSIM_SPEC.md` for the full design spec, known issues, and
prioritized roadmap — read that file before doing any non-trivial engine work, since it lays out which
mechanics are intentional and must be preserved through refactors.

## Commands

There is no build step, package manifest, linter config, or test suite in this repo.

- Run the game: `python3 main.py` (run from the repo root — it reads/writes `aleague.txt`,
  `bleague.txt`, `cleague.txt` in the current directory).
- The game is fully interactive: it blocks on `input()` at many points (advancing weeks, viewing a
  team, confirming playoff results, continuing to another season). There's no non-interactive/headless
  mode currently — keep this in mind if you're trying to test a full season programmatically.

## Architecture

### Entity model (`Player.py`, `Team.py`, `League.py`)

- **`Player`** — a single "star player" per team (this is not a full-roster sim, by design — see
  spec's "Design pillars"). `defineStats()` assigns Swing/Block/Defense/Serve ranges keyed by
  position (OH, OPP, MB, S, L, DS), modeling how each position functions in real volleyball (e.g.
  setters: high serve/defense, low swing; liberos/DS: high defense, low block). This is what gives
  the star-player modifier real texture — preserve the archetype logic if touching it.
- **`Team`** — holds `teamStats` (Swing/Block/Defense/Serve, team stat + star player stat combined
  in `defStats()`), season record (wins/losses/setwins/setlosses/streak/lastfive), and career
  totals (`podiums` = championship/runner-up/third/regular-season/League-B-champ/League-C-champ
  counts, `awards` = Offensive/Defensive Team of the Year counts).
  - `seasonChange()` randomly drifts each stat between seasons and resets the season record. This is
    the **comeback mechanic**: Tier C gets a 1.5x multiplier on positive stat changes, Tier B gets
    1.25x, Tier A gets none — lower tiers bounce back harder, higher tiers regress more toward the
    mean. This is intentional game balance, not a bug.
  - `trade()` swaps star players with a random other team in the league. Trade odds scale with
    standing (`random.randint(0, self.position + 5)`), so worse-placed teams trade more often.
  - `updateStreak()` tracks win/loss streaks and a rolling last-five-opponents record.
- **`League`** — owns a list of `Team`s for one tier (A/B/C) and drives the season: weekly match
  play (`week()`), standings (`printleague()`, `rank()`), and the playoff qualification cut
  (`playoffs()`). League A and League B additionally run the full bracket (`championship()`: quarters
  → semis → third-place → final) and postseason awards (`postawards()`) each season. **League C is
  deliberately lower-stakes** — it's a feeder league without A/B's prestige, so `main.py` computes
  `cleague.playoffs()` but never calls `cleague.championship()` or `cleague.postawards()`; League C's
  postseason is just promoting its top two teams by standing via `printtoptwo()`. `podiums[5]`
  ("League C Champions") exists on `Team` as a result but is never incremented, consistent with C
  having no championship to win.
  - `playGame()` is the point-by-point match engine. Point resolution: pick a random stat category
    (Swing/Block/Defense/Serve), each team rolls `random.randint(0, their_stat_value)`, higher roll
    wins the point. Regular-season matches and championship quarterfinals are best-of-3 sets to 25
    (15-point decider); championship semifinals, the third-place match, and the final are best-of-5
    (also 15-point decider) — **this asymmetry is intentional**, not a placeholder to unify. All sets
    require a 2-point win margin. `watchGame()` is a near-duplicate of `playGame()` with
    `os.system('clear')` + `time.sleep` added for a step-through "watch mode," but it's currently
    **dead code** — nothing in `main.py` calls it. See spec's "Known issues" before changing match
    logic, since the plan is to eventually merge these into one engine that emits events.

### Orchestration (`main.py`)

`main()` is the entire game loop, run top to bottom each time:
1. Load state from `aleague.txt`/`bleague.txt`/`cleague.txt` (whitespace-delimited, one team per
   line — see format below), or generate fresh teams/leagues if the files don't exist.
2. Per season, per league (A, B, C): run trades, apply `seasonChange()`, print stat deltas.
3. Build a round-robin schedule via `rotate()` (a simple "rotate list, zip home vs away" scheme —
   the spec calls out formalizing this into an explicit, inspectable schedule as roadmap work).
4. Simulate 40 weeks per league, printing standings after each and offering a "view team" menu
   every 10 weeks.
5. Run playoffs for each league; run the championship bracket and postseason awards for League A and
   League B only (see below — League C is a feeder league by design and has no bracket).
6. Ask whether to play another season, then apply promotion/relegation (`leagueswap()`)
   unconditionally — this runs every season regardless of the answer. The answer only gates whether
   the outer `while` loop repeats.
7. On exit (loop no longer repeating), write all three leagues back out to their `.txt` files.

`leagueswap()` implements promotion/relegation between tiers: bottom two of A → B, top two of B → A,
bottom two of B → C, top two of C → B. Each `League` accumulates `toptwo`/`bottomtwo` during
`championship()`/`printtoptwo()`/`playoffs()` and these lists are cleared at the end of the swap.

### Persistence format (`aleague.txt`, `bleague.txt`, `cleague.txt`)

Hand-rolled, whitespace-delimited text, one team per line (A-league file has a season-number header
line first). Field order per line: `name tier swing block defense serve podium[0..5] award[0..1]
starFirstName starLastName starPosition`. This format is fragile — it breaks on names containing
spaces, and both the reader (`main.py`) and writer (`main.py`, end of `main()`) must be kept in sync
by hand if the schema changes. The spec's top roadmap priority is replacing this with JSON — check
`VOLLEYSIM_SPEC.md` before extending this format further.

## Working in this codebase

- Simulation logic and terminal I/O (`print`/`input`/`os.system('clear')`) are tightly interleaved
  throughout `League.py` and `main.py`. Any change that assumes a non-CLI caller (a test harness, a
  future UI, a "simulate a whole season instantly" script) needs to account for this coupling —
  don't assume functions like `playGame()` or `championship()` can be called headlessly without
  hitting `input()`.
- Indentation in this codebase is inconsistent (mostly 2-space, some 4-space) — match the
  surrounding function's existing style rather than reformatting whole files.
