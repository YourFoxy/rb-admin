from django.db import models

from apps.libraries.models import Library
from apps.series.models import Series


class Criterion(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Provenention(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Book(models.Model):
    class Language(models.TextChoices):
        RU = "ru"
        EN = "en"

    name = models.TextField()
    description = models.TextField(blank=True)

    entered_at = models.DateTimeField(blank=True, null=True)
    inventory_number = models.TextField(blank=True)
    presenter = models.TextField(blank=True)

    libraries = models.ManyToManyField(Library, related_name="books")
    criterion = models.ForeignKey(Criterion, on_delete=models.PROTECT, related_name="books")
    provenentions = models.ManyToManyField(Provenention, blank=True, related_name="books")

    main_photo = models.ImageField(blank=True)

    language = models.CharField(max_length=8, choices=Language.choices, default=Language.RU)

    copies = models.ManyToManyField("self", blank=True)
    series = models.ForeignKey(Series, blank=True, null=True, on_delete=models.SET_NULL, related_name="books")

    def __str__(self):
        return self.name


class BookPhoto(models.Model):
    photo = models.ImageField(blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="photos")
