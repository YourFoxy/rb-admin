from apps.books.serializers import BaseBookSerializer, BaseSeriesSerializer


class SeriesSerializer(BaseSeriesSerializer):
    books = BaseBookSerializer(many=True)

    class Meta(BaseSeriesSerializer.Meta):
        fields = BaseSeriesSerializer.Meta.fields + ("books",)
