from django.db import models
from fabric_sample_tracker_api.models import P7Model
from resources import strings_fabric


class FabricType(P7Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_fabric.FABRIC_TYPE_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_TYPE_VERBOSE_NAME_PLURAL
        db_table = 'fabric_types'

    def __str__(self):
        return self.name


class Fiber(P7Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_fabric.FIBER_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FIBER_VERBOSE_NAME_PLURAL
        db_table = 'fibers'

    def __str__(self):
        return self.name


class FabricComposition(P7Model):
    fiber = models.ForeignKey(Fiber, on_delete=models.PROTECT, db_column='fiber')
    percentage = models.PositiveIntegerField()

    class Meta:
        verbose_name = strings_fabric.FABRIC_COMPOSITION_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_COMPOSITION_VERBOSE_NAME_PLURAL
        db_table = 'fabric_compositions'

    def __str__(self):
        return self.fiber.name + " " + str(self.percentage) + "%"


class FabricConstruction(P7Model):
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


class Fabric(P7Model):
    dekko_reference = models.CharField(max_length=255, unique=True)
    mill_reference = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_fabric.FABRIC_VERBOSE_NAME
        verbose_name_plural = strings_fabric.FABRIC_VERBOSE_NAME_PLURAL
        db_table = 'fabrics'

    def __str__(self):
        return self.dekko_reference
