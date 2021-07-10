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


class WashTypeListAPI(ListAPIView):
    queryset = WashType.objects.filter(is_archived=False)
    serializer_class = WashTypeListSerializer


class DesignerListAPI(ListAPIView):
    queryset = Designer.objects.filter(is_archived=False)
    serializer_class = DesignerListSerializer


class PropertyListAPI(ListAPIView):
    queryset = Property.objects.filter(is_archived=False)
    serializer_class = PropertyListSerializer
