from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router instance
router = DefaultRouter()

# Register the BookViewSet with the router
router.register(r'books', BookViewSet)

# Define the URL patterns
urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]
