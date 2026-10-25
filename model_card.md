# VibeScout 1.0: Model Card

## 1. Model Name

**VibeScout 1.0** suggests songs based on a listener's stated vibe.

## 2. Goal / Task

The recommender ranks songs for a simple taste profile. It tries to find tracks with a matching genre and mood, and an energy level close to the listener's target.

## 3. Data Used

The catalog has 20 songs. It includes 17 genres and 16 mood labels. Each song has a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The example data is small and manually assembled. It has no real listening history, likes, skips, or playlist data.

## 4. Algorithm Summary

The program gives one point for a genre match and one point for a mood match. It gives up to four points when a song's energy is close to the listener's target. The total can reach six points. Songs with the highest scores appear first. The current version does not use tempo, valence, danceability, or acousticness.

## 5. Observed Behavior / Biases

The catalog has only one rock song, so all three rock-based profiles put Storm Runner first. This is a catalog gap, not proof that every rock fan prefers that track. In the weight experiment, Midnight Coding matched “chill” but fell out of the Conflicting Rock/Chill top five because its energy was far from the target. Energy can outweigh mood, and an unsupported mood like “sad” earns no mood points. The system has no variety rule, so similar high-energy songs can crowd a list.

## 6. Evaluation Process

I ran five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Conflicting Rock/Chill, and Unsupported Mood. I compared their top five results and tested a weight change that doubled energy's importance and halved genre's.

- **High-Energy Pop vs. Chill Lofi:** Their lists do not overlap. Pop favors Sunrise City and Gym Hero; lofi favors Library Rain and Midnight Coding.
- **High-Energy Pop vs. Deep Intense Rock:** Both target high energy, so Gym Hero, No Apologies, and Iron Tempest appear in both. Genre and mood put Sunrise City and Storm Runner at the top of their respective lists.
- **High-Energy Pop vs. Conflicting Rock/Chill:** They share Gym Hero, No Apologies, and Iron Tempest. Their top tracks differ because their genre and mood preferences differ.
- **High-Energy Pop vs. Unsupported Mood:** They share Gym Hero, No Apologies, and Iron Tempest. Both target high energy, while “sad” has no match in the catalog.
- **Chill Lofi vs. Deep Intense Rock:** Their lists do not overlap. Low energy and lofi favor Library Rain; high energy and rock favor Storm Runner.
- **Chill Lofi vs. Conflicting Rock/Chill:** Their lists do not overlap, despite both asking for chill. The conflict profile's high energy and rock preference outweigh its mood match.
- **Chill Lofi vs. Unsupported Mood:** Their lists do not overlap. Their genre and energy preferences point in opposite directions.
- **Deep Intense Rock vs. Conflicting Rock/Chill:** They have the same five songs, but in a different order. Both request rock and high energy; mood changes the order.
- **Deep Intense Rock vs. Unsupported Mood:** They also have the same five songs in a different order. The unsupported mood earns no points, while the rock and energy preferences still match.
- **Conflicting Rock/Chill vs. Unsupported Mood:** Their top five and order are identical. This surprised me: changing “chill” to “sad” did not change the list because the chill matches were too low-energy to reach the top five.

Gym Hero also ranks highly for High-Energy Pop. It is pop and has high energy, even though its mood is “intense,” not “happy.” That makes sense under the score, but a listener who cares more about mood may disagree.

## 7. Intended Use and Non-Intended Use

This is a classroom demo for learning how simple content-based recommendations work. It is useful for trying profiles and scoring weights. It is not a production music service. It should not be treated as a reliable measure of a person's taste or as a replacement for listening to the songs.

## 8. Ideas for Improvement

- Add more songs, especially in underrepresented genres and moods.
- Let listeners set several moods or preferences, not just one energy target.
- Add a variety rule so the top results do not become too similar.

## 9. Personal Reflection

My biggest learning moment was changing the genre and energy weights and seeing Midnight Coding fall out of the Conflicting Rock/Chill top five. The scoring rule was simple, but small weight changes changed what the system treated as a good match. AI tools helped me implement the loader, scoring logic, and CLI output, and helped organize tests and documentation. I still had to check the math, inspect the actual terminal results, and update the README so it did not present old scores as current. I was surprised that a few explicit preferences and a weighted score can feel personal, even though the system does not understand the songs or the listener. Next, I would add more varied tracks, let users express several moods, and test whether a diversity rule makes the results feel more useful.
