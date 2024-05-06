from django.shortcuts import render
from rest_framework import generics
from assetapi.models import Asset
from assetapi.serializers import AssetSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class AssetApis(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializers

    def delete(self, request, *args, **kwargs):
        queryset = Asset.objects.all().delete()
        serializer_class = AssetSerializers
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssetRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializers
    lookup_field = "pk"


class AssetApiView(APIView):

    def get(self, request, assetType, **kwargs):

        if assetType:
            assets = Asset.objects.filter(assetType=assetType)
        else:
            assets = Asset.objects.all()

        assetSerializer = AssetSerializers(assets, many=True)
        return Response(assetSerializer.data, status=status.HTTP_200_OK)

