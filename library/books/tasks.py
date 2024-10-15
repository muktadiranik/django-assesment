from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now
from .models import Book


@shared_task
def archive_old_books():
    ten_years_ago = now().date() - timedelta(days=10*365)
    books = Book.objects.filter(
        published_date__lt=ten_years_ago, is_archived=False)
    books.update(is_archived=True)
