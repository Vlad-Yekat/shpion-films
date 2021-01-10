from rest_framework import serializers

from core.models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    rubric = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'

