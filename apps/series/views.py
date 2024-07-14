from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.series.models import Series
from apps.series.serializers import SeriesSerializer


class SeriesViewSet(ListModelMixin, GenericViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
