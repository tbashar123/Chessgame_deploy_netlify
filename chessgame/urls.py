from django.urls import path, include


urlpatterns = [
    path('', include('chess.urls')),
    # Add more URL patterns as needed
]
