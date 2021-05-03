from django.contrib import admin
from fabric_sample_tracker_api.admin import FabricSampleTrackerAdmin
from supplier.models import Supplier, Country, SupplierType


@admin.register(SupplierType)
class SupplierTypeAdmin(FabricSampleTrackerAdmin):
    list_display = ['name', ]


@admin.register(Country)
class CountryAdmin(FabricSampleTrackerAdmin):
    list_display = ['name', ]


@admin.register(Supplier)
class SupplierAdmin(FabricSampleTrackerAdmin):
    list_display = ['name', 'supplier_type', 'contact_person_name', 'contact_person_number',
                    'contact_person_email', 'license_number', 'vat_number'
                    ]
