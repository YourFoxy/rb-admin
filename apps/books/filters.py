from django_filters import FilterSet

from apps.books.models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            "criterion": ["exact"],
            "libraries__id": ["exact"],
            "name": ["icontains"],
        }
