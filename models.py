from django.db import models


class Book(models.Model):
    # Field to store the title of the book
    title = models.CharField(max_length=100)

    # Field to store the author of the book
    author = models.CharField(max_length=100)

    # Field to store the publication date of the book
    publication_date = models.DateField()

    # Field to store the genre of the book
    genre = models.CharField(max_length=50)

    # Field to store the price of the book
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # Add other fields as needed
