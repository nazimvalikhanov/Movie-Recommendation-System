# 🎬 Movie Recommendation System

This project is a **hybrid movie recommendation system** that combines  
**Content-Based Filtering** (using TF-IDF & Cosine Similarity) and  
**Collaborative Filtering** (using ALS from the Implicit library) to suggest movies based on user preferences.

---

## Tech Stack Used in This Project

- Python (`Pandas`, `NumPy`, `Scikit-learn`, `Implicit`, `Streamlit`)
- NLP: TF-IDF Vectorizer, Cosine Similarity
- Collaborative Filtering: ALS (Alternating Least Squares)
- Pickle (for model saving/loading)
- Streamlit (for UI deployment)

---

## Data & Models

> ⚠️ Due to GitHub's file size limit, some large files such as `movies.csv` and `tfidf_model.pkl` are not included here.  
> If needed, they can be shared upon request or made accessible via an external link.

---

## Project Structure

```bash
├── app.py                              # Streamlit interface
├── movie_recommendation_system.ipynb  # Core logic notebook
├── requirements.txt                   # Required packages
├── models/
│   └── tfidf_model.pkl                # ❌ Not uploaded (too large)
├── data/
│   └── movies.csv                     # ❌ Not uploaded (too large)
```

---

## Features

- Search any movie title
- Generate top N movie recommendations based on:
   - Similar movie content (TF-IDF + cosine similarity)
   - User preferences (ALS collaborative filtering)
- Lightweight and interactive Streamlit UI

---

## How to Run Locally

### Clone the repository
git clone https://github.com/nazimvalikhanov/Movie-Recommendation-System.git

### Navigate into the project folder
cd Movie-Recommendation-System

### Install dependencies
pip install -r requirements.txt

### Launch the Streamlit app
streamlit run app.py

---

## Author

**Nazim Valikhanov**  
📧 nazim.valikhanov@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/nazim-valikhanov)

## License
This project is open source and available under the MIT License.
