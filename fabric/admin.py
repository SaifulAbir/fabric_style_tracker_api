from django.contrib import admin
from fabric.models import Fabric, FabricType, FabricComposition, FabricConstruction, Shrinkage, Fiber
from fabric_sample_tracker_api.admin import FabricSampleTrackerAdmin


@admin.register(Fabric)
class FabricAdmin(FabricSampleTrackerAdmin):
    list_display = ['dekko_reference', 'mill_reference', 'supplier', 'fabric_type',
                    'composition', 'construction','shrinkage', 'weight'
                    ]


@admin.register(FabricType)
class FabricTypeAdmin(FabricSampleTrackerAdmin):
    list_display = ['name']


@admin.register(Fiber)
class FiberCompositionAdmin(FabricSampleTrackerAdmin):
    list_display = ['name']


@admin.register(FabricComposition)
class FabricCompositionAdmin(FabricSampleTrackerAdmin):
    list_display = ['fiber', 'percentage']


@admin.register(FabricConstruction)
class FabricConstructionAdmin(FabricSampleTrackerAdmin):
    list_display = ['ends_per_inch', 'picks_per_inch', 'warp_count', 'weft_count']


@admin.register(Shrinkage)
class ShrinkageAdmin(FabricSampleTrackerAdmin):
    list_display = ['warp', 'weft']
