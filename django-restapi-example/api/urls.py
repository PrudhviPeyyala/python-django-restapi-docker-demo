from api.views import BookViewListCreate, BookRetrieveUpdateDestroy, BookAPIView
from django.urls import path

urlpatterns = [
    path("api/", BookViewListCreate.as_view(), name="book-post-view"),
    path("api/<int:pk>", BookRetrieveUpdateDestroy.as_view(), name="update or delete book"),
    path("api/<name>", BookAPIView.as_view(), name="get-data")
]
