from django.db import models
from fabric.models import Fabric
from fabric_sample_tracker_api.models import FabricSampleTrackerModel
from resources import strings_style


class Style(FabricSampleTrackerModel):
    name = models.CharField(max_length=255)
    fabric = models.ForeignKey(Fabric, on_delete=models.PROTECT, db_column='fabric')
    wash = models.CharField(max_length=255)
    designer = models.CharField(max_length=255)
    fob = models.PositiveIntegerField()
    remark = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = strings_style.STYLE_VERBOSE_NAME
        verbose_name_plural = strings_style.STYLE_VERBOSE_NAME_PLURAL
        db_table = 'styles'

    def __str__(self):
        return self.name
