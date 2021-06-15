from rest_framework import serializers

from api.models import Titles, Categories, Genres, Reviews, Comments, User


class TitlesSerializer(serializers.ModelSerializer):
    ...


class CategoriesSerializer(serializers.ModelSerializer):
    ...


class GenresSerializer(serializers.ModelSerializer):
    ...


class ReviewsSerializer(serializers.ModelSerializer):
    ...


class CommentsSerializer(serializers.ModelSerializer):
    ...


class UsersSerializer(serializers.ModelSerializer):
    """Serialization of users."""

    class Meta:
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        )
        model = User