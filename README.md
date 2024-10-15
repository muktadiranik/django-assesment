# Online Library System API

This is a Django-based REST API service that allows users to manage books and authors, including full CRUD operations for both models. It also features data filtering, background task processing using Celery, caching for optimized performance, and logging through Django signals.

## Features

- **Authors and Books Management:** Full CRUD for managing authors and books.
- **Filtering:** Allows filtering of books by author name, genre, and published date range.
- **Background Tasks:** Archives books older than 10 years every 30 minutes using Celery.
- **Signals:** Automatically logs book creation and deletion events.
- **Optimized Queries:** Uses `select_related` and `prefetch_related` to optimize database queries.
- **Caching:** Caches the book list endpoint for improved performance, with automatic cache invalidation.
- **JWT Authentication:** Token-based authentication for secure access to API endpoints.

---

## Requirements

- Python 3.8+
- Django 3.2+
- Django Rest Framework
- Celery
- Redis (for task scheduling and caching)
- Postman (optional for API testing)

---

## Instructions

```bash
git clone https://github.com/muktadiranik/django-assesment.git
cd library
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
celery -A library worker --loglevel=info
celery -A library beat --loglevel=info
```

---

## API Endpoints

Authors

    GET /authors/: Get all authors.
    POST /authors/: Create a new author.
    PUT /authors/{id}/: Update an author.
    DELETE /authors/{id}/: Delete an author.

Books

    GET /books/: Get all books (includes filtering and caching).
    POST /books/: Create a new book.
    PUT /books/{id}/: Update a book.
    DELETE /books/{id}/: Delete a book.
