from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from style.models import Style, WashType
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
        WashType.objects.filter(id=instance.wash_type.id).update(name=validated_data.pop('wash_type'))
        validated_data.update({"wash_type": instance.wash_type})
        return super().update(instance, validated_data)