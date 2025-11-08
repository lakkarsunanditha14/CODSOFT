# Task 3 - Food Recipe Recommendation System

 # overview
This project is part of the **CODSOFT Internship (Python Programming).  
The task is to build a **Food Recipe Recommendation System** that suggests similar dishes based on ingredients using machine learning (text similarity) techniques.

# Objective
The main goal of this project is to recommend similar recipes or dishes based on their ingredients.  
When a user enters a dish name (e.g., “Chicken Biryani”), the system finds and displays other dishes with similar ingredients.

# Technologies Used
- **Python**
- **Pandas**
- **Scikit-learn (sklearn)**
  - `TfidfVectorizer`
  - `cosine_similarity'.

# How It Works
1. A dataset of dishes and their ingredients is created.
2. The system converts ingredients into numerical form using **TF-IDF Vectorization**.
3. The **cosine similarity** metric is used to find how similar two dishes are based on their ingredients.
4. The user enters a dish name, and the system recommends other similar dishes.
