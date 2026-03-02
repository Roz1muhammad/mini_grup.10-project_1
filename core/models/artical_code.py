from django.db import models
import uuid
from .user import *




class ArticleCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, unique=True)


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    thumbnail = models.ImageField(
        upload_to='articles/thumbnails/',
        default='articles/thumbnails/default.jpg'
    )

    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()

    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles'
    )