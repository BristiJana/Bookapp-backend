import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Book
from ..serializers import BookSerializer


class BookListView(APIView):
    """GET all books"""
    def get(self, request):
        books = Book.objects.all().order_by("-created_at")
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
