import datetime
from dateutil.relativedelta import relativedelta
from style.models import Style, WashType, Designer, Property
from style.serializers import StyleSerializer, StyleListSerializer, WashTypeListSerializer, DesignerListSerializer, \
    PropertyListSerializer, StyleNameListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser


class StyleListAPI(ListAPIView):
    queryset = Style.objects.filter(is_archived=False)
    serializer_class = StyleListSerializer


class StyleNameListAPI(ListAPIView):
    queryset = Style.objects.filter(is_archived=False)
    serializer_class = StyleNameListSerializer


class StyleSearchAPI(ListAPIView):
    serializer_class = StyleListSerializer

    def get_queryset(self):
        request = self.request
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        name = request.GET.get('name')
        designer = request.GET.get('designer')
        property = request.GET.get('property')
        wash_type = request.GET.get('wash_type')

        if from_date and to_date:
            queryset = Style.objects.filter(is_archived=False, created_at__gte=from_date,
                              created_at__lte=to_date)
        else:
            this_month = datetime.datetime.today()
            previous_month = this_month - relativedelta(months=1)
            queryset = Style.objects.filter(is_archived=False, created_at__gte=previous_month,
                                  created_at__lt=this_month)
        if name:
            queryset = queryset.filter(name=name)
        if designer:
            queryset = queryset.filter(designer__name=designer)
        if property:
            queryset = queryset.filter(property__name=property)
        if wash_type:
            queryset = queryset.filter(wash_type__name=wash_type)

        return queryset


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
