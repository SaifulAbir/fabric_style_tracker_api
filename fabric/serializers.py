from rest_framework.serializers import ModelSerializer
from fabric.models import Fabric


class FabricSerializer(ModelSerializer):
    class Meta:
        model = Fabric
        fields = "__all__"