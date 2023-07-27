# Movie Recommendation System

This is a movie recommendation system that currently provides users with two recommendation options:

1. **Movie Description Based Recommendation:** This option recommends movies based on the similarity of their descriptions or plot summaries using Cosine Similarity.

2. **Movie Meta Data Based Recommendation:** This option recommends movies based on their metadata, such as genres, actors, directors, etc.

In the future, I plan to add collaborative filtering to enhance the recommendation system further.

The system is developed using Django, a high-level Python web framework, to provide a user-friendly web interface for accessing the movie recommendations.

## How it Works

The movie recommendation system leverages the concept of Cosine Similarity to suggest similar movies to the user. Here's how it works for each recommendation option:

1. **Movie Description Based Recommendation:**
   - The system processes the movie descriptions and converts them into numerical vectors using text embedding techniques like TF-IDF (Term Frequency-Inverse Document Frequency).
   - When a user inputs a movie title or description, the system converts the input into a numerical vector.
   - It then calculates the cosine similarity between the input vector and the vectors of all the movies in the dataset.
   - The system recommends the top-5 movies with the highest cosine similarity scores as the most similar ones.

2. **Movie Meta Data Based Recommendation:**
   - The system processes the movie metadata, such as genres, actors, directors, etc., and creates binary feature vectors for each movie.
   - When a user selects a movie or preferences from various metadata options, the system converts the selection into a binary feature vector.
   - It then calculates the cosine similarity between the user's feature vector and the feature vectors of all the movies in the dataset.
   - The system recommends the top-5 movies with the highest cosine similarity scores as the most similar ones based on metadata.

## Collaborative Filtering (Future Enhancement)

In the future, I plan to integrate collaborative filtering into my movie recommendation system. Collaborative filtering is a popular recommendation technique that analyzes user behavior, such as past movie ratings and interactions, to identify patterns and make personalized recommendations.

Collaborative filtering will enable the system to recommend movies based on similarities between users' preferences. This approach can help discover movies that other users with similar tastes enjoyed, allowing for more accurate and personalized recommendations.

## Future Work

As I continue to improve and expand my movie recommendation system, here are some future enhancements and features I plan to implement:

1. **Collaborative Filtering:** Incorporate collaborative filtering to provide personalized movie recommendations based on user behavior and preferences.

2. **User Accounts:** Implement user account functionality to allow users to create profiles, save their preferences, and receive recommendations tailored to their individual tastes.

3. **Rating System:** Introduce a movie rating system where users can rate movies they have watched. These ratings will be used to improve the accuracy of the recommendations.

4. **Popular and Trending Movies:** Include a section that displays popular and trending movies based on overall user ratings and recent releases.

5. **Movie Trailers and Reviews:** Integrate movie trailers and reviews from external sources to provide users with more comprehensive information before deciding to watch a movie.

6. **Recommendation Refresh:** Implement a mechanism to periodically refresh the recommendation models with the latest movie data to ensure up-to-date and relevant suggestions.

## Contents of the Repository

The GitHub repository contains the following components:

1. **Recommendation Notebooks Folder: (Not Yet Added To Repository)**
   This folder contains Jupyter notebooks used for data preprocessing, generating movie embeddings, and calculating cosine similarity scores. The notebooks show how the Cosine Similarity approach is used for movie recommendations.
   Will add it soon.

2. **Django Web App:**
   The Django web app is the heart of the movie recommendation system. It provides a user-friendly interface where users can input movie titles or select movie preferences to get personalized movie recommendations.

## Getting Started

To set up the movie recommendation system on your local machine, follow these steps:

1. Clone this GitHub repository to your local machine.
2. Install the required Python dependencies by running `pip install -r requirements.txt`. (Currently not available in the repository)
3. Navigate to the Django web app directory and run `python manage.py runserver` to start the local development server.
4. Open your web browser and go to `http://localhost:8000/` to access the movie recommendation system.

## Contributing

Contributions to this movie recommendation system are welcome!

## 

Happy movie watching! 🍿🍿🎬🎬