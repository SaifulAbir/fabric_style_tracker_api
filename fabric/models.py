from django.core.files import File
from django.db import models
from django.db.models.signals import pre_save
from barcode import EAN13
from barcode.writer import ImageWriter
from io import BytesIO
from fabric.utils import unique_code_generator
from fabric_sample_tracker_api.models import FabricSampleTrackerModel, populate_time_info
from resources import strings_fabric
from supplier.models import Supplier


class FabricType(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.FABRIC_TYPE_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_TYPE_VERBOSE_NAME_PLURAL
        db_table = 'fabric_types'

    def __str__(self):
        return self.name


class Fiber(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.FIBER_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FIBER_VERBOSE_NAME_PLURAL
        db_table = 'fibers'

    def __str__(self):
        return self.name


class FiberPercentage(FabricSampleTrackerModel):
    fiber = models.ForeignKey(Fiber, on_delete=models.PROTECT, db_column='fiber')
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.FIBER_PERCENTAGE_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FIBER_PERCENTAGE_VERBOSE_NAME_PLURAL
        unique_together = ('fiber', 'percentage',)
        db_table = 'fiber_percentages'

    def __str__(self):
        return self.fiber.name + " " + str(self.percentage) + "%"

    @property
    def name(self):
        return self.fiber.name + " " + str(self.percentage) + "%"


class FabricComposition(FabricSampleTrackerModel):
    fiber_percentages = models.ManyToManyField(FiberPercentage, through="FiberComposition")

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.FABRIC_COMPOSITION_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_COMPOSITION_VERBOSE_NAME_PLURAL
        db_table = 'fabric_compositions'

    @property
    def fabric_composition(self):
        return " ".join([str(fiber) for fiber in self.fiber_percentages.all()])
    def __str__(self):
        return " ".join([str(fiber) for fiber in self.fiber_percentages.all()])


class FiberComposition(FabricSampleTrackerModel):
    fiber_percentage = models.ForeignKey(FiberPercentage, on_delete=models.PROTECT)
    fabric_composition = models.ForeignKey(FabricComposition, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.FIBER_COMPOSITION_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FIBER_COMPOSITION_VERBOSE_NAME_PLURAL
        unique_together = ('fiber_percentage', 'fabric_composition',)
        db_table = 'fiber_compositions'


class FabricConstruction(FabricSampleTrackerModel):
    ends_per_inch = models.PositiveIntegerField()
    picks_per_inch = models.PositiveIntegerField()
    warp_count = models.PositiveIntegerField()
    weft_count = models.PositiveIntegerField()

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.FABRIC_CONSTRUCTION_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_CONSTRUCTION_VERBOSE_NAME_PLURAL
        db_table = 'fabric_constructions'

    def __str__(self):
        return "{}*{}/{}*{}".format(self.ends_per_inch, self.picks_per_inch, self.warp_count, self.weft_count)


class Shrinkage(FabricSampleTrackerModel):
    warp = models.PositiveIntegerField()
    weft = models.PositiveIntegerField()

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.SHRINKAGE_VERBOSE_NAME
        verbose_name_plural = strings_fabric.SHRINKAGE_VERBOSE_NAME_PLURAL
        db_table = 'shrinkage'

    def __str__(self):
        return "{}, {}".format(self.warp, self.weft)


class Weave(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.WEAVE_VERBOSE_NAME
        verbose_name_plural = strings_fabric.WEAVE_VERBOSE_NAME_PLURAL
        db_table = 'weaves'

    def __str__(self):
        return self.name


class Appearance(FabricSampleTrackerModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.APPEARANCE_VERBOSE_NAME
        verbose_name_plural = strings_fabric.APPEARANCE_VERBOSE_NAME_PLURAL
        db_table = 'appearances'

    def __str__(self):
        return self.name


class Fabric(FabricSampleTrackerModel):
    dekko_reference = models.CharField(max_length=255, unique=True)
    mill_reference = models.CharField(max_length=255, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    fabric_type = models.ForeignKey(FabricType, on_delete=models.PROTECT)
    composition = models.ForeignKey(FabricComposition, on_delete=models.PROTECT)
    construction = models.ForeignKey(FabricConstruction, on_delete=models.PROTECT)
    weave = models.ForeignKey(Weave, on_delete=models.PROTECT)
    appearance = models.ForeignKey(Appearance, on_delete=models.PROTECT)
    shrinkage = models.ForeignKey(Shrinkage, on_delete=models.PROTECT)
    weight = models.PositiveIntegerField(null=True, blank=True)
    cuttable_width = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    moq = models.PositiveIntegerField(null=True, blank=True)
    lead_time = models.PositiveIntegerField(null=True, blank=True)
    initial_availability = models.PositiveIntegerField(null=True, blank=True)
    last_availability = models.PositiveIntegerField(null=True, blank=True)
    code = models.CharField(max_length=13, blank=True)
    barcode = models.ImageField(upload_to="images/", blank=True)
    image = models.ImageField(upload_to="images/", blank=True)
    marketing_tools = models.TextField(null=True, blank=True)
    remark = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.FABRIC_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_VERBOSE_NAME_PLURAL
        db_table = 'fabrics'

    def __str__(self):
        return self.dekko_reference

    # def save(self, *args, **kwargs):
    #     ean = EAN13(f'{self.code}', writer=ImageWriter())
    #     buffer = BytesIO()
    #     ean.write(buffer)
    #     self.barcode.save(f'{self.dekko_reference}.png', File(buffer), save=False)
    #     return super().save(*args, **kwargs)

    @property
    def fabric_composition(self):
        return " ".join([str(p) for p in self.composition.fiber_percentages.all()])

    @property
    def fabric_construction(self):
        return "{}*{}/{}*{}".format(self.construction.ends_per_inch, self.construction.picks_per_inch, self.construction.warp_count, self.construction.weft_count)


class FabricDetail(FabricSampleTrackerModel):
    fabric = models.ForeignKey(Fabric, on_delete=models.PROTECT)
    initial_availability = models.PositiveIntegerField(null=True, blank=True)
    used_yds = models.PositiveIntegerField(null=True, blank=True)
    last_availability = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = strings_fabric.FABRIC_DETAIL_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_DETAIL_VERBOSE_NAME_PLURAL
        db_table = 'fabric_details'

    def __str__(self):
        return self.fabric.dekko_reference


def fabric_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.code:
        instance.code = unique_code_generator(instance)
        ean = EAN13(f'{instance.code}', writer=ImageWriter())
        instance.code = ean
        buffer = BytesIO()
        ean.write(buffer)
        instance.barcode.save(f'{instance.dekko_reference}.png', File(buffer), save=False)


pre_save.connect(populate_time_info, sender=Fabric)
pre_save.connect(populate_time_info, sender=FabricDetail)
pre_save.connect(fabric_pre_save_receiver, sender=Fabric)
pre_save.connect(populate_time_info, sender=Shrinkage)
pre_save.connect(populate_time_info, sender=FabricConstruction)
pre_save.connect(populate_time_info, sender=FabricComposition)
pre_save.connect(populate_time_info, sender=Fiber)
pre_save.connect(populate_time_info, sender=FabricType)
