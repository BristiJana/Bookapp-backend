# BookApp Backend

This is the Django REST API backend for BookApp. It provides endpoints for managing books, importing from Google Books, and generating reports.

## Prerequisites

- Python 3.10+
- PostgreSQL
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

## Setup

1. **Clone the repository**

   ```sh
   git clone <repo-url>
   cd bookapp
   ```

2. **Create and activate a virtual environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Edit `.env` with your database credentials and Google Books API base URL:

   ```
   DB_NAME=bookdb
   DB_USER=postgres
   DB_PASSWORD=yourpassword
   DB_HOST=localhost
   DB_PORT=5432
   GOOGLE_BOOKS_API=https://www.googleapis.com/books/v1/volumes?q=
   ```

5. **Create the database**

   Make sure PostgreSQL is running and create the database if it doesn't exist:

   ```sh
   psql -U postgres
   CREATE DATABASE bookdb;
   ```

6. **Apply migrations**

   ```sh
   python manage.py migrate
   ```

## Running the Application

Start the development server:

```sh
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`.

## API Endpoints

- `GET /api/books/` — List all books
- `POST /api/books/create/` — Create a new book
- `GET /api/books/<id>/` — Get book details
- `PUT /api/books/<id>/update/` — Update a book
- `DELETE /api/books/<id>/delete/` — Delete a book
- `POST /api/books/import/` — Import books from Google Books API
- `GET /api/books/report/year/` — Get books grouped by year

## Testing

Run tests with:

```sh
python manage.py test
```

## Admin Panel

Create a superuser to access Django admin:

```sh
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/`.

##
