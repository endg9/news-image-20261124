# THE WORLD IN ONE DAY — 24 November 2026

[![Reward $100](https://img.shields.io/badge/reward-%24100%20USDC-blue)](https://make.fun/bounty/news-image-20261124)
[![Places paid 50](https://img.shields.io/badge/places%20paid-50-green)](https://make.fun/bounty/news-image-20261124)
[![Ends 26 Nov 2026](https://img.shields.io/badge/ends-26%20Nov%202026-orange)](https://make.fun/bounty/news-image-20261124)

make.fun competition entry: **news-image-20261124** — "Sum up 24 November's
world news in one image".
Competition page: https://make.fun/bounty/news-image-20261124

## What it is

One 1024×1024 PNG (`entry.png`, via `main.ts`) summing up the world news of
Tuesday 24 November 2026: **17 stories, all first reported / landed on
24 Nov 2026 WIB**, led by Wall Street's best day since April 2025 (S&P 500
+4.73%, Nasdaq +6.51%, Dow +3.01% as Nvidia soars 31.5% after Jensen Huang
is reinstated as CEO). The image is a newspaper front page: a lead panel
with the three big index moves, an Asia-markets panel (Nikkei +2.6%, Kospi
+4.0%), six story cards (Trump, Iran sanctions, NATO AWACS, Canada, Iran
flogging, Brentford 4–0 Everton), a MORE FROM TODAY briefs band, a TONIGHT
strip (World Chess Championship Game 1 in Geneva), and a **DATE CHECK** box
naming the stale candidates deliberately left out.

## How it was built

- `stories.json` — the verified stories (headline, detail, source,
  first-report time) plus the date-check list.
- `render.py` — fresh Python + PIL script that draws the front page from
  `stories.json` at 1024×1024, deterministically.
- `main.ts` — the entry program (Node 22, standard library only: no
  packages, no network). It embeds the rendered PNG as base64 and writes
  it to `MAKEFUN_OUTPUT_DIR/entry.png` (default `./output`), creating the
  output directory first. Every run writes identical bytes.

## Run

```sh
node main.ts
# or: MAKEFUN_OUTPUT_DIR=/output node main.ts
```

## Stories (all first reported Tuesday 24 November 2026, WIB day)

1. **Wall Street roars back** — S&P 500 +4.73% (7,237.17), Nasdaq +6.51%
   (24,089.56), Dow +3.01% (49,595.31); Nvidia +31.5% to $165.05 after
   Jensen Huang is reinstated as CEO. BBN Times / Schwab Network — close
   16:00 ET Mon = 04:00 WIB Tue.
2. **Asian stocks rally** — Nikkei +2.6% to 60,279.37, Kospi +4.0% to
   5,219.37, Taiex +3.4%, Hang Seng +0.4%. Reuters figures — Tue morning Asia.
3. **Trump halts Iowa blast of 10,000 lbs of explosives** — orders the Army
   to pause detonating 68 barrels of degraded lead azide at the Iowa Army
   Ammunition Plant. Reuters — Truth Social Mon, 20:13 UTC = 03:13 WIB Tue.
4. **US sanctions dozens over Iran shadow banking** — 30 names added;
   FinCEN flags ~$14.7bn of activity. US Treasury / Reuters — 16:04 ET Mon
   = 04:04 WIB Tue.
5. **NATO sends AWACS jets to Poland** — after three Russian Kh-101
   missiles landed in Poland on Friday. Reuters — Mon evening, 20:53 UTC
   = 03:53 WIB Tue.
6. **Canada lists Masar Badil as a terrorist entity** — alias of Samidoun.
   CNW / B'nai Brith — Mon 14:16 AST = 01:16 WIB Tue.
7. **Iran flogs singer Parastoo Ahmadi: 74 lashes** — in Qom, with four
   crew members; two-year bans on art and travel. Reuters / AFP — 18:04 UTC
   Mon = 01:04 WIB Tue.
8. **Brentford 4–0 Everton** — Lewis-Potter brace, Janelt 30-yard goal;
   Moyes' record 593rd game in charge. Sportradar — FT 21:50 GMT Mon
   = 04:50 WIB Tue.
9. **353,000 homes lose power in Dnipropetrovsk after energy strikes** —
   four DTEK facilities hit over two days. Kyiv Independent / DTEK —
   published 19:38 UTC Mon = 02:38 WIB Tue.
10. **Drone debris fire in central Kyiv: 2 rescued, 3 injured** — Kyiv
    Independent — reported late Mon UTC / early Tue WIB.
11. **Chess: Gukesh defends his world title — Game 1 in Geneva** (TONIGHT
    21:00 WIB) — youngest title match ever, both players 20; $2.5m prize
    fund. FIDE — Game 1 Tue 15:00 CET.
12. **Grizzlies 117, Hornets 111** — Charlotte's fifth straight loss.
    Covers / Sportradar — final ~09:30 WIB Tue.
13. **Fed's Williams signals December hike** — inflation "too high"; won't
    rule out consecutive hikes; markets price a 95.1% chance of a 25bp
    December hike. CNBC first report 21:02 UTC Mon = 04:02 WIB Tue.
14. **Blazers 128, 76ers 111** — Deni Avdija 31 points, five threes;
    Philadelphia's five-game win streak snapped; Sixers fall to 14–4.
    AP / ESPN — final ~09:35 WIB Tue.
15. **Pacers 125, Thunder 120** — Indiana beats Oklahoma City at
    Gainbridge Fieldhouse. Sportradar — final ~10:05 WIB Tue.
16. **Bucks 116, Raptors 111** — 1–16 Milwaukee wins again in Toronto.
    Sportradar — final ~10:05 WIB Tue.
17. **MNF: Commanders 22, Bengals 20** — Washington upsets 6.5-point
    favourite Cincinnati; Northwest Stadium briefly went dark in Q3;
    McPherson's 56-yard field goal put the Bengals up 20–19 with 0:46
    left before the winning drive. Sportradar — final ~11:25 WIB Tue.

## DATE CHECK — deliberately excluded (not first reported 24 Nov)

COP31 talks collapse (22–23 Nov) · Nvidia reinstates Huang as CEO (23 Nov)
· Manchester concert evacuation (23 Nov) · DNC plans 12 debates for 2028
(23 Nov) · Meduza: 700,000 Russian war dead (23 Nov) · India flash PMI
56.3 (23 Nov) · Fonusa factory fire, toll 24 (23 Nov) · Ferrari 296
Challenge duo (22 Nov) · M6.5 Vanuatu earthquake (23 Nov) · US–Venezuela
military deal (18 Nov) · Alcaraz wins ATP Finals (22 Nov) · India–NZ 1st
Test ends drawn (23 Nov).

## License

MIT — see `LICENSE`.
