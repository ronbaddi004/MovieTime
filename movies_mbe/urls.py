from django.urls import path
from movies_mbe.views import MovieListView, MovieDeleteView, MovieCreateView, MovieUpdateView
from movies_mbe.views import ShowtimeListView, ShowtimeCreateView, ShowtimeUpdateView, ShowtimeDeleteView

urlpatterns = [
    path('', MovieListView.as_view(), name="movies-list"),
    path('movies/add', MovieCreateView.as_view(), name="movie-create"),
    path('movies/<int:id>', MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:id>/delete', MovieDeleteView.as_view(), name='movie-delete'),

    path('showtimes/<int:movie_id>/', ShowtimeListView.as_view(), name='showtime-list'),
    path('showtimes/<int:movie_id>/add/', ShowtimeCreateView.as_view(), name='showtime-create'),
    path('showtimes/<int:movie_id>/<int:id>', ShowtimeUpdateView.as_view(), name='showtime-update'),
    path('showtimes/<int:movie_id>/<int:id>/delete', ShowtimeDeleteView.as_view(), name='showtime-delete')
]
