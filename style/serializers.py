from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from style.models import Style, WashType, Designer, Property
from fabric.models import FabricDetail


class StyleSerializer(ModelSerializer):
    used_yds = serializers.IntegerField(write_only=True)

    class Meta:
        model = Style
        model_fields = ['name', 'fabric', 'wash_type', 'designer', 'fob', 'remark']
        extra_fields = ['used_yds']
        fields = model_fields + extra_fields

    def create(self, validated_data):
        fabric_instance = validated_data.get('fabric')

        fabric_initial_availability = fabric_instance.initial_availability
        fabric_last_availability = fabric_instance.last_availability

        if fabric_last_availability == None:
            fabric_last_availability = fabric_initial_availability - validated_data.get('used_yds')
            fabric_detail_initial_availability = fabric_initial_availability
        else:
            fabric_detail_initial_availability = fabric_last_availability
            fabric_last_availability = fabric_last_availability - validated_data.get('used_yds')

        fabric_instance = validated_data.get('fabric')
        fabric_instance.last_availability = fabric_last_availability
        fabric_instance.save()

        fabric_details_instance = FabricDetail.objects.create(
            fabric=fabric_instance,
            initial_availability=fabric_detail_initial_availability,
            used_yds=validated_data.pop('used_yds'),
            last_availability=fabric_last_availability
        )
        style_instance = Style.objects.create(**validated_data, fabric_details=fabric_details_instance)
        return style_instance

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class StyleListSerializer(ModelSerializer):
    fabric_dekko_reference = serializers.CharField(source='fabric.dekko_reference')
    fabric_mill_reference = serializers.CharField(source='fabric.mill_reference')
    fabric_supplier = serializers.CharField(source='fabric.supplier')
    fabric_fabric_type = serializers.CharField(source='fabric.fabric_type')
    fabric_composition = serializers.CharField(source='fabric.composition')
    fabric_construction = serializers.CharField(source='fabric.construction')
    fabric_shrinkage = serializers.CharField(source='fabric.shrinkage')
    fabric_weight = serializers.CharField(source='fabric.weight')
    fabric_cuttable_width = serializers.CharField(source='fabric.cuttable_width')
    fabric_price = serializers.CharField(source='fabric.price')
    fabric_moq = serializers.CharField(source='fabric.moq')
    fabric_lead_time = serializers.CharField(source='fabric.lead_time')
    fabric_last_availability = serializers.CharField(source='fabric.last_availability')
    fabric_marketing_tools = serializers.CharField(source='fabric.marketing_tools')
    wash_type_name = serializers.CharField(source='wash_type.name')
    used_yds = serializers.CharField(source='fabric_details.used_yds')
    designer_name = serializers.CharField(source='designer.name')

    class Meta:
        model = Style
        fields = ('id', 'name', 'fabric', 'fabric_dekko_reference', 'used_yds', 'wash_type', 'wash_type_name', 'designer', 'designer_name', 'fob', 'remark', 'barcode', 'code',
                  'fabric_mill_reference', 'fabric_supplier', 'fabric_fabric_type', 'fabric_composition', 'fabric_construction', 'fabric_shrinkage',
                  'fabric_weight', 'fabric_cuttable_width', 'fabric_price', 'fabric_moq', 'fabric_lead_time', 'fabric_last_availability', 'fabric_marketing_tools')


class WashTypeListSerializer(ModelSerializer):
    class Meta:
        model = WashType
        fields = ['id', 'name']


class DesignerListSerializer(ModelSerializer):
    class Meta:
        model = Designer
        fields = ['id', 'name']


class PropertyListSerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name']