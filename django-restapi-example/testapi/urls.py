from django.urls import path
from testapi.views import BikeView, BikeRetrieveUpdateDestroy, BikeAPIView

urlpatterns = [
    path("bikeList/", BikeView.as_view(), name="get-all-bike-info"),
    path("bikeList/<int:pk>/", BikeRetrieveUpdateDestroy.as_view(), name="update-delete-bike-info"),
    path("bikeList/modelname/<modelName>", BikeAPIView.as_view(), name="bike with request param")
]
