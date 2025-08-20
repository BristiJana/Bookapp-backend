from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from ..models import Book
from collections import Counter

class BooksByYearView(APIView):
    """Report: Number of books grouped by published_year"""
    def get(self, request):
        with transaction.atomic():
            books = Book.objects.values_list("published_year", flat=True)
            year_counts = Counter(books)

        # ✅ Convert dict {2024: 1, 2025: 1} -> list of dicts [{year: 2024, total: 1}, ...]
        report = [{"published_year": year, "total": count} for year, count in year_counts.items()]

        # ✅ Sort by year (ascending)
        report = sorted(report, key=lambda x: x["published_year"])

        return Response(report, status=status.HTTP_200_OK)
