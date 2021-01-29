from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

from core.models import Movie, Review, Actor
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer
from .serializers import CreateRatingSerializer, ActorListSerializer, ActorDetailSerializer


class MovieListView(generics.ListAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        data = Movie.objects.filter(is_published=True).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__user=self.request.user))
            ).annotate(
            rating_all=models.Sum(models.F("ratings__star"))/models.Count(models.F("ratings"))
        )
        return data


class MovieDetailView(generics.RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer


class AddRatingView(generics.CreateAPIView):
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ActorListView(generics.ListAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailView(generics.RetrieveAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
