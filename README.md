# Movie Recommender App

A Flask-based movie recommendation system that uses machine learning to suggest movies based on user preferences, actor/director searches, and description similarities.

## Features

- 🎬 **Smart Recommendations** - Get movie suggestions based on:
  - Movie title similarity
  - Actor/Director search
  - Description-based similarity matching
  - Top popular movies fallback

- 🎨 **Movie Posters** - Fetch and display high-quality movie posters from TMDB API

- 👤 **User Authentication** - Sign up and login with secure password hashing using bcrypt

- 📊 **Search History** - Keep track of your search history and previous recommendations

- 🔍 **Multi-stage Search** - Intelligent search pipeline with multiple fallback strategies

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL
- **ML/Data**: scikit-learn, pandas, numpy
- **Authentication**: bcrypt
- **API**: TMDB (The Movie Database)
- **Server**: Gunicorn

## Installation

### Prerequisites

- Python 3.8+
- MySQL Server running locally
- TMDB API Key (free from https://www.themoviedb.org/settings/api)

### Setup

1. **Clone the repository**

```bash
cd "d:\Movie Recomender app"
```

2. **Create and activate virtual environment**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
.venv\Scripts\activate.bat  # Windows CMD
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
   Create a `.env` file in the project root:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=movie_app
TMDB_API_KEY=your_tmdb_api_key
```

5. **Set up the database**

```sql
CREATE DATABASE movie_app;

USE movie_app;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    query VARCHAR(255) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES users(username)
);
```

## Running the App

```bash
.venv\Scripts\python app.py
```

The app will be available at: **http://localhost:5000**

## Project Structure

```
Movie Recomender app/
├── app.py                 # Main Flask application
├── auth.py               # User authentication (signup/login)
├── db.py                 # Database connection
├── recommender.py        # ML-based recommendation engine
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not in git)
├── data/                 # Movie dataset CSV files
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
├── models/               # Pre-trained ML models
│   ├── movies.pkl
│   ├── embeddings.pkl
│   ├── vectorizer.pkl
│   ├── vectors.pkl
│   └── poster_cache.json
├── notebooks/            # Jupyter notebooks
│   └── recommender_training.ipynb
├── static/               # Static files
│   ├── style.css
│   ├── logo.png
│   └── no_poster.png
└── templates/            # HTML templates
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    └── movie_details.html
```

## How It Works

### Recommendation Pipeline

1. **Actor/Director Search** - Searches cast and director names
2. **Title-based Recommendation** - Fuzzy matching on movie titles
3. **Description Similarity** - TF-IDF vectorization and cosine similarity
4. **Top Movies Fallback** - Shows popular movies if no matches found

### Features in Detail

- **Fuzzy Matching** - Handles typos and close matches
- **Cache System** - Caches movie posters to reduce API calls
- **Session Management** - Tracks user sessions and search history
- **Guest Mode** - Users can browse without login

## Configuration

### Environment Variables

| Variable       | Description    | Default                |
| -------------- | -------------- | ---------------------- |
| `DB_HOST`      | MySQL host     | `localhost`            |
| `DB_USER`      | MySQL username | `root`                 |
| `DB_PASSWORD`  | MySQL password | (required)             |
| `DB_NAME`      | Database name  | `movie_app`            |
| `TMDB_API_KEY` | TMDB API key   | (required for posters) |

## Troubleshooting

### No Posters Displaying

- Ensure `TMDB_API_KEY` is set in `.env`
- Clear `models/poster_cache.json` to force refresh
- Check API key validity at https://www.themoviedb.org/settings/api

### Database Connection Error

- Verify MySQL is running
- Check credentials in `.env`
- Ensure database and tables are created

### scikit-learn Version Warning

- Model was trained with v1.2.2, current version may differ
- This is a compatibility warning and won't affect functionality

## License

This project is open source and available for educational purposes.

## Author

Movie Recommender App - 2024
