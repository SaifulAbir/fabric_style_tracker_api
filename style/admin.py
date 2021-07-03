from django.contrib import admin
from fabric_sample_tracker_api.admin import FabricSampleTrackerAdmin
from style.models import Style, WashType
# Register your models here.

@admin.register(Style)
class StyleAdmin(FabricSampleTrackerAdmin):
    list_display = ['name', 'fabric', 'fabric_details', 'wash_type',
                    'designer', 'fob', 'remark']

@admin.register(WashType)
class WashTypeAdmin(FabricSampleTrackerAdmin):
    list_display = ['name']