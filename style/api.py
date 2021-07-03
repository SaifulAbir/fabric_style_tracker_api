from style.models import Style, WashType, Designer
from style.serializers import StyleSerializer, StyleListSerializer, WashTypeListSerializer, DesignerListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView


class StyleListAPI(ListAPIView):
    queryset = Style.objects.filter(is_archived=False)
    serializer_class = StyleListSerializer


class StyleCreateAPI(CreateAPIView):
    serializer_class = StyleSerializer


class StyleUpdateAPI(UpdateAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class WashTypeListAPI(ListAPIView):
    queryset = WashType.objects.filter(is_archived=False)
    serializer_class = WashTypeListSerializer


class DesignerListAPI(ListAPIView):
    queryset = Designer.objects.filter(is_archived=False)
    serializer_class = DesignerListSerializer