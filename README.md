# Movie Recommendation System

A content-based movie recommender web app built with Python and Streamlit. Enter a movie you like and get 5 similar movie recommendations with posters fetched from TMDB API.

## 🚀 Demo

> Run locally using the steps below.

---

## 📌 Features

- 🔍 Search from 5000+ movies
- 🎯 Content-based filtering using cosine similarity
- 🖼️ Fetches movie posters via TMDB API
- ⚡ Fast and interactive UI with Streamlit

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Core language |
| Streamlit | Web UI |
| Pandas | Data processing |
| Scikit-learn | Cosine similarity |
| TMDB API | Fetching movie posters |
| Pickle | Storing processed data |

---

## 📂 Project Structure

```
Movies-Recommendation-System/
│
├── app.py                  # Main Streamlit app
├── movies_dict.pkl         # Processed movies data
├── similarity.pkl          # Cosine similarity matrix (not pushed to GitHub)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/NIKHILPATIL1508/Movies-Recommendation-System.git
cd Movies-Recommendation-System
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your TMDB API Key
Get a free API key from [https://www.themoviedb.org/](https://www.themoviedb.org/) and replace it in `app.py`:
```python
response = requests.get(
    'https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY'.format(movie_id)
)
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 📊 How It Works

1. Movie data is preprocessed and vectorized using **Bag of Words**
2. **Cosine Similarity** is computed between all movies
3. When a movie is selected, the top 5 most similar movies are returned
4. Movie posters are fetched in real-time from the **TMDB API**

---

## 📦 Dataset

- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle

---

## ⚠️ Note

The `similarity.pkl` file exceeds GitHub's 100MB limit and is not included in this repository.  
You can generate it by running the preprocessing notebook locally.

---

## 🙋‍♂️ Author

**Nikhil Patil**  
GitHub: [@NIKHILPATIL1508](https://github.com/NIKHILPATIL1508)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).