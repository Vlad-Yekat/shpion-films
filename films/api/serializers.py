from rest_framework import serializers

from core.models import Movie, Review, Rating


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'description')


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class FilterReviewSerializer(serializers.ListSerializer):
    """ Only parents """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class ReviewSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Review
        fields = ('author', 'text', 'children')


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


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('star', 'movie', 'user')

    def create(self, validated_data):
        print(validated_data)
        rating = Rating.objects.update_or_create(
            user=validated_data.get('user', None),
            movie=validated_data.get('movie', None),
            defaults={'star': validated_data.get('star')}
        )
        return rating
