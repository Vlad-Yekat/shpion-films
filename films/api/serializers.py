from rest_framework import serializers

from core.models import Movie, Review


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'description')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('author', 'text')


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    rubric = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


