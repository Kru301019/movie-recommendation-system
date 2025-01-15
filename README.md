# 🎥End-to-End Movie Recommendation System  

A **Movie Recommendation System** that suggests movies based on a selected movie using **content-based filtering**. The system analyzes movie features like genres, keywords, and cast to recommend similar movies. The application is deployed using **Streamlit**, providing an interactive and user-friendly interface.

---

## 🚀 Features  

- **Content-Based Recommendations**  
   Recommends movies similar to the selected one by analyzing features like genres, keywords, and cast.  

- **Interactive Web App**  
   An intuitive web application built with **Streamlit**, allowing users to interact with the recommendation system.  

- **Movie Posters Integration**  
   Fetches and displays movie posters using the **TMDB API**, enhancing the visual experience.  

- **Top 5 Recommendations**  
   Displays the 5 most similar movies to the user's selection.

---

## 🛠️ Tech Stack  

- **Programming Language**: Python  
- **Libraries**:  
   - Machine Learning: `scikit-learn`, `nltk`  
   - Data Handling: `pandas`, `numpy`  
   - Web App Deployment: `Streamlit`  
   - Visualization: `matplotlib`, `seaborn`  
- **API**: TMDB API for fetching movie posters  
- **Data**: TMDB 5000 Movie Dataset  

---

## 📂 Project Structure  

```plaintext
├── app.py      # Streamlit app code
├──Movie-Content-Based-Recommender-System.ipynb # Jupyter notebook for developmentand   
├── similarity.pkl        # Precomputed cosine similarity matrix  
├── movies_dict.pkl       # Serialized movie data with features  
├── requirements.txt      # Python libraries required for the project  
└── README.md             # Project documentation  

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
