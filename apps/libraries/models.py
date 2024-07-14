from django.db import models


class LibraryType(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    type = models.ForeignKey(LibraryType, on_delete=models.PROTECT, related_name="libraries")

    def __str__(self):
        return self.name
