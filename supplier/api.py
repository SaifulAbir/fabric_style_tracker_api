from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from supplier.models import Supplier, Country, SupplierType
from supplier.serializers import SupplierSerializer, CountrySerializer, SupplierTypeSerializer


class SupplierListAPI(ListAPIView):
    queryset = Supplier.objects.filter(
        is_archived=False
    )
    serializer_class = SupplierSerializer


class SupplierCreateAPI(CreateAPIView):
    serializer_class = SupplierSerializer


class SupplierUpdateAPI(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CountryListAPI(ListAPIView):
    queryset = Country.objects.filter(
        is_archived=False
    )
    serializer_class = CountrySerializer


class SupplierTypeCreateAPI(CreateAPIView):
    serializer_class = SupplierTypeSerializer

class SupplierTypeUpdateAPI(UpdateAPIView):
    queryset = SupplierType.objects.all()
    serializer_class = SupplierTypeSerializer

class SupplierTypeListAPI(ListAPIView):
    queryset = SupplierType.objects.filter(
        is_archived=False
    )
    serializer_class = SupplierTypeSerializer