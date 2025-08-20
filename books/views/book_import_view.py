from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction
from ..models import Book
from ..serializers import BookSerializer
import requests
import os

class ImportBookView(APIView):
    """
    Import book data from Google Books API
    Example: POST /api/books/import/?q=python
    """
    def post(self, request):
        query = request.data.get("q", "Hamlet")
        base_url = os.getenv("GOOGLE_BOOKS_API","")
        url = f"{base_url}{query}"
        try:
            response = requests.get(url, timeout=10)
            data = response.json()

            imported = []
            with transaction.atomic():
                for item in data.get("items", []):
                    volume = item.get("volumeInfo", {})
                    title = volume.get("title", "Untitled")
                    author = ", ".join(volume.get("authors", ["Unknown"]))
                    published = volume.get("publishedDate", "2000")[:4]

                    book, created = Book.objects.get_or_create(
                        title=title,
                        defaults={"author": author, "published_year": published},
                    )
                    if created:
                        imported.append(title)

            return Response(
                {"imported": imported, "count": len(imported)},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


