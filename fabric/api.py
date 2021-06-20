from collections import Counter

from django.http import HttpResponse, Http404
from rest_framework import generics
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from fabric.models import Fabric, FabricComposition, FabricType, FiberPercentage, Fiber, FiberComposition, \
    FabricConstruction, Shrinkage
from fabric.serializers import FabricSerializer, FabricCompositionSerializer, FabricTypeSerializer, \
    FabricListSerializer, FiberPercentageSerializer, FiberSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from fabric_sample_tracker_api.settings import STATIC_DIR
from supplier.models import Supplier
from supplier.api import SupplierListAPI
import os

class FabricCreateAPI(CreateAPIView):
    serializer_class = FabricSerializer

class DownloadFabricExcelFormat(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        file_path = os.path.join(STATIC_DIR, 'fabric_excel_format.xlsx')
        if file_path:
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read())
                response['Content-Disposition'] = 'attachment; filename=fabric_excel_format.xlsx'
                return response
        else:
            raise Http404


@api_view(["POST"])
@permission_classes(())
def FabricCreateFromExcelAPI(request):
    excel_data = request.data
    new_entry = 0
    total_data = 0

    for key in excel_data:
        fiber_percentages = []
        total_data += 1
        mill_reference = key[0]
        dekko_reference = key[1]
        supplier = key[2]
        fabric_type = key[3]
        fiber1 = key[4]
        percentage1 = key[5]
        fiber2 = key[6]
        percentage2 = key[7]
        fiber3 = key[8]
        percentage3 = key[9]
        ends_per_inch = key[10]
        picks_per_inch = key[11]
        warp_count = key[12]
        weft_count = key[13]
        warp = key[14]
        weft = key[15]
        weight = key[16]
        cuttable_width = key[17]
        price = key[18]
        moq = key[19]
        lead_time = key[20]
        availability = key[21]
        marketing_tools = key[22]
        remark = key[23]

        if not Fabric.objects.filter(mill_reference=mill_reference).exists():
            new_entry += 1
            if not Supplier.objects.filter(name=supplier).exists():
                supplier_obj = Supplier.objects.create(name=supplier)
            else:
                supplier_obj = Supplier.objects.get(name=supplier)

            if not FabricType.objects.filter(name=fabric_type).exists():
                fabric_type_obj = FabricType.objects.create(name=fabric_type)
            else:
                fabric_type_obj = FabricType.objects.get(name=fabric_type)

            if fiber1 != None or percentage1 != None:
                if not FiberPercentage.objects.filter(fiber__name=fiber1, percentage=percentage1).exists():
                    if not Fiber.objects.filter(name=fiber1).exists():
                        fiber_obj1 = Fiber.objects.create(name=fiber1)
                        fiber_percentage_obj1 = FiberPercentage.objects.create(fiber=fiber_obj1, percentage=percentage1)
                        fiber_percentages.append(fiber_percentage_obj1)
                    else:
                        fiber_obj1 = Fiber.objects.get(name=fiber1)
                        fiber_percentage_obj1 = FiberPercentage.objects.create(fiber=fiber_obj1, percentage=percentage1)
                        fiber_percentages.append(fiber_percentage_obj1)
                else:
                    fiber_percentage_obj1 = FiberPercentage.objects.get(fiber__name=fiber1, percentage=percentage1)
                    fiber_percentages.append(fiber_percentage_obj1)

            if fiber2 != None or percentage2 != None:
                if not FiberPercentage.objects.filter(fiber__name=fiber2, percentage=percentage2).exists():
                    if not Fiber.objects.filter(name=fiber2).exists():
                        fiber_obj2 = Fiber.objects.create(name=fiber2)
                        fiber_percentage_obj2 = FiberPercentage.objects.create(fiber=fiber_obj2, percentage=percentage2)
                        fiber_percentages.append(fiber_percentage_obj2)
                    else:
                        fiber_obj2 = Fiber.objects.get(name=fiber2)
                        fiber_percentage_obj2 = FiberPercentage.objects.create(fiber=fiber_obj2, percentage=percentage2)
                        fiber_percentages.append(fiber_percentage_obj2)
                else:
                    fiber_percentage_obj2 = FiberPercentage.objects.get(fiber__name=fiber2, percentage=percentage2)
                    fiber_percentages.append(fiber_percentage_obj2)

            if fiber3 != None or percentage3 != None:
                if not FiberPercentage.objects.filter(fiber__name=fiber3, percentage=percentage3).exists():
                    if not Fiber.objects.filter(name=fiber3).exists():
                        fiber_obj3 = Fiber.objects.create(name=fiber3)
                        fiber_percentage_obj3 = FiberPercentage.objects.create(fiber=fiber_obj3, percentage=percentage3)
                        fiber_percentages.append(fiber_percentage_obj3)
                    else:
                        fiber_obj3 = Fiber.objects.get(name=fiber3)
                        fiber_percentage_obj3 = FiberPercentage.objects.create(fiber=fiber_obj3, percentage=percentage3)
                        fiber_percentages.append(fiber_percentage_obj3)
                else:
                    fiber_percentage_obj3 = FiberPercentage.objects.get(fiber__name=fiber3, percentage=percentage3)
                    fiber_percentages.append(fiber_percentage_obj3)

            if len(fiber_percentages) > 0:
                fiber_percentage_id = [obj.id for obj in fiber_percentages]
                fiber_compositions = FiberComposition.objects.filter(fiber_percentage__in=fiber_percentage_id)
                fabric_composition_id_counter = dict(Counter([obj.fabric_composition.id for obj in fiber_compositions]))
                fabric_composition = None
                for key, value in fabric_composition_id_counter.items():
                    fabric_obj_count = FabricComposition.objects.get(id=key).fiber_percentages.count()
                    if fabric_obj_count == len(fiber_percentages):
                        if value == len(fiber_percentage_id):
                            fabric_composition = key

                if not fabric_composition:
                    composition = FabricComposition.objects.create()
                    for fiber_percentage in fiber_percentages:
                        FiberComposition(fiber_percentage_id=fiber_percentage.id, fabric_composition=composition).save()
                    composition = composition.id
                else:
                    composition = fabric_composition

            if not FabricConstruction.objects.filter(ends_per_inch=ends_per_inch, picks_per_inch=picks_per_inch, warp_count=warp_count, weft_count=weft_count).exists():
                construction_obj = FabricConstruction.objects.create(ends_per_inch=ends_per_inch, picks_per_inch=picks_per_inch, warp_count=warp_count, weft_count=weft_count)
            else:
                construction_obj = FabricConstruction.objects.get(ends_per_inch=ends_per_inch, picks_per_inch=picks_per_inch, warp_count=warp_count, weft_count=weft_count)

            if not Shrinkage.objects.filter(warp=warp, weft=weft).exists():
                shrinkage_obj = Shrinkage.objects.create(warp=warp, weft=weft)
            else:
                shrinkage_obj = Shrinkage.objects.get(warp=warp, weft=weft)

            Fabric.objects.create(
                dekko_reference=dekko_reference,
                mill_reference=mill_reference,
                supplier=supplier_obj,
                fabric_type=fabric_type_obj,
                composition_id=composition,
                construction=construction_obj,
                shrinkage=shrinkage_obj,
                weight=weight,
                cuttable_width=cuttable_width,
                price=price,
                moq=moq,
                lead_time=lead_time,
                availability=availability,
                marketing_tools=marketing_tools,
                remark=remark
            )

    if new_entry == 0:
        message = "Sheet is up to date."
    else:
        message = "{} row added out of {}.".format(new_entry, total_data)
    data = {
        'status': 'success',
        'code': HTTP_200_OK,
        "message": message,
    }
    return Response(data)


