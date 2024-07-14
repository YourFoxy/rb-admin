from django.contrib import admin

from apps.books.models import Book
from apps.series.models import Series


class BookStackedInline(admin.StackedInline):
    model = Book
    fields = ("name", "description")
    extra = 0

    def has_add_permission(self, request, obj):
        return False


@admin.register(Series)
class SeriesTypeAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_display = ("name",)

    inlines = (BookStackedInline,)
