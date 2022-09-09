from django.urls import path
from .views import Home, MovieDetails, ProfileList, CreateProfile
from .views import MoviesList, IndexPage

app_name = 'core'

urlpatterns = [
    path('',IndexPage.as_view()),
    path('home/', Home.as_view(), name = 'home'),
    path('profile/', ProfileList.as_view(), name = 'profile_list'),
    path('profile/create', CreateProfile.as_view(), name = 'create_profile'),
    path('movies/<str:profile_id>/', MoviesList.as_view(), name = 'movies_list'),
    path('movies/info/<str:movie_id>/', MovieDetails.as_view(), name = 'movie_info'),
]