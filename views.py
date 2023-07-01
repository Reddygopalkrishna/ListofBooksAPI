from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    # Define the viewset for the Book model
    queryset = Book.objects.all()
    # Set the queryset to retrieve all Book objects
    serializer_class = BookSerializer
    # Use the BookSerializer for serialization and deserialization

# Additional viewset code can be added here
