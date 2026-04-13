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

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
Each Song object includes the following features: id, title, artist, genre, mood, energy (as a float), tempo_bpm, valence, danceability, and acousticness. These are used to match against user preferences in the recommendation process.

- What information does your `UserProfile` store
The UserProfile stores the user's favorite_genre, favorite_mood, target_energy, and likes_acoustic.

- How does your `Recommender` compute a score for each song
The Recommender computes a score by evaluating how well each song's features align with the user's profile. For numerical features like energy, it uses a formula that rewards closeness to the user's preference (e.g., score = max(0, 1 - |user_preference - song_feature|)). Categorical features like genre and mood are scored as 1 for matches and 0 otherwise.

- How do you choose which songs to recommend
Songs are chosen by first computing scores for all songs using the scoring rule, then ranking them by score in descending order. The top k songs (default 5) are selected and returned as recommendations, ensuring the most relevant ones are prioritized.

You can include a simple diagram or bullet list if helpful.




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


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> FoundtheVibe 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.
The system recommends songs by comparing what the user likes with the features of each song, and then giving each song a score based on how well it matches.

- What features of each song does it consider
Genre,Mood,Energy level,Danceability, Acousticness
- What information about the user does it use
The system looks at the user’s preferences,their favorite genre, their preferred mood and their target energy level
- How does it turn those into a number
For each song, the system compares its features with the user’s preferences.
If the song’s genre or mood matches the user’s favorites, it gets a higher score

"Algorithm Recipe"
My recommender uses a point-based scoring system to rank songs based on how closely they match a user’s taste profile. Each song is scored using four features: genre, mood, energy, and acousticness. A song receives +2.0 points if its genre matches the user’s favorite genre, +1.0 point if its mood matches the user’s favorite mood, and up to +2.0 points based on how close its energy level is to the user’s target energy using the formula max(0, 2.0 - abs(song_energy - target_energy) * 4).

"Bias"
It may over-prioritize genre, which could cause it to miss songs from other genres that still strongly match the user’s mood or energy preferences.
---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

