from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.libraries.models import Library, LibraryType
from apps.libraries.serializers import LibrarySerializer, LibraryTypeSerializer


class LibraryTypeViewSet(ListModelMixin, GenericViewSet):
    queryset = LibraryType.objects.all()
    serializer_class = LibraryTypeSerializer


class LibraryViewSet(ListModelMixin, GenericViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
