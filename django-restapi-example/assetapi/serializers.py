from rest_framework import serializers
from assetapi.models import Asset


class AssetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ["id", "assetType", "assetManufacturer", "assetModel"]
