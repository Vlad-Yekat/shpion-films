from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

from core.models import Movie, Review, Actor
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer
from .serializers import CreateRatingSerializer, ActorListSerializer, ActorDetailSerializer


class MovieListView(APIView):
    serializer_class = MovieListSerializer

    def get(self, request):
        data = Movie.objects.filter(is_published=True).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__user=request.user))
            ).annotate(
            rating_all=models.Sum(models.F("ratings__star"))/models.Count(models.F("ratings"))
        )

        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    serializer_class = MovieDetailSerializer

    def get(self, request, pk):
        data = Movie.objects.get(id=pk)
        serializer = self.serializer_class(data)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    serializer_class = ReviewCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class AddRatingView(APIView):
    serializer_class = CreateRatingSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ActorListView(generics.ListAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailView(generics.RetrieveAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
