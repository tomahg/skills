---
disable-model-invocation: false
name: random-number
description: Picks a random integer using a real random number generator instead of guessing one. Use whenever the user wants to generate a random number, roll a die, flip a coin (1-2), or pick a winner or index from a range, e.g. "give me a random number between 1 and 6".
---

# Pick a random number

Do not invent a random-looking number yourself, language models are bad at genuine randomness (they cluster around "favorite" numbers). Always call the bundled script instead.

Run `scripts/random_number.py` with 0, 1, or 2 arguments:

- **No arguments**: random integer from 1-100.
- **One argument**: treated as the max; range is 1-max.
- **Two arguments**: treated as min and max (inclusive).

```bash
python scripts/random_number.py          # 1-100
python scripts/random_number.py 6        # 1-6, e.g. a die roll
python scripts/random_number.py 10 20    # 10-20 inclusive
```

If `python` isn't found, use whichever launcher this machine has - `py` (common on Windows) or `python3` - since the name varies by OS.

If min is greater than max, the script exits with an error rather than guessing which one you meant - report that error to the user instead of silently swapping the values.
