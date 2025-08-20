from django.urls import path
from books.views.book_create_view import  BookCreateView
from books.views.book_list_view import BookListView
from books.views.book_delete_view import BookDeleteView
from books.views.book_detail_view import BookDetailView
from books.views.book_update_view import BookUpdateView
from books.views.book_import_view import ImportBookView
from books.views.book_year_view import BooksByYearView


urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/create/", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
    path("books/import/", ImportBookView.as_view(), name="book-import"),
    path("books/report/year/", BooksByYearView.as_view(), name="books-by-year"),
]
