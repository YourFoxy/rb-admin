from rest_framework import serializers

from apps.libraries.models import Library, LibraryType


class LibraryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryType
        fields = (
            "id",
            "name",
        )


class LibrarySerializer(serializers.ModelSerializer):
    type = LibraryTypeSerializer()

    class Meta:
        model = Library
        fields = ("id", "name", "description", "type", "photo")
