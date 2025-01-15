## 🧠 How It Works

### Data Preprocessing
- Combines features like genres, keywords, cast, and overview into a single feature called tags.
- Removes stopwords and processes text data for better feature representation.

### TF-IDF Vectorization
- Uses TF-IDF Vectorizer to convert text data into numerical form, highlighting important features for each movie.

### Cosine Similarity Matrix
- Computes the similarity between movies based on their feature vectors using cosine similarity.

### Recommendation Logic
- Identifies the top 5 most similar movies for a selected movie using the similarity matrix.
- Fetches movie posters from the TMDB API based on movie IDs.

### Streamlit App
- Users select a movie from a dropdown menu, and recommendations are displayed with posters in a grid format.

## 📋 Prerequisites
- Python 3.7+
- TMDB API Key

## 🖥️ Deployment Instructions

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:

    ```bash
    streamlit run app.py
    ```

4. Open the app in your browser (usually at http://localhost:8501).

## 🎬 Demo

- Select a movie from the dropdown menu.
- View the top 5 recommended movies with their posters.

## 🌟 Future Enhancements
- Implement hybrid recommendations (content + collaborative filtering).
- Add additional details like trailers, ratings, and reviews.
- Enhance UI/UX for a better user experience.
