import numpy as np
import pandas as pd

movies = pd.read_csv('movies.csv',sep=';',encoding='latin-1').drop('Unnamed: 3',axis=1)
print('Shape of this dataset :',movies.shape)
movies.head()

ratings = pd.read_csv('ratings.csv',sep=';')
print('Shape of this dataset :',ratings.shape)
ratings.head()

users = pd.read_csv('users.csv',sep=';')
print('Shape of this dataset :',users.shape)
users.head()

"""### **Types of Recommendation System :**

<div align='center'><img src='https://miro.medium.com/max/998/1*O_GU8xLVlFx8WweIzKNCNw.png'></div>

<b>1) Content-Based Recommendation System :</b> It is a type of recommendation system which works on the principle of similar content. If a user is watching a movie, then the system will check about other movies of similar content or the same genre of the movie the user is watching. There are various fundamentals attributes that are used to compute the similarity while checking about similar content.

<b>2) Collaborative Filtering :</b> It is considered to be one of the very smart recommender systems that work on the similarity between different users and also items that are widely used as an e-commerce website and also online movie websites. It checks about the taste of similar users and does recommendations.

##### I will used first Collaborative Filtering and then Content Based Filtering to build the same Recommendation Engine.

<div align='center'><img src='https://miro.medium.com/max/1313/1*Qkv3n2Wt9xBmvel_Ee9QGA.png'></div>

## **Recommendation System using Collaborative Filtering**

##### This Recommendation System will works like "people who watching and like this movie also watch and like that movies".

#### **Pivot Table with respect to ratings given by users to movies**
"""

rating_pivot = ratings.pivot_table(values='rating',columns='userId',index='movieId').fillna(0)
print('Shape of this pivot table :',rating_pivot.shape)
rating_pivot.head()

"""#### **Machine Learning Model training for Recommending movies based on users ratings.**"""

from sklearn.neighbors import NearestNeighbors
nn_algo = NearestNeighbors(metric='cosine')
nn_algo.fit(rating_pivot)

"""#### **Developing the class of Collaborative filtering Recommendation Engine**"""

class Recommender:
    def __init__(self):
        # This list will stored movies that called atleast ones using recommend_on_movie method
        self.hist = []
        self.ishist = False # Check if history is empty

    # This method will recommend movies based on a movie that passed as the parameter
    def recommend_on_movie(self,movie,n_reccomend = 5):
        self.ishist = True
        movieid = int(movies[movies['title']==movie]['movieId'])
        self.hist.append(movieid)
        distance,neighbors = nn_algo.kneighbors([rating_pivot.loc[movieid]],n_neighbors=n_reccomend+1)
        movieids = [rating_pivot.iloc[i].name for i in neighbors[0]]
        recommeds = [str(movies[movies['movieId']==mid]['title']).split('\n')[0].split('  ')[-1] for mid in movieids if mid not in [movieid]]
        return recommeds[:n_reccomend]

    # This method will recommend movies based on history stored in self.hist list
    def recommend_on_history(self,n_reccomend = 5):
        if self.ishist == False:
            return print('No history found')
        history = np.array([list(rating_pivot.loc[mid]) for mid in self.hist])
        distance,neighbors = nn_algo.kneighbors([np.average(history,axis=0)],n_neighbors=n_reccomend + len(self.hist))
        movieids = [rating_pivot.iloc[i].name for i in neighbors[0]]
        recommeds = [str(movies[movies['movieId']==mid]['title']).split('\n')[0].split('  ')[-1] for mid in movieids if mid not in self.hist]
        return recommeds[:n_reccomend]

"""<br>

<div align='center'><img src='https://miro.medium.com/max/792/1*P63ZaFHlssabl34XbJgong.jpeg'></div>

## **Recommendation System using Content Based Filtering**

##### This Recommendation System will works like "This movies are similar to the movie you recently watched".

#### **Vectorization of contents of movies**
"""