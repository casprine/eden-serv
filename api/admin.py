from django.contrib import admin
from api.models import Book, Author, Publication

admin.site.register((Book, Author, Publication, ))
