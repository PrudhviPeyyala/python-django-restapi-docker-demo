from rest_framework import serializers
from testapi.models import Bike


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ["id", "modelName", "manufacturer", "activeOrNot"]
