from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookAPITest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="Book1", author="Author1", published_year=2021)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Book1", response.content.decode())

    def test_create_book(self):
        data = {"title": "Book2", "author": "Author2", "published_year": 2022}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Book.objects.filter(title="Book2").exists())

    def test_get_book_detail(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Book1", response.content.decode())

    def test_update_book(self):
        data = {"title": "Book1 Updated", "author": "Author1", "published_year": 2021}
        response = self.client.put(f'/api/books/{self.book.id}/update/', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Book1 Updated")

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_import_books(self):
        data = {"query": "python"}
        response = self.client.post('/api/books/import/', data)
        self.assertIn(response.status_code, [200, 201, 400])

    def test_report_books_by_year(self):
        response = self.client.get('/api/books/report/year/')
        self.assertEqual(response.status_code, 200)