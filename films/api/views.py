from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core.models import Movie, Review
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer


class MovieListView(APIView):
    serializer_class = MovieListSerializer

    def get(self, request):
        data = Movie.objects.all()
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
