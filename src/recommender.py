from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


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

    """Calculate a score and reasons for how well a song matches user preferences."""
    def _score_song(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        score = 0.0
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            score += 5.0
            reasons.append("genre match (+5.0)")

        if song.mood.lower() == user.favorite_mood.lower():
            score += 3.0
            reasons.append("mood match (+3.0)")

        energy_score = max(0.0, 2.0 - abs(song.energy - user.target_energy) * 4)
        score += energy_score
        reasons.append(f"energy similarity (+{energy_score:.2f})")

        if user.likes_acoustic:
            acoustic_score = song.acousticness
            score += acoustic_score
            reasons.append(f"acoustic preference (+{acoustic_score:.2f})")
        else:
            acoustic_score = 1.0 - song.acousticness
            score += acoustic_score
            reasons.append(f"low acousticness preference (+{acoustic_score:.2f})")

        return score, reasons
    """Rank songs by score and return the top k recommendations with explanations."""
    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []

        for song in self.songs:
            score, _ = self._score_song(user, song)
            scored_songs.append((song, score))

        scored_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = self._score_song(user, song)
        return f"{song.title} by {song.artist}: " + ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 5.0
        reasons.append("genre match (+5.0)")

    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 3.0
        reasons.append("mood match (+3.0)")

    energy_score = max(0.0, 2.0 - abs(song["energy"] - user_prefs["target_energy"]) * 4)
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    if user_prefs["likes_acoustic"]:
        acoustic_score = song["acousticness"]
        score += acoustic_score
        reasons.append(f"acoustic preference (+{acoustic_score:.2f})")
    else:
        acoustic_score = 1.0 - song["acousticness"]
        score += acoustic_score
        reasons.append(f"low acousticness preference (+{acoustic_score:.2f})")

    return score, reasons

def critique_recommendation(user_prefs, song, reasons):
    critiques = []

    reason_text = " ".join(reasons)

    if "genre match" not in reason_text:
        critiques.append("genre mismatch")

    if "mood match" not in reason_text:
        critiques.append("mood mismatch")

    if "energy similarity" not in reason_text:
        critiques.append("energy not well aligned")

    if user_prefs["likes_acoustic"]:
        if song["acousticness"] < 0.5:
            critiques.append("not very acoustic")
    else:
        if song["acousticness"] > 0.5:
            critiques.append("too acoustic")

    return ", ".join(critiques) if critiques else "strong match"

def recommend_songs(user_prefs, songs, k=5):
    scored_songs = []

    max_possible_score = 11.0

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        confidence = score / max_possible_score

        explanation = ", ".join(reasons)
        critique = critique_recommendation(user_prefs, song, reasons)

        scored_songs.append((song, score, explanation, critique))

    scored_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)

    return scored_songs[:k]