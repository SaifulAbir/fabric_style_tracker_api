from rest_framework.generics import CreateAPIView
from fabric.serializers import FabricSerializer


class FabricCreateAPI(CreateAPIView):
    serializer_class = FabricSerializer