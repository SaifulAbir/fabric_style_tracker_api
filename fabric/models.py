from django.db import models
from django.db.models.signals import pre_save
from fabric_sample_tracker_api.models import FabricSampleTrackerModel, populate_time_info
from resources import strings_fabric
from supplier.models import Supplier


class FabricType(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_fabric.FABRIC_TYPE_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_TYPE_VERBOSE_NAME_PLURAL
        db_table = 'fabric_types'

    def __str__(self):
        return self.name


class Fiber(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_fabric.FIBER_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FIBER_VERBOSE_NAME_PLURAL
        db_table = 'fibers'

    def __str__(self):
        return self.name


class FabricComposition(FabricSampleTrackerModel):
    fiber = models.ForeignKey(Fiber, on_delete=models.PROTECT, db_column='fiber')
    percentage = models.PositiveIntegerField()

    class Meta:
        verbose_name = strings_fabric.FABRIC_COMPOSITION_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_COMPOSITION_VERBOSE_NAME_PLURAL
        db_table = 'fabric_compositions'

    def __str__(self):
        return self.fiber.name + " " + str(self.percentage) + "%"


class FabricConstruction(FabricSampleTrackerModel):
    ends_per_inch = models.PositiveIntegerField(unique=True)
    picks_per_inch = models.PositiveIntegerField(unique=True)
    warp_count = models.PositiveIntegerField(unique=True)
    weft_count = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name = strings_fabric.FABRIC_CONSTRUCTION_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_CONSTRUCTION_VERBOSE_NAME_PLURAL
        db_table = 'fabric_constructions'

    def __str__(self):
        return "{}*{}/{}*{}".format(self.ends_per_inch, self.picks_per_inch, self.warp_count, self.weft_count)


class Shrinkage(FabricSampleTrackerModel):
    wrap = models.PositiveIntegerField()
    weft = models.PositiveIntegerField()

    class Meta:
        verbose_name = strings_fabric.SHRINKAGE_VERBOSE_NAME
        verbose_name_plural = strings_fabric.SHRINKAGE_VERBOSE_NAME_PLURAL
        db_table = 'shrinkage'

    def __str__(self):
        return "{}, {}".format(self.wrap, self.weft)


class Fabric(FabricSampleTrackerModel):
    dekko_reference = models.CharField(max_length=255, unique=True)
    mill_reference = models.CharField(max_length=255, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    fabric_type = models.ForeignKey(FabricType, on_delete=models.PROTECT)
    composition = models.ForeignKey(FabricComposition, on_delete=models.PROTECT)
    construction = models.ForeignKey(FabricConstruction, on_delete=models.PROTECT)
    shrinkage = models.ForeignKey(Shrinkage, on_delete=models.PROTECT)
    weight = models.PositiveIntegerField(null=True, blank=True)
    cuttable_width = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    moq = models.PositiveIntegerField(null=True, blank=True)
    lead_time = models.PositiveIntegerField(null=True, blank=True)
    availability = models.PositiveIntegerField(null=True, blank=True)
    marketing_tools = models.TextField(null=True, blank=True)
    remark = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = strings_fabric.FABRIC_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_VERBOSE_NAME_PLURAL
        db_table = 'fabrics'

    def __str__(self):
        return self.dekko_reference


pre_save.connect(populate_time_info, sender=Fabric)
pre_save.connect(populate_time_info, sender=Shrinkage)
pre_save.connect(populate_time_info, sender=FabricConstruction)
pre_save.connect(populate_time_info, sender=FabricComposition)
pre_save.connect(populate_time_info, sender=Fiber)
pre_save.connect(populate_time_info, sender=FabricType)
