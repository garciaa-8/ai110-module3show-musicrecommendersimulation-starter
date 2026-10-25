# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommenders often combine collaborative signals, such as what listeners with similar habits enjoyed, with content-based signals from the items themselves. This simulation will use content-based matching: it will compare each song's genre and mood with the user's preferences, and reward energy values close to the user's target. It will rank songs by their total score. The other song attributes are available for future experiments.

- `Song`: `id`, `title`, `artist`, `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`.
- `UserProfile`: `favorite_genre`, `favorite_mood`, `target_energy`, and `likes_acoustic`.

**Current Algorithm Recipe:** Let `G` be 1 for a genre match and 0 otherwise, and `M` be 1 for a mood match and 0 otherwise. For energy values on a 0-to-1 scale, calculate `E = 1 - abs(song.energy - target_energy)`. After the weight-shift experiment, the score is `1*G + 1*M + 4*E`, with a maximum of 6 points. Genre and mood matches are each worth 1 point, while energy similarity is worth up to 4 points. Tempo, valence, danceability, and acousticness are not used in this scoring version.

**Potential Biases:** The increased energy weight can over-prioritize songs near the target energy even when their genre or mood is a poor fit. Mood labels are subjective, and a single target energy may not represent a listener whose taste changes with context. The small catalog may also underrepresent some genres and moods.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

The CLI in `src/main.py` was run against all 20 songs for these three distinct profiles and two edge cases:

The five output blocks below are the baseline run before the weight-shift experiment (`+2` genre, `+1` mood, up to `+2` energy similarity). The experiment's current output is recorded under **Experiments You Tried**.

```python
user_profiles = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.95},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
    "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
    "Conflicting Rock/Chill": {"genre": "rock", "mood": "chill", "energy": 0.90},
    "Unsupported Mood Edge Case": {"genre": "rock", "mood": "sad", "energy": 0.90},
}
```

**Adversarial-profile critique prompt:**

> Review `src/recommender.py`, `src/main.py`, and `data/songs.csv`. The recommender awards 1 point for an exact genre match, 1 for an exact mood match, and up to 4 for energy similarity. Suggest additional adversarial or edge-case preference dictionaries that could reveal surprising rankings, ties, unsupported preferences, or weaknesses in this scoring rule. Explain what each profile tests and what result you would expect before running it.

**High-Energy Pop** (`genre=pop`, `mood=happy`, `energy=0.95`):

```text
1. Sunrise City  |  Score: 4.74/5.00
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (87%, +1.7/2.0)
2. Gym Hero  |  Score: 3.96/5.00
   Reasons: genre match (+2.0); mood mismatch (+0.0); energy similarity (98%, +2.0/2.0)
3. Rooftop Lights  |  Score: 2.62/5.00
   Reasons: genre mismatch (+0.0); mood match (+1.0); energy similarity (81%, +1.6/2.0)
4. No Apologies  |  Score: 2.00/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (100%, +2.0/2.0)
5. Iron Tempest  |  Score: 1.94/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (97%, +1.9/2.0)
```

**Chill Lofi** (`genre=lofi`, `mood=chill`, `energy=0.35`):

```text
1. Library Rain  |  Score: 5.00/5.00
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (100%, +2.0/2.0)
2. Midnight Coding  |  Score: 4.86/5.00
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (93%, +1.9/2.0)
3. Focus Flow  |  Score: 3.90/5.00
   Reasons: genre match (+2.0); mood mismatch (+0.0); energy similarity (95%, +1.9/2.0)
4. Spacewalk Thoughts  |  Score: 2.86/5.00
   Reasons: genre mismatch (+0.0); mood match (+1.0); energy similarity (93%, +1.9/2.0)
5. Coffee Shop Stories  |  Score: 1.96/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (98%, +2.0/2.0)
```

**Deep Intense Rock** (`genre=rock`, `mood=intense`, `energy=0.95`):

```text
1. Storm Runner  |  Score: 4.92/5.00
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (96%, +1.9/2.0)
2. Gym Hero  |  Score: 2.96/5.00
   Reasons: genre mismatch (+0.0); mood match (+1.0); energy similarity (98%, +2.0/2.0)
3. No Apologies  |  Score: 2.00/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (100%, +2.0/2.0)
4. Iron Tempest  |  Score: 1.94/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (97%, +1.9/2.0)
5. Golden Parade  |  Score: 1.84/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (92%, +1.8/2.0)
```

