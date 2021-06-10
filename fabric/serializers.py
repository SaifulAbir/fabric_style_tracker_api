from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from fabric.models import Fabric, FabricComposition, FabricType, FabricConstruction, Shrinkage, FiberPercentage, Fiber
from supplier.models import Supplier


class FabricSerializer(ModelSerializer):
    ends_per_inch = serializers.IntegerField(write_only=True)
    picks_per_inch = serializers.IntegerField(write_only=True)
    warp_count = serializers.IntegerField(write_only=True)
    weft_count = serializers.IntegerField(write_only=True)
    warp = serializers.IntegerField(write_only=True)
    weft = serializers.IntegerField(write_only=True)

    class Meta:
        model = Fabric
        model_fields = ['dekko_reference', 'mill_reference', 'supplier', 'fabric_type', 'composition',
                        'construction', 'shrinkage', 'weight', 'cuttable_width', 'price', 'moq', 'lead_time', 'availability', 'marketing_tools', 'remark']
        extra_fields = ['ends_per_inch', 'picks_per_inch', 'warp_count', 'weft_count', 'warp', 'weft']
        fields = model_fields + extra_fields
        extra_kwargs = {"construction": {"required": False},
                        "shrinkage": {"required": False}}

    def create(self, validated_data):
        construction_instance = FabricConstruction.objects.create(ends_per_inch=validated_data.pop('ends_per_inch'),
                                                                  picks_per_inch=validated_data.pop('picks_per_inch'),
                                                                  warp_count=validated_data.pop('warp_count'),
                                                                  weft_count=validated_data.pop('weft_count'))
        shrinkage_instance = Shrinkage.objects.create(warp=validated_data.pop('warp'), weft=validated_data.pop('weft'))
        fabric_instance = Fabric.objects.create(**validated_data, construction=construction_instance, shrinkage=shrinkage_instance)
        return fabric_instance

    def update(self, instance, validated_data):
        FabricConstruction.objects.filter(id=instance.construction.id).update(
            ends_per_inch=validated_data.pop('ends_per_inch'),
            picks_per_inch=validated_data.pop('picks_per_inch'),
            warp_count=validated_data.pop('warp_count'),
            weft_count=validated_data.pop('weft_count'))
        Shrinkage.objects.filter(id=instance.shrinkage.id).update(
            warp=validated_data.pop('warp'), weft=validated_data.pop('weft'))
        validated_data.update({"construction": instance.construction, "shrinkage": instance.shrinkage})
        return super().update(instance, validated_data)


class FabricListSerializer(ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name')
    fabric_type_name = serializers.CharField(source='fabric_type.name')
    ends_per_inch = serializers.CharField(source='construction.ends_per_inch')
    picks_per_inch = serializers.CharField(source='construction.picks_per_inch')
    warp_count = serializers.CharField(source='construction.warp_count')
    weft_count = serializers.CharField(source='construction.weft_count')
    warp = serializers.CharField(source='shrinkage.warp')
    weft = serializers.CharField(source='shrinkage.weft')
    class Meta:
        model = Fabric
        fields = ('id', 'dekko_reference', 'mill_reference', 'supplier', 'supplier_name', 'fabric_type',
                  'fabric_type_name', 'fabric_composition', 'composition', 'fabric_construction', 'ends_per_inch',
                  'picks_per_inch', 'warp_count', 'weft_count', 'warp', 'weft', 'weight', 'cuttable_width', 'price',
                  'moq', 'lead_time', 'availability', 'marketing_tools', 'remark', 'barcode')


class FiberListSerializer(ModelSerializer):
    class Meta:
        model = Fiber
        fields = ('id', 'name')

class FabricCompositionSerializer(ModelSerializer):
    class Meta:
        model = FabricComposition
        fields = ('id', 'fabric_composition', 'fiber_percentages')


class FabricTypeSerializer(ModelSerializer):
    class Meta:
        model = FabricType
        fields = ('id', 'name')


class FiberPercentageSerializer(ModelSerializer):
    class Meta:
        model = FiberPercentage
        fields = ('id', 'name', 'fiber', 'percentage')