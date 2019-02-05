from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from api.models import Book, Author, Publication


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publication = PublicationSerializer()

    class Meta:
        model = Book
        fields = '__all__'


@api_view(['GET'])
def get_featured(request):
    featured_books = Book.objects.filter(is_featured=True)
    data = BookSerializer(featured_books, many=True).data
    return Response(data)
