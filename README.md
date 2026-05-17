# Nudge 🧠
### Track your day. Understand yourself.

Nudge is a full-stack AI-powered productivity tracker that analyzes your daily habits and uses machine learning to find patterns — telling you exactly what's helping or hurting your productivity.

**Live Demo:** [nudge-awpw.onrender.com](https://nudge-awpw.onrender.com)

---

## What it does

- Log daily habits — social media time, productive screen time, tasks completed, sleep hours, and mood
- ML pipeline analyzes your data and calculates a daily productivity score
- Dashboard shows productivity trends over time with interactive charts
- AI-generated insights like *"You're 57 points more productive on days you sleep 7+ hours"*
- Predicts tomorrow's productivity score based on your recent patterns

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, Chart.js |
| Backend | Python, Flask |
| Database | SQLite |
| ML & Data | Pandas, Scikit-learn, NumPy |
| Deployment | Render |

---

## How the ML works

1. **Data collection** — user logs daily habits via a web form, stored in SQLite
2. **Feature engineering** — productivity score calculated using a weighted formula across 5 variables
3. **Correlation analysis** — Pandas finds which habits most strongly correlate with productivity
4. **Prediction** — Linear Regression model predicts tomorrow's score based on recent patterns
5. **Insights generation** — correlations are translated into plain English, actionable insights

---

## Running locally

```bash
git clone https://github.com/nandanavinesh/nudge.git
cd nudge
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`

---

## Project structure

nudge/
├── app.py              # Flask server and API routes
├── database.py         # SQLite setup and queries
├── ml.py               # ML pipeline — scoring, correlation, prediction
├── requirements.txt
├── templates/
│   ├── index.html      # Log Today page
│   └── dashboard.html  # Dashboard page
└── static/
├── style.css
├── script.js        # Log form logic
└── dashboard.js     # Chart rendering and insights


---

## Built by

Nandana Vinesh — B.Tech CSE, VIT Chennai  
[LinkedIn](https://linkedin.com/in/nandanavinesh) · [GitHub](https://github.com/nandanavinesh)
