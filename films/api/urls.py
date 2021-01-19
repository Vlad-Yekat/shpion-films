from django.contrib import admin
from django.urls import path, include
from .views import MovieListView, MovieDetailView, ReviewCreateView
from .views import AddRatingView, ActorListView, ActorDetailView

urlpatterns = [
    path('actors/', ActorListView.as_view()),
    path('actors/<int:pk>', ActorDetailView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('movies/<int:pk>', MovieDetailView.as_view()),
    path('review/', ReviewCreateView.as_view()),
    path('rating/', AddRatingView.as_view()),
]
