from django.urls import path
from .views import Home, ProfileList, ProfileCreate, MovieList, ShowMovieDetail,ShowMovie


app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name= 'home'),
    path('profile/', ProfileList.as_view(), name= 'profile_list'),
    path('profile/create/',ProfileCreate.as_view(),name= 'profile_create'),
    path('movies/<str:profile_id>/',MovieList.as_view(),name= 'movies_list'),
    path('movies/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name= 'movie_detail'),
    path('movies/play/<str:movie_id>/',ShowMovie.as_view(),name= 'play'),

]
