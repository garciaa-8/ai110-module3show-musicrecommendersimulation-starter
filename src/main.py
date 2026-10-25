"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    user_profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.95},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
        "Conflicting Rock/Chill": {"genre": "rock", "mood": "chill", "energy": 0.90},
        "Unsupported Mood Edge Case": {"genre": "rock", "mood": "sad", "energy": 0.90},
    }

    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\nProfile: {profile_name}")
        print(
            f"Preferences: genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
            f"energy={user_prefs['energy']:.2f}"
        )
        print("Top recommendations:")
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']}  |  Score: {score:.2f}/6.00")
            print(f"   Reasons: {explanation}")


if __name__ == "__main__":
    main()
