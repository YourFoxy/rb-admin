from django.db import models


class Series(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
