from django.contrib import admin
from fabric.models import Fabric
from fabric_sample_tracker_api.admin import FabricSampleTrackerAdmin


@admin.register(Fabric)
class FabricAdmin(FabricSampleTrackerAdmin):
    list_display = ['dekko_reference', 'mill_reference', 'supplier', 'fabric_type',
                    'composition', 'construction','shrinkage', 'weight'
                    ]
