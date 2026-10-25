from src.recommender import Song, UserProfile, Recommender, score_song, recommend_songs

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_score_song_returns_weighted_score_and_reasons():
    user_prefs = {"genre": "rock", "mood": "intense", "energy": 0.9}
    song = {"genre": "rock", "mood": "intense", "energy": 0.98}

    score, reasons = score_song(user_prefs, song)

    assert abs(score - 5.68) < 1e-9
    assert reasons == [
        "genre match (+1.0)",
        "mood match (+1.0)",
        "energy similarity (92%, +3.7/4.0)",
    ]


def test_recommend_songs_returns_top_k_sorted_with_explanations():
    user_prefs = {"genre": "rock", "mood": "intense", "energy": 0.9}
    songs = [
        {"title": "Chill Lofi", "genre": "lofi", "mood": "chill", "energy": 0.4},
        {"title": "Intense Rock", "genre": "rock", "mood": "intense", "energy": 0.9},
        {"title": "Happy Pop", "genre": "pop", "mood": "happy", "energy": 0.7},
    ]

    recommendations = recommend_songs(user_prefs, songs, k=2)

    assert len(recommendations) == 2
    assert recommendations[0][0]["title"] == "Intense Rock"
    assert recommendations[0][1] >= recommendations[1][1]
    assert "genre match (+2.0)" in recommendations[0][2]
