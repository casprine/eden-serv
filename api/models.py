from django.db import models
from taggit.managers import TaggableManager

MAX_NAME_LENGTH = 70
MAX_MEDIA_URL_LENGTH = 250
MAX_SHORT_DESCRIPTION_LENGTH = 300


class Author(models.Model):
    title = models.CharField(max_length=MAX_NAME_LENGTH)
    bio = models.TextField()
    avatar = models.CharField(max_length=MAX_MEDIA_URL_LENGTH)
    topics = TaggableManager()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=MAX_NAME_LENGTH)
    logo = models.CharField(max_length=MAX_MEDIA_URL_LENGTH)
    description = models.TextField()

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=MAX_NAME_LENGTH)
    cover = models.CharField(max_length=MAX_MEDIA_URL_LENGTH)
    short_description = models.CharField(
        max_length=MAX_SHORT_DESCRIPTION_LENGTH)
    full_description = models.TextField()
    publication = models.ForeignKey(
        Publication, related_name="books", on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE)
    publish_year = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