**Conflicting Rock/Chill** (`genre=rock`, `mood=chill`, `energy=0.90`):

```text
1. Storm Runner  |  Score: 3.98/5.00
   Reasons: genre match (+2.0); mood mismatch (+0.0); energy similarity (99%, +2.0/2.0)
2. Midnight Coding  |  Score: 2.04/5.00
   Reasons: genre mismatch (+0.0); mood match (+1.0); energy similarity (52%, +1.0/2.0)
3. Gym Hero  |  Score: 1.94/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (97%, +1.9/2.0)
4. Golden Parade  |  Score: 1.94/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (97%, +1.9/2.0)
5. No Apologies  |  Score: 1.90/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (95%, +1.9/2.0)
```

**Unsupported Mood Edge Case** (`genre=rock`, `mood=sad`, `energy=0.90`):

```text
1. Storm Runner  |  Score: 3.98/5.00
   Reasons: genre match (+2.0); mood mismatch (+0.0); energy similarity (99%, +2.0/2.0)
2. Gym Hero  |  Score: 1.94/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (97%, +1.9/2.0)
3. Golden Parade  |  Score: 1.94/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (97%, +1.9/2.0)
4. No Apologies  |  Score: 1.90/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (95%, +1.9/2.0)
5. Iron Tempest  |  Score: 1.84/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (92%, +1.8/2.0)
```

The High-Energy Pop and Chill Lofi results seem plausible from their metadata: Sunrise City and Library Rain respectively match all three preferences. I do not have subjective listening experience, so this is a feature-based intuition rather than a judgment from hearing the tracks. Under baseline weights, the conflicting profile was less intuitive for someone seeking a chill vibe: Storm Runner ranked first with `2.0` genre points, `0.0` mood points, and `1.98` energy points, totaling `3.98`. Midnight Coding matched mood but scored only `2.04` because its energy was far from the target. This showed that genre and energy together could outweigh a conflicting mood.

Storm Runner appears first for all three rock-based profiles, but not across every profile. That repetition is expected because those profiles all prefer rock and high energy; it also reflects the small catalog, which contains only one rock song. More catalog variety or a mood-sensitive weighting rule could reduce this effect.

**Prompt for the AI coding assistant:**

> In the baseline terminal output, the `Conflicting Rock/Chill` profile ranks Storm Runner first with 3.98 points and Midnight Coding second with 2.04. Inspect `src/recommender.py`, `src/main.py`, and `data/songs.csv`. Explain each song's score using the baseline +2 genre, +1 mood, and up-to-2 energy-similarity weights. Does Storm Runner's first-place result make sense for a listener who asked for a chill mood? Explain which preference dominates and suggest one small scoring adjustment if mood should have more influence.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

**Weight-shift prompt:**

> In `src/recommender.py`, temporarily change the weights so energy similarity is twice as important and genre match is half as important: genre `2.0` to `1.0`, energy multiplier `2.0` to `4.0`, while mood stays at `1.0`. Update reason strings and any displayed maximum score. Verify that energy similarity remains between 0 and 1, the total maximum is 6, and the score math still uses the same normalized energy distance. Run `python3 -m src.main` and compare the profile rankings with the baseline.

The experiment uses `score = 1*G + 1*M + 4*E`, where `E = 1 - abs(song.energy - target_energy)`. Since `G`, `M`, and `E` are each between 0 and 1, the maximum score is 6. The changed weights make energy-aligned results rise; this is a different ranking, not automatically a more accurate one. In particular, mood is now a smaller influence relative to energy.

For the `Conflicting Rock/Chill` profile, the changed top five were:

```text
1. Storm Runner  |  Score: 4.96/6.00
   Reasons: genre match (+1.0); mood mismatch (+0.0); energy similarity (99%, +4.0/4.0)
2. Gym Hero  |  Score: 3.88/6.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (97%, +3.9/4.0)
3. Golden Parade  |  Score: 3.88/6.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (97%, +3.9/4.0)
4. No Apologies  |  Score: 3.80/6.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (95%, +3.8/4.0)
5. Iron Tempest  |  Score: 3.68/6.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (92%, +3.7/4.0)
```

Compared with the baseline, the mood-matching `Midnight Coding` falls out of the top five and high-energy songs move up. This is less intuitive for someone prioritizing a chill mood, so the change is more energetic, not necessarily more accurate.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



