from django.db import models
from django.db.models.signals import pre_save
from fabric.models import Fabric, FabricDetail
from fabric_sample_tracker_api.models import FabricSampleTrackerModel, populate_time_info
from resources import strings_style


class WashType(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_style.WASH_TYPE_VERBOSE_NAME
        verbose_name_plural = strings_style.WASH_TYPE_VERBOSE_NAME_PLURAL
        db_table = 'wash_types'

    def __str__(self):
        return self.name


class Style(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)
    fabric = models.ForeignKey(Fabric, on_delete=models.PROTECT, db_column='fabric')
    fabric_details = models.ForeignKey(FabricDetail, on_delete=models.PROTECT, db_column='fabric_details')
    wash_type = models.ForeignKey(WashType, on_delete=models.PROTECT, db_column='wash_type')
    designer = models.CharField(max_length=255)
    fob = models.PositiveIntegerField()
    remark = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = strings_style.STYLE_VERBOSE_NAME
        verbose_name_plural = strings_style.STYLE_VERBOSE_NAME_PLURAL
        db_table = 'styles'

    def __str__(self):
        return self.name


pre_save.connect(populate_time_info, sender=Style)
pre_save.connect(populate_time_info, sender=WashType)