class FabricUpdateAPI(UpdateAPIView):
    queryset = Fabric.objects.all()
    serializer_class = FabricSerializer


class FabricListAPI(ListAPIView):
    queryset = Fabric.objects.filter(
        is_archived=False
    )
    serializer_class = FabricListSerializer


class FabricCompositionListAPI(ListAPIView):
    queryset = FabricComposition.objects.filter(
        is_archived=False
    )
    serializer_class = FabricCompositionSerializer


class FiberCreateAPI(CreateAPIView):
    serializer_class = FiberSerializer


class FiberListAPI(ListAPIView):
    queryset = Fiber.objects.filter(
        is_archived=False
    )
    serializer_class = FiberSerializer


class FiberUpdateAPI(UpdateAPIView):
    queryset = Fiber.objects.all()
    serializer_class = FiberSerializer


class FabricTypeListAPI(ListAPIView):
    queryset = FabricType.objects.filter(
        is_archived=False
    )
    serializer_class = FabricTypeSerializer


class FiberPercentageListAPI(ListAPIView):
    queryset = FiberPercentage.objects.filter(
        is_archived=False
    )
    serializer_class = FiberPercentageSerializer


class FiberPercentageCreateAPI(CreateAPIView):
    serializer_class = FiberPercentageSerializer


class FiberPercentageUpdateAPI(UpdateAPIView):
    queryset = FiberPercentage.objects.all()
    serializer_class = FiberPercentageSerializer


class FabricTypeCreateAPI(CreateAPIView):
    serializer_class = FabricTypeSerializer


class FabricTypeUpdateAPI(UpdateAPIView):
    queryset = FabricType.objects.all()
    serializer_class = FabricTypeSerializer


class FabricCompositionCreateAPI(CreateAPIView):
    serializer_class = FabricCompositionSerializer


class FabricCompositionUpdateAPI(UpdateAPIView):
    queryset = FabricComposition.objects.all()
    serializer_class = FabricCompositionSerializer