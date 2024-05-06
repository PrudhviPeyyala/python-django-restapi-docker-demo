from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from api.models import Book
from api.serializers import BookSerializer
from rest_framework.views import APIView


class BookViewListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def delete(self, request, *args, **kwargs):
        queryset = Book.objects.all().delete()
        serializer_class = BookSerializer
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class BookAPIView(APIView):

    def get(self, request, name, **kwargs):
        print(name)

        if name:
            book = Book.objects.filter(name=name)
        else:
            book = Book.objects.all()

        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
