from django.contrib import admin
from django.urls import path, include
from .views import MovieListView, MovieDetailView, ReviewCreateView
from .views import AddRatingView

urlpatterns = [
    path('movie/', MovieListView.as_view()),
    path('movie/<int:pk>', MovieDetailView.as_view()),
    path('review/', ReviewCreateView.as_view()),
    path('rating/', AddRatingView.as_view()),
]
