from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name
