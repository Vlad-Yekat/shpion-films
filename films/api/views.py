from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer


class MovieListView(APIView):
    def get(self, request):
        data = Movie.objects.all()
        serializer = MovieListSerializer(data, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    def get(self, request, pk):
        data = Movie.objects.get(id=pk)
        serializer = MovieDetailSerializer(data)
        return Response(serializer.data)