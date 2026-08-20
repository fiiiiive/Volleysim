# Volleysim — Project Spec & Roadmap

## What it is
A text-based volleyball league simulator. Three tiers (A/B/C) with promotion/relegation,
40-game regular seasons, 8-team playoffs, player trades, and season-over-season stat drift.
Originally built as a CLI game in college; being revived and extended.

## Design pillars (keep these — don't over-engineer past them)
- **Simplicity over realism.** Team-level stats (Swing, Block, Defense, Serve) plus one
  "star player" as a modifier. Deliberately not a full-roster sim — that's a possible
  future layer (injuries, bench players), not a v1 requirement.
- **Point-by-point resolution.** Each point: random stat category chosen, each team rolls
  a random value up to their stat in that category, higher roll wins the point.
- **Three-tier league with promotion/relegation**, standard 2-of-3 sets to 25 (15 for
  the decider).
- **Comeback mechanic (already implemented, confirm it's tuned right):** in
  `Team.seasonChange()`, Tier C teams get a 1.5x multiplier on positive stat changes
  between seasons, Tier B gets 1.25x, Tier A gets no boost — so lower-tier teams are
  more likely to bounce back and higher-tier teams are more likely to regress.

## Design highlights worth preserving (don't flatten these in a refactor)
These are the mechanics that make the sim feel intentional rather than generic —
protect them explicitly when touching engine code:
- **Position-based stat archetypes.** `Player.defineStats()` assigns stat ranges by
  position (setters: high serve/defense, low swing; liberos/DS: high defense, low
  block; middle blockers: high block, moderate elsewhere) that map to how those
  positions actually function in real volleyball. This is what gives the star-player
  modifier real texture.
- **Trade frequency tied to standing.** `Team.trade()` uses
  `random.randint(0, self.position + 5)`, so worse-standing teams roll a wider range
  and trade more often — realistic (bad teams shake things up) and good for gameplay
  (keeps lower teams from being permanently stuck).
- **Streak + head-to-head history.** `updateStreak()` tracks win/loss streaks and a
  rolling last-five-opponents record per team. Useful raw data for the future stat
  tracker (rivalry history, hot/cold runs).
- **Full playoff bracket.** Quarters → semis → third-place match → championship, with
  seeding based on final standings — a complete bracket, not a shortcut winner-pick.
- **Comeback mechanic.** In `Team.seasonChange()`, Tier C gets 1.5x multiplier on
  positive stat changes between seasons, Tier B gets 1.25x, Tier A gets none — lower
  tiers bounce back harder, higher tiers regress more.

## Current known issues (from code review)
- `playGame` and `watchGame` in `League.py` are near-duplicate ~90-line functions —
  same logic, different print/sleep behavior. Should merge into one engine function
  that emits events; display layers (silent, live-CLI, future UI) subscribe to those
  events instead of the engine calling `print`/`input` directly.
- Simulation logic and I/O (`print`/`input`) are tightly coupled throughout
  `League.py` and `main.py`. This blocks any non-CLI frontend and blocks a clean
  "real-time match" API.
- Save/load uses a hand-rolled whitespace-delimited `.txt` format — fragile (breaks on
  names with spaces) and awkward to extend.

## Roadmap (priority order, per your notes)

### 1. JSON persistence
Replace `aleague.txt` / `bleague.txt` / `cleague.txt` with JSON. Design a clean schema
up front (teams, star player, stat history, podiums/awards, season number) so it's easy
to extend later without another migration. This was flagged as "busy work" before —
worth just doing it once, properly, with a schema that anticipates the stat-tracker
work in priority 3 (e.g. leave room for match-level records, not just team totals).

### 2. Sim logic, real-time match play, and league schedule (UI secondary)
- Decouple the engine from I/O first (see issues above) — this unblocks everything else.
- Real-time match playing: the engine should be able to emit a point-by-point event
  stream that a caller can consume live (for a future "watch mode" or UI) or just
  resolve instantly (for fast season sims).
- League schedule: formalize the round-robin/rotation logic (`rotate()` in `main.py`)
  into something explicit and inspectable — useful both for a future UI and for the
  stat tracker (e.g. "what was the schedule for season 4").
- Basic UI is secondary — don't block on it, but keep the engine decoupled enough
  that a UI (even just a `rich`/`textual` TUI) is a thin layer, not a rewrite.

### 3. Stat tracker / all-time records database
Lightweight — not a full analytics system. Examples of what to track:
- Championships per team per league, per season
- Highest single-season offensive/defensive score
- Highest single-match point total
- Longest win streak
- All-time win/loss record per team across tier changes

A simple SQLite database (or even a JSON append-log if SQLite feels heavy) fed by
events from the decoupled engine would cover this well, and pairs naturally with the
JSON persistence work in priority 1.

## Explicitly out of scope for now
- Full individual roster simulation (injuries, bench players, rotations) — noted as a
  "maybe later," not a current requirement.
- Real UI/frontend — sequenced after the engine refactor, not before.
