from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import MovieListView, MovieDetailView


urlpatterns = [
    path('list/', MovieListView.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailView.as_view(), name='movie-detail')
]
