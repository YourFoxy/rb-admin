from rest_framework import serializers

from apps.books.serializers import BookSerializer
from apps.series.models import Series


class SeriesSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Series
        fields = ("id", "name", "description", "photo", "books")
