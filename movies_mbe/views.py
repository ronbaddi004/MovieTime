from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from movies_mbe.models import Movie, ShowTime
from movies_mbe.forms import MovieForm, ShowTimeForm


class MovieListView(ListView):
    model = Movie


class MovieCreateView(CreateView):
    form_class = MovieForm
    template_name = "movies_mbe/movie_create.html"
    model = Movie


class MovieUpdateView(UpdateView):
    form_class = MovieForm
    template_name = "movies_mbe/movie_update.html"
    # fields = ["name", "description", "released_date"]
    model = Movie

    def get_initial(self):
        instance = self.get_object()
        return instance.__dict__

    def get_object(self):
        return get_object_or_404(Movie, id=self.kwargs.get("id"))

    def put(self, *args: str, **kwargs):
        return super().put(*args, **kwargs)


class MovieDeleteView(DeleteView):
    template_name = "movies_mbe/movie_delete.html"
    model = Movie
    # success_url = '/movies'

    def get_object(self):
        return get_object_or_404(Movie, id=self.kwargs.get("id"))

    def get_success_url(self) -> str:
        return reverse('movies-list')


class ShowtimeListView(ListView):
    model = ShowTime

    def get_queryset(self):

        return super().get_queryset().filter(movie=self.kwargs.get("movie_id")).select_related("movie")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"movie": Movie.objects.get(id=self.kwargs.get("movie_id"))})
        return context


class ShowtimeCreateView(CreateView):
    form_class = ShowTimeForm
    template_name = "movies_mbe/showtime_create.html"
    model = ShowTime

    def post(self, request, *args: str, **kwargs):
        form = ShowTimeForm(request.POST or None)

        if form.is_valid():

            showtime_obj = ShowTime(movie_id=kwargs.get('movie_id'), **form.cleaned_data)

            showtime_obj.save()

            return redirect("showtime-list", movie_id=kwargs.get("movie_id"))

        return render(request, 'movie_mbe/showtime_create.html', {'form': form})


class ShowtimeUpdateView(UpdateView):
    form_class = ShowTimeForm
    template_name = "movies_mbe/showtime_update.html"
    model = ShowTime

    def get_initial(self):
        instance = self.get_object()
        return instance.__dict__

    def get_object(self):
        return get_object_or_404(ShowTime, id=self.kwargs.get("id"))

    def put(self, *args: str, **kwargs):
        return super().put(*args, **kwargs)


class ShowtimeDeleteView(DeleteView):
    template_name = "movies_mbe/showtime_delete.html"
    model = ShowTime
    # success_url = '/movies'

    def get_object(self):
        return get_object_or_404(ShowTime, id=self.kwargs.get("id"))

    def get_success_url(self) -> str:
        return reverse('showtime-list', kwargs={"movie_id":self.kwargs.get("movie_id")})
