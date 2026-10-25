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

**Algorithm Recipe:** Let `G` be 1 for a genre match and 0 otherwise, and `M` be 1 for a mood match and 0 otherwise. For energy values on a 0-to-1 scale, calculate `E = 1 - abs(song.energy - target_energy)`. The score is `2*G + 1*M + 2*E`. This gives genre up to 2 points, mood 1 point, and energy similarity up to 2 points; closer energy earns more points, regardless of whether it is high or low. Tempo, valence, danceability, and acousticness are not used in this first scoring version.

**Potential Biases:** The genre weight may over-prioritize a favorite genre and miss excellent songs in other genres that fit the user's mood and energy. Mood labels are subjective, and a single target energy may not represent a listener whose taste changes with context. The small catalog may also underrepresent some genres and moods.

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

```text
Loaded songs: 20

Top recommendations:

1. Sunrise City  |  Score: 4.96/5.00
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (98%, +2.0/2.0)

2. Gym Hero  |  Score: 3.74/5.00
   Reasons: genre match (+2.0); mood mismatch (+0.0); energy similarity (87%, +1.7/2.0)

3. Rooftop Lights  |  Score: 2.92/5.00
   Reasons: genre mismatch (+0.0); mood match (+1.0); energy similarity (96%, +1.9/2.0)

4. Side Street Shuffle  |  Score: 1.98/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (99%, +2.0/2.0)

5. Night Drive Loop  |  Score: 1.90/5.00
   Reasons: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (95%, +1.9/2.0)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

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



