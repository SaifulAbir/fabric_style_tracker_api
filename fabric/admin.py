from django.contrib import admin
from fabric.models import Fabric, FabricType, FabricComposition, FabricConstruction, Shrinkage, Fiber, FiberPercentage, \
    FiberComposition, FabricDetail, Weave, Appearance
from fabric_sample_tracker_api.admin import FabricSampleTrackerAdmin


@admin.register(Fabric)
class FabricAdmin(FabricSampleTrackerAdmin):
    list_display = ['dekko_reference', 'mill_reference', 'supplier', 'fabric_type',
                    'composition', 'construction','shrinkage', 'weight', 'initial_availability', 'last_availability']


@admin.register(FabricType)
class FabricTypeAdmin(FabricSampleTrackerAdmin):
    list_display = ['name']


@admin.register(Fiber)
class FiberAdmin(FabricSampleTrackerAdmin):
    list_display = ['name']


@admin.register(FiberPercentage)
class FiberPercentageAdmin(FabricSampleTrackerAdmin):
    list_display = ['fiber', 'percentage']


class FiberCompositionInline(admin.TabularInline):
    model = FiberComposition
    fields = ['fiber_percentage', ]
    extra = 2 # how many rows to show


@admin.register(FabricComposition)
class FabricCompositionAdmin(FabricSampleTrackerAdmin):
    inlines = (FiberCompositionInline, )
    list_display = ['fabric_composition']\


@admin.register(FiberComposition)
class FiberCompositionAdmin(FabricSampleTrackerAdmin):
    list_display = ['fiber_percentage', 'fabric_composition']


@admin.register(FabricConstruction)
class FabricConstructionAdmin(FabricSampleTrackerAdmin):
    list_display = ['ends_per_inch', 'picks_per_inch', 'warp_count', 'weft_count']


@admin.register(Shrinkage)
class ShrinkageAdmin(FabricSampleTrackerAdmin):
    list_display = ['warp', 'weft']


@admin.register(FabricDetail)
class FabricDetailAdmin(FabricSampleTrackerAdmin):
    list_display = ['fabric', 'initial_availability', 'used_yds', 'last_availability']


@admin.register(Weave)
class WeaveAdmin(FabricSampleTrackerAdmin):
    list_display = ['name']


@admin.register(Appearance)
class AppearanceAdmin(FabricSampleTrackerAdmin):
    list_display = ['name']