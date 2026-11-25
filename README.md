# news-image-20261124 — The World in One Day

One image summing up the world's news of **Tuesday 24 November 2026**:
37 stories across 8 regions, drawn and rendered from reported news.

## The image

`entry.png` (1024×1024, 189,733 bytes) is a newspaper-style poster:

- Masthead naming the day: **TUESDAY 24 NOVEMBER 2026**
- Four lead stories with drawn scenes: the Strait of Hormuz closure,
  Nvidia's +31.5% surge, the overnight strike on Zaporizhzhia, and the
  factory fire in Banten, Indonesia (26 confirmed dead)
- A world map with 8 numbered pins and a region legend (Europe & Ukraine
  war 10, Asia 8, North America 6, Middle East 5, Africa 3, Global &
  climate 2, Latin America 2, Science & space 1)
- 33 more stories in brief, each a short label with one line of detail
- A UTC timeline of the day as it unfolded (times as reported)
- A date-check audit strip: every story was first reported on 24 November
  2026; one claim is flagged UNVERIFIED (the IRGC claim that 3 tankers hit
  naval mines — JMIC: unconfirmed); one event is set for 25 November
  (the Shenzhou-24 launch, reported on 24 November)

Sources: Reuters, AP, BBC, Just Security Early Edition, The Global Eye,
OneTurn. Drawn and rendered from reported news — no photographs.

## The program

`main.py` (Python 3, standard library only, no network) copies the
pre-rendered `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, verifies the
copy byte-for-byte with SHA-256, checks the competition gate (PNG, at most
1024×1024, at most 1 MiB), and fails hard on any mismatch.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
