import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            for feature in ("energy", "valence", "danceability", "acousticness"):
                row[feature] = float(row[feature])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return reasons."""
    score = 0.0
    reasons = []

    genre_matches = user_prefs["genre"].casefold() == song["genre"].casefold()
    genre_points = 1.0 if genre_matches else 0.0
    score += genre_points
    reasons.append(f"genre {'match' if genre_matches else 'mismatch'} (+{genre_points:.1f})")

    mood_matches = user_prefs["mood"].casefold() == song["mood"].casefold()
    mood_points = 1.0 if mood_matches else 0.0
    score += mood_points
    reasons.append(f"mood {'match' if mood_matches else 'mismatch'} (+{mood_points:.1f})")

    energy_similarity = max(
        0.0,
        1.0 - abs(float(song["energy"]) - float(user_prefs["energy"])),
    )
    energy_points = 4.0 * energy_similarity
    score += energy_points
    reasons.append(
        f"energy similarity ({energy_similarity:.0%}, +{energy_points:.1f}/4.0)"
    )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by score with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    return sorted(scored_songs, key=lambda result: result[1], reverse=True)[:k]
