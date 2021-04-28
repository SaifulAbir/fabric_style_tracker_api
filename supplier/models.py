from django.db import models
from fabric_sample_tracker_api.models import P7Model
from resources import strings_supplier


class SupplierType(P7Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_supplier.SUPPLIER_TYPE_VERBOSE_NAME
        verbose_name_plural = strings_supplier.SUPPLIER_TYPE_VERBOSE_NAME_PLURAL
        db_table = 'supplier_types'

    def __str__(self):
        return self.name
