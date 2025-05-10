# 🎬 Movie Recommendation System

This is a web-based movie recommendation system built using Python, Streamlit, and the K-Nearest Neighbors (KNN) algorithm. It recommends movies similar to a selected title based on collaborative filtering using the MovieLens dataset.

## 🚀 Features

- Recommend movies based on your favorite movie
- Streamlit-powered clean and interactive UI
- Fetches movie posters using TMDb API
- Built with scikit-learn, pandas, and KNN
- Lightweight and easy to deploy

## 🧠 How It Works

The recommendation engine uses KNN to find movies similar to the one selected by the user. It calculates similarity based on user rating patterns from the MovieLens dataset.

## 🛠️ Tech Stack

- Python
- scikit-learn
- pandas
- Streamlit
- TMDb API

## 📦 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/movie-recommender.git
    cd movie-recommender
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your TMDb API key in `app.py`:
    ```python
    TMDB_API_KEY = "your_actual_key"
    ```

4. Run the app:
    ```bash
    streamlit run app.py
    ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgements

- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [TMDb API](https://www.themoviedb.org/documentation/api)
