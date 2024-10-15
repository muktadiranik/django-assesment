from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books")
    published_date = models.DateField()
    genre = models.CharField(max_length=255)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
