from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction
from ..models import Book
from ..serializers import BookSerializer
import requests


class BookDeleteView(APIView):
    """DELETE a book"""
    def delete(self, request, pk):
        with transaction.atomic():
            book = get_object_or_404(Book, pk=pk)
            book.delete()
            return Response({"message": "Book deleted"}, status=status.HTTP_204_NO_CONTENT)

