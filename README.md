# 🎵 Music Recommender Simulation

## Project Summary


This project is an AI-powered music recommender system that suggests songs based on a user’s preferences such as genre, mood, energy level, and acoustic style. It uses a transparent scoring algorithm to rank songs and provide explanations for each recommendation. The goal is to demonstrate how simple AI systems can turn structured data into meaningful, personalized outputs.

### Original Project (Modules 1–3)

This project builds on my earlier work in Modules 1–3, where I designed a basic rule-based recommender system. The original system focused on representing songs and user preferences as data and using a simple scoring function to rank songs. In this version, I expanded the system by adding explainability, confidence scoring, and a self-critique mechanism to make the recommendations more transparent and reliable.

### Architecture Overview

The system follows a simple CLI-first architecture:

Data Layer: Songs are stored in a CSV file (data/songs.csv)
Logic Layer: Python functions handle scoring, ranking, and critique
User Input Layer: User preferences are defined in main.py
Output Layer: Results are printed in the terminal with explanations
Flow:
Load song data from CSV
Input user preferences
Score each song based on matching features
Rank songs from highest to lowest score
Output top recommendations with explanations and model critique

---

---

## ⚙️ Setup Instructions

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
python3 -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```
No additional dependencies are required beyond Python 3.

# Sample Output
Example:
1. Sunrise City by Neon Echo
   Score: 10.74
   Why: genre match (+5.0), mood match (+3.0)
   Model Check: strong match
⚖️ Design Decisions
Weighted scoring system (genre > mood > energy)
CLI-first design for simplicity
Added explanation + critique for transparency

## 🧪 Testing Summary

I tested the recommender with multiple user profiles and compared the top 5 results against expected outcomes. Clear profiles like High-Energy Pop and Chill Lofi produced accurate recommendations, while edge cases exposed weaknesses in the scoring logic. The self-critique feature helped identify mismatches such as genre mismatch, mood mismatch, and acoustic mismatch.

Summary: The recommender worked well for clear user preferences but struggled with conflicting profiles. This showed that the system is reliable for simple use cases, but limited by its small dataset and fixed scoring rules.

## Reflection

This project helped me understand how recommender systems translate user preferences into numerical scores and ranked outputs. I learned that even simple rule-based systems require careful design to avoid bias and ensure fairness. One of the most interesting takeaways was how small changes in scoring weights can significantly impact results. This experience gave me a deeper appreciation for how real-world systems like Spotify or Netflix balance personalization, diversity, and user satisfaction.

My recommender has limitations due to its small dataset and fixed scoring rules, which can introduce bias. It tends to over-prioritize genre and uses exact matching, which may ignore similar styles and reduce diversity in recommendations. This system could be misused by reinforcing narrow preferences, so improvements like adding more diverse data and allowing partial matches would help make it more balanced. During development, AI tools were helpful for suggesting features like the self-critique function, but sometimes gave flawed code that required debugging. 


Loom Link:
