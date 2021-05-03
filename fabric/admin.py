from django.contrib import admin
from fabric.models import Fabric
from fabric_sample_tracker_api.models import FabricSampleTrackerModel


@admin.register(Fabric)
class FabricAdmin(FabricSampleTrackerModel):
    list_display = ['dekko_reference', 'mill_reference', 'supplier', 'fabric_type',
                    'composition', 'construction','shrinkage', 'weight'
                    ]
