from rest_framework import serializers

from core.models import Movie, Review, Rating, Actor


class MovieListSerializer(serializers.ModelSerializer):
    rating_user = serializers.BooleanField()
    rating_all = serializers.FloatField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'rating_user', 'rating_all')


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'description', 'image')


class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


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
    actors = ActorDetailSerializer(many=True, read_only=True)
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
