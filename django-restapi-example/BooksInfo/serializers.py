from rest_framework import serializers
from BooksInfo.models import BlogPost


class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]
