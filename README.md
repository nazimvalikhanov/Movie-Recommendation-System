# 🎬 Movie Recommendation System

This project is a **hybrid movie recommendation system** that combines **Content-Based Filtering** (using TF-IDF & Cosine Similarity) and **Collaborative Filtering** (using ALS from Implicit library) to suggest movies based on user preferences.

---

## 📁 Project Structure

Movie-Recommendation-System/
│
├── app/
│ └── app.py ← Streamlit web app interface
├── notebooks/
│ └── movie_recommendation_system.ipynb ← main notebook
├── data/
│ └── movies.csv, ratings.csv ← datasets
├── models/
│ └── als_model.pkl, tfidf_model.pkl ← trained models
├── requirements.txt ← list of required packages
└── README.md ← this file


---

## 🧠 Key Features
- **Content-Based Filtering** using TF-IDF vectorization and cosine similarity
- **Collaborative Filtering** using ALS (Alternating Least Squares) from Implicit
- `fuzzywuzzy` for fuzzy title matching
- Saved models with `pickle`
- Deployed via **Streamlit interface**

---

## 📊 Dataset
- Source: [MovieLens Dataset - GroupLens](https://grouplens.org/datasets/movielens/)
- Files used: `movies.csv`, `ratings.csv`

---

## 💻 Tech Stack
- Python
- pandas, numpy, scikit-learn
- fuzzywuzzy
- implicit
- scipy
- Streamlit

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

---

## 📬 Author

**Nazim Valikhanov**  
📧 nazim.valikhanov@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/nazim-valikhanov)
