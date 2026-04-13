# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  
This recommender is designed to generate song suggestions based on a user’s preferences for genre, mood, energy level, and acoustic style.

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

The model works by comparing each song’s features to a user’s preferences and assigning a score based on how closely they match. It considers features such as genre, mood, energy level, and acousticness for each song.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset contains 15 songs with a mix of genres such as pop, lofi, rock, ambient, jazz, hip-hop, classical, reggae, and electronic. Each song includes features like mood, energy, tempo, valence, danceability, and acousticness.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users with clear and consistent preferences, such as those who enjoy high-energy pop or chill lofi music. It effectively captures patterns where genre and mood strongly define the listening experience. 
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One weakness I discovered is that the recommender over-prioritizes genre, which can limit the diversity of results. Even when a song closely matches the user’s mood and energy, it may still rank lower if the genre is not an exact match. This became especially clear in edge cases where users had mixed preferences, such as wanting high-energy but sad music, where the system struggled to find balanced recommendations.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

I evaluated the recommender by testing several user profiles, including “High-Energy Pop,” “Chill Lofi,” and “Deep Intense Rock,” as well as edge cases like “Sad but High Energy” and “Rock but Calm and Acoustic.” For each profile, I looked to see whether the top recommendations matched the expected genre, mood, and energy levels. The system performed well for clear profiles, consistently returning songs that aligned with the user’s preferences, but it struggled with conflicting profiles, where no song perfectly matched all criteria.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would improve the model by adding more features such as tempo ranges, lyrical themes, or user listening history to better capture musical preferences.
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned how recommender systems convert user preferences into numerical scores and rankings. One interesting discovery was how small changes in scoring weights can significantly impact the final recommendations.