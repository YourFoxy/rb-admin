from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from apps.books.models import Book, Criterion, Provenention
from apps.books.serializers import BookSerializer, CriterionSerializer, ProvenentionSerializer


class CriterionViewSet(ListModelMixin, GenericViewSet):
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer


class ProvenentionViewSet(ListModelMixin, GenericViewSet):
    queryset = Provenention.objects.all()
    serializer_class = ProvenentionSerializer


class BookViewSet(ListModelMixin, GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ("criterion", "libraries__id")
