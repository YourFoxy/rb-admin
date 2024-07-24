from rest_framework import serializers

from apps.books.models import Book, BookPhoto, Criterion, Provenention
from apps.series.models import Series
from apps.libraries.serializers import LibrarySerializer


class CriterionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterion
        fields = (
            "id",
            "name",
        )


class ProvenentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provenention
        fields = ("id", "name", "description", "photo")


class BookPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPhoto
        fields = ("photo",)


class BaseSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("id", "name", "description", "photo")


class BaseBookSerializer(serializers.ModelSerializer):
    libraries = LibrarySerializer(many=True)
    criterion = CriterionSerializer()
    provenentions = ProvenentionSerializer(many=True)
    photos = BookPhotoSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "description",
            "entered_at",
            "inventory_number",
            "presenter",
            "libraries",
            "criterion",
            "provenentions",
            "main_photo",
            "photos",
            "language",
            "copies",
        )


class BookSerializer(BaseBookSerializer):
    series = BaseSeriesSerializer(read_only=True)

    class Meta(BaseBookSerializer.Meta):
        fields = BaseBookSerializer.Meta.fields + ("series",)
