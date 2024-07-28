from apps.books.serializers import BookWithProvenentionSerializer, BaseSeriesSerializer


class SeriesSerializer(BaseSeriesSerializer):
    books = BookWithProvenentionSerializer(many=True)

    class Meta(BaseSeriesSerializer.Meta):
        fields = BaseSeriesSerializer.Meta.fields + ("books",)
