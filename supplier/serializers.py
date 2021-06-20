from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from supplier.models import Supplier, SupplierType, Country


class SupplierSerializer(ModelSerializer):
    supplier_type_name = serializers.CharField(source='supplier_type.name', read_only=True)
    country_name = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = Supplier
        fields = ('id', 'name', 'supplier_type', 'supplier_type_name', 'contact_person_name', 'contact_person_number',
                  'contact_person_email', 'license_number', 'vat_number', 'corporate_address', 'country',
                  'country_name', 'supplier_address')


class SupplierTypeSerializer(ModelSerializer):
    class Meta:
        model = SupplierType
        fields = ["id", "name"]


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"