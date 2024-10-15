from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['author__name', 'genre', 'published_date']
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60*15), name="list")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.clear()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.clear()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.clear()
