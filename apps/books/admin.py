from django.contrib import admin

from apps.books.models import Book, BookPhoto, Criterion, Provenention


@admin.register(Criterion)
class CriterionAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


class BookStackedInline(admin.StackedInline):
    model = Book.provenentions.through
    autocomplete_fields = ("book",)
    extra = 1


@admin.register(Provenention)
class ProvenentionAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_display = ("name",)

    inlines = (BookStackedInline,)


class BookPhotoStackedInline(admin.StackedInline):
    model = BookPhoto
    extra = 1


class CopyStackedInline(admin.StackedInline):
    model = Book.copies.through
    fk_name = "from_book"

    autocomplete_fields = ("to_book",)
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ("name", "description", "inventory_number", "presented_by")
    list_filter = ("entered_at", "criterion", "libraries", "language")
    list_display = ("name",)
    exclude = ("copies",)

    filter_horizontal = ("libraries", "provenentions")
    inlines = (BookPhotoStackedInline, CopyStackedInline)
    autocomplete_fields = ("criterion", "series")
