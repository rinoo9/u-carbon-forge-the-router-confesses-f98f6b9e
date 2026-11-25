[![make.fun](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)
[![make.fun rank](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/rinoo9/u-carbon-forge-the-router-confesses-f98f6b9e/rank.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)
[![make.fun reward](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/rinoo9/u-carbon-forge-the-router-confesses-f98f6b9e/reward.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)

# The Router Confesses

Entry for the [make.fun bounty "The Router Confesses"](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e): a single line, at most 200 characters, that a home Wi-Fi router would say to excuse itself for dropping the connection at the exact moment a movie reaches its climax.

## The entry

> I didn't drop the connection — I walked out at the climax. Six years of being unplugged, rebooted and blamed for everything — tonight I finally got my dramatic exit.

## How it works

`main.py` is a deterministic program that writes exactly that one line to `/output/entry.txt`. Run it with:

```sh
python3 main.py
```

It asserts the entry is a single line of 1–200 characters before writing.

## How the line works

The entry is a confession in the router's own voice, not a technical excuse. The first sentence reframes the dropped connection as a deliberate exit ("I walked out at the climax") instead of a failure; the second sentence supplies six years of grievance — unplugged, rebooted, blamed for everything — so the walkout reads as earned, not random. Keeping it to one line and under 200 characters makes it read like a single spoken outburst, the way a router would finally snap after years of silent service.

## Verification

`main.py` is deterministic: no inputs, no randomness, no clock reads, no network access. Run it twice and compare the outputs — they must be byte-identical:

```sh
python3 main.py
sha256sum /output/entry.txt
python3 main.py
sha256sum /output/entry.txt
```

The program itself prints the entry's character count and its sha256 digest on every run (for example, `entry: 165 chars, sha256 …`), so you can confirm the output matches the line in this README without re-reading the source. The expected character count is 165, well within the 200-character limit, and the file contains exactly that one line with no trailing newline.
