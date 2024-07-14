from django.contrib import admin

from apps.libraries.models import Library, LibraryType


@admin.register(LibraryType)
class LibraryTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_filter = ("type",)
    list_display = ("name", "type")
