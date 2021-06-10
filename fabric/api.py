from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from fabric.models import Fabric, FabricComposition, FabricType, FiberPercentage, Fiber
from fabric.serializers import FabricSerializer, FabricCompositionSerializer, FabricTypeSerializer, \
    FabricListSerializer, FiberPercentageSerializer, FiberSerializer


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


class FabricCompositionListAPI(ListAPIView):
    queryset = FabricComposition.objects.filter(
        is_archived=False
    )
    serializer_class = FabricCompositionSerializer


class FiberCreateAPI(CreateAPIView):
    serializer_class = FiberSerializer


class FiberListAPI(ListAPIView):
    queryset = Fiber.objects.filter(
        is_archived=False
    )
    serializer_class = FiberSerializer


class FiberUpdateAPI(UpdateAPIView):
    queryset = Fiber.objects.all()
    serializer_class = FiberSerializer


class FabricTypeListAPI(ListAPIView):
    queryset = FabricType.objects.filter(
        is_archived=False
    )
    serializer_class = FabricTypeSerializer


class FiberPercentageListAPI(ListAPIView):
    queryset = FiberPercentage.objects.filter(
        is_archived=False
    )
    serializer_class = FiberPercentageSerializer


class FiberPercentageCreateAPI(CreateAPIView):
    serializer_class = FiberPercentageSerializer


class FiberPercentageUpdateAPI(UpdateAPIView):
    queryset = FiberPercentage.objects.all()
    serializer_class = FiberPercentageSerializer


class FabricTypeCreateAPI(CreateAPIView):
    serializer_class = FabricTypeSerializer


class FabricTypeUpdateAPI(UpdateAPIView):
    queryset = FabricType.objects.all()
    serializer_class = FabricTypeSerializer


class FabricCompositionCreateAPI(CreateAPIView):
    serializer_class = FabricCompositionSerializer


class FabricCompositionUpdateAPI(UpdateAPIView):
    queryset = FabricComposition.objects.all()
    serializer_class = FabricCompositionSerializer