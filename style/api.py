from style.models import Style, WashType, Designer, Property
from style.serializers import StyleSerializer, StyleListSerializer, WashTypeListSerializer, DesignerListSerializer, \
    PropertyListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser


class StyleListAPI(ListAPIView):
    queryset = Style.objects.filter(is_archived=False)
    serializer_class = StyleListSerializer


class StyleCreateAPI(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = StyleSerializer


class StyleUpdateAPI(UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class WashTypeCreateAPI(CreateAPIView):
    serializer_class = WashTypeListSerializer


class WashTypeUpdateAPI(UpdateAPIView):
    queryset = WashType.objects.all()
    serializer_class = WashTypeListSerializer


class WashTypeListAPI(ListAPIView):
    queryset = WashType.objects.filter(is_archived=False)
    serializer_class = WashTypeListSerializer


class DesignerCreateAPI(CreateAPIView):
    serializer_class = DesignerListSerializer


class DesignerUpdateAPI(UpdateAPIView):
    queryset = Designer.objects.all()
    serializer_class = DesignerListSerializer


class DesignerListAPI(ListAPIView):
    queryset = Designer.objects.filter(is_archived=False)
    serializer_class = DesignerListSerializer


class PropertyCreateAPI(CreateAPIView):
    serializer_class = PropertyListSerializer


class PropertyUpdateAPI(UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer


class PropertyListAPI(ListAPIView):
    queryset = Property.objects.filter(is_archived=False)
    serializer_class = PropertyListSerializer
