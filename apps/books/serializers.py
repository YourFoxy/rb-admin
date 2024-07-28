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
            "main_photo",
            "photos",
            "language",
            "copies",
        )


class BaseProvenentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provenention
        fields = ("id", "name", "description", "photo")


class ProvenentionSerializer(serializers.ModelSerializer):
    books = BaseBookSerializer(many=True)

    class Meta:
        model = Provenention
        fields = ("id", "name", "description", "photo", "books")


class BookWithProvenentionSerializer(BaseBookSerializer):
    provenentions = BaseProvenentionSerializer(many=True)

    class Meta(BaseBookSerializer.Meta):
        model = Book
        fields = BaseBookSerializer.Meta.fields + ("provenentions",)


class BookSerializer(BookWithProvenentionSerializer):
    series = BaseSeriesSerializer(read_only=True)

    class Meta(BookWithProvenentionSerializer.Meta):
        fields = BookWithProvenentionSerializer.Meta.fields + ("series",)
