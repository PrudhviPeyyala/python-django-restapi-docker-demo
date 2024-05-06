from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from testapi.models import Bike
from testapi.serializers import BikeSerializer
from rest_framework.views import APIView

# Create your views here.
class BikeView(generics.ListCreateAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

    def delete(self, request, *args, **kwargs):
        Bike.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BikeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    lookup_field = "pk"


class BikeAPIView(APIView):
    def get(self, request, modelName ,format=None ):
        print(modelName)
        # modelName = request.query_params.get("modelName", "")

        if modelName:
            bikes = Bike.objects.filter(modelName = modelName)
        else:
            bikes = Bike.objects.all()

        bikeSerializer = BikeSerializer(bikes, many=True)
        return Response(bikeSerializer.data, status= status.HTTP_200_OK)

