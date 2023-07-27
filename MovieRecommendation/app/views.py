from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.recommendation import *

def homePage(request):
    movie = ""
    typeOfRecommendation = ""
    if request.method == 'POST':
        movie = request.POST.get('movie')
        typeOfRecommendation = request.POST.get('typeOfRecommendation')

    movie_ids = []
    imdb_ids = []
    
    if (movie != "" and typeOfRecommendation=="descriptionBased"):
        movie_ids, imdb_ids = description_based_recommendations(movie)
    elif (movie != "" and typeOfRecommendation=="dataBased"):
        movie_ids, imdb_ids = movie_data_based_recommendations(movie)

    poster_srcs = []
    imdb_srcs = []
    
    if (len(movie_ids) != 0):
        poster_srcs, imdb_srcs = get_poster_source(movie_ids, imdb_ids)

    ziplist = zip(poster_srcs, imdb_srcs)

    context = {
        'ziplist': ziplist
    }

    return render(request, 'home.html', context)
