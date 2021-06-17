from django.db import models
from fabric_sample_tracker_api.models import FabricSampleTrackerModel
from resources import strings_supplier


class SupplierType(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_supplier.SUPPLIER_TYPE_VERBOSE_NAME
        verbose_name_plural = strings_supplier.SUPPLIER_TYPE_VERBOSE_NAME_PLURAL
        db_table = 'supplier_types'

    def __str__(self):
        return self.name


class Country(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_supplier.COUNTRY_VERBOSE_NAME
        verbose_name_plural = strings_supplier.COUNTRY_VERBOSE_NAME_PLURAL
        db_table = 'countries'

    def __str__(self):
        return self.name


class Supplier(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)
    supplier_type = models.ForeignKey(SupplierType, on_delete=models.PROTECT, null=True, db_column='supplier_type')
    contact_person_name = models.CharField(max_length=255, null=True, blank=True)
    contact_person_number = models.CharField(max_length=255, null=True, blank=True)
    contact_person_email = models.EmailField(max_length=255, null=True, blank=True)
    license_number = models.CharField(max_length=255, null=True, blank=True)
    vat_number = models.PositiveIntegerField(null=True, blank=True)
    corporate_address = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, db_column='country')
    supplier_address = models.TextField()

    class Meta:
        verbose_name = strings_supplier.SUPPLIER_VERBOSE_NAME
        verbose_name_plural = strings_supplier.SUPPLIER_VERBOSE_NAME_PLURAL
        db_table = 'suppliers'

    def __str__(self):
        return self.name
