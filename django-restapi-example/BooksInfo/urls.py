from django.urls import path
from BooksInfo.views import BlogPostListCreate, BlogPostRetriveUpdateDestroy, BlogPostAPIView

urlpatterns = [
    path("blogposts/", BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogpost/<int:pk>/", BlogPostRetriveUpdateDestroy.as_view(), name="update-delete blogpost"),
    path("blogpost/<title>/", BlogPostAPIView.as_view(), name="get by title")
]
