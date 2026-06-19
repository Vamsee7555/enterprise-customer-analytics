# IMDb Movie Recommendation System Using Storylines

## Project Overview

This project is a Content-Based Movie Recommendation System that recommends similar movies based on their storylines. The system uses Natural Language Processing (NLP) techniques and Cosine Similarity to identify movies with similar plot descriptions.

The recommendation engine helps users discover movies that match their interests based on movie content rather than ratings or popularity.

---

## Features

* Movie recommendation based on storyline similarity
* Content-based filtering approach
* Interactive movie search
* Fast recommendation generation
* IMDb movie dataset integration
* User-friendly interface

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Streamlit
* Pickle

---

## Dataset

Dataset used:

* imdb_movies_2024.csv

Main attributes:

* Movie Title
* Storyline / Overview
* Genre
* Rating
* Release Year

---

## Project Structure

```text
IMDb Movie Recommendation/
│
├── imdb_movies_2024.csv
├── recommendation.py
├── app.py
├── movie_similarity.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Methodology

### Data Preprocessing

* Removed missing values
* Cleaned text data
* Converted storyline text into numerical vectors

### Feature Extraction

TF-IDF Vectorization was used to convert movie storylines into numerical representations.

### Similarity Calculation

Cosine Similarity was used to measure similarity between movies.

### Recommendation Generation

When a user selects a movie, the system finds the most similar movies based on storyline content.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Vamsee7555/imdb-movie-recommendation-system.git
```

Navigate to the project folder:

```bash
cd imdb-movie-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Sample Output

Input Movie:

```text
Inception
```

Recommended Movies:

```text
Interstellar
Shutter Island
The Prestige
Memento
Tenet
```

---

## Business Applications

* OTT Platforms
* Streaming Services
* Movie Discovery Systems
* Personalized Entertainment Recommendations

---

## Future Enhancements

* Hybrid Recommendation System
* User Rating Integration
* Collaborative Filtering
* Deep Learning Models
* Real-Time Recommendations

---

## Conclusion

The IMDb Movie Recommendation System successfully recommends similar movies using storyline-based content filtering. The project demonstrates the practical application of Natural Language Processing and Machine Learning in recommendation systems.

---

## Author

Vamsee Krishna M
