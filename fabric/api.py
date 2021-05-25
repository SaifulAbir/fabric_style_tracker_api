from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from fabric.models import Fabric, FabricComposition, FabricType
from fabric.serializers import FabricSerializer, SupplierSerializer, FabricCompositionSerializer, FabricTypeSerializer, \
    FabricListSerializer
from supplier.models import Supplier


class FabricCreateAPI(CreateAPIView):
    serializer_class = FabricSerializer


class FabricUpdateAPI(UpdateAPIView):
    queryset = Fabric.objects.all()
    serializer_class = FabricSerializer


class FabricListAPI(ListAPIView):
    queryset = Fabric.objects.filter(
        is_archived=False
    )
    serializer_class = FabricListSerializer

class SupplierListAPI(ListAPIView):
    queryset = Supplier.objects.filter(
        is_archived=False
    )
    serializer_class = SupplierSerializer

class FabricCompositionListAPI(ListAPIView):
    queryset = FabricComposition.objects.filter(
        is_archived=False
    )
    serializer_class = FabricCompositionSerializer

class FabricTypeListAPI(ListAPIView):
    queryset = FabricType.objects.filter(
        is_archived=False
    )
    serializer_class = FabricTypeSerializer