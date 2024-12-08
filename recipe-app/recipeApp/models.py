from django.contrib.auth.models import User
from django.db import models

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True, blank=True)
    short_desc = models.CharField(max_length=500)
    ingred_html = models.TextField()
    desc_html = models.TextField()
    additional_html = models.TextField(null=True, blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite_recipes', blank=True)

    def __str__(self):
        return self.name
