from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from BooksInfo.models import BlogPost
from BooksInfo.serializers import BlogPostSerializers
from rest_framework.views import APIView


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class BlogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    lookup_field = "pk"


class BlogPostAPIView(APIView):
    def get(self, request, title , **kwargs):

        if title:
            blogPost = BlogPost.objects.filter(title=title)
        else:
            blogPost = BlogPost.objects.all()

        serializers = BlogPostSerializers(blogPost, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
