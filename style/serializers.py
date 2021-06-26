from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from style.models import Style, WashType
from fabric.models import FabricDetail, Fabric


class StyleSerializer(ModelSerializer):
    used_yds = serializers.IntegerField(write_only=True)
    wash_type = serializers.CharField(write_only=True)

    class Meta:
        model = Style
        model_fields = ['name', 'fabric', 'fabric_details', 'wash_type', 'designer', 'fob', 'remark']
        extra_fields = ['used_yds', 'wash_type']
        fields = model_fields + extra_fields

    def create(self, instance, validated_data):
        fabric_initial_availability = instance.fabric.initial_availability
        fabric_last_availability = instance.fabric.last_availability
        if fabric_last_availability == 0:
            fabric_last_availability = fabric_initial_availability - validated_data.get('used_yds')
        else:
            fabric_last_availability = fabric_last_availability - validated_data.get('used_yds')

        fabric_instance = Fabric.objects.filter(id=instance.fabric.id).update(last_availability=fabric_last_availability)
        fabric_details_instance = FabricDetail.objects.create(
            fabric=validated_data.get('fabric'),
            initial_availability=fabric_last_availability,
            used_yds=validated_data.pop('used_yds'),
            last_availability=fabric_last_availability
        )
        style_instance = Style.objects.create(**validated_data, fabric=fabric_instance, fabric_details=fabric_details_instance)
        return style_instance

    def update(self, instance, validated_data):
        WashType.objects.filter(id=instance.wash_type.id).update(name=validated_data.pop('wash_type'))
        validated_data.update({"wash_type": instance.wash_type})
        return super().update(instance, validated_data)