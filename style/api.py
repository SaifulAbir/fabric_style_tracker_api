from style.models import Style, WashType
from style.serializers import StyleSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView


class StyleListAPI(ListAPIView):
    queryset = Style.objects.filter(is_archived=False)
    serializer_class = StyleSerializer


class StyleCreateAPI(CreateAPIView):
    serializer_class = StyleSerializer


class StyleUpdateAPI(UpdateAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer