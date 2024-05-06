from django.urls import path
from assetapi.views import AssetApis, AssetRetrieveUpdateDestroy, AssetApiView

urlpatterns = [
    path("asset/", AssetApis.as_view(), name="asset get - post"),
    path("assetupdate/<int:pk>", AssetRetrieveUpdateDestroy.as_view(), name="asset update-delete"),
    path("assets/<assetType>", AssetApiView.as_view(), name="asset -all ")
]
