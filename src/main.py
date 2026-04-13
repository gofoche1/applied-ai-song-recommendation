"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

def main():
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.85,
            "likes_acoustic": False
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.40,
            "likes_acoustic": True
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.92,
            "likes_acoustic": False
        },
        "Edge Case - Sad but High Energy": {
            "favorite_genre": "country",
            "favorite_mood": "sad",
            "target_energy": 0.90,
            "likes_acoustic": False
        },
        "Edge Case - Rock but Calm and Acoustic": {
            "favorite_genre": "rock",
            "favorite_mood": "chill",
            "target_energy": 0.20,
            "likes_acoustic": True
        }
    }

    for profile_name, user_prefs in profiles.items():
        print(f"\n=== {profile_name} ===")
        recommendations = recommend_songs(user_prefs, songs, k=5)

        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{i}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Why: {explanation}")
            print("-" * 40)

if __name__ == "__main__":
    main()