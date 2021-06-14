from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from fabric.models import Fabric, FabricComposition, FabricType, FiberPercentage, Fiber
from fabric.serializers import FabricSerializer, FabricCompositionSerializer, FabricTypeSerializer, \
    FabricListSerializer, FiberPercentageSerializer, FiberSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from supplier.models import Supplier
from supplier.api import SupplierListAPI


class FabricCreateAPI(CreateAPIView):
    serializer_class = FabricSerializer


@api_view(["POST"])
@permission_classes(())
def FabricCreateFromExcelAPI(request):
    excel_data = request.data
    print("Excel data:",excel_data)
    for key in excel_data:
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
            if not Supplier.objects.filter(name=supplier).exists():
                Supplier.objects.create(name=supplier)

            if not FabricType.objects.filter(name=fabric_type).exists():
                FabricType.objects.create(name=fabric_type)

            # if not Fiber.objects.filter(name=fiber1).exists():
            #     Fiber.objects.create(name=fiber1)

            if not FiberPercentage.objects.filter(fiber=fiber1).exists():
                if not Fiber.objects.filter(name=fiber1).exists():
                    Fiber.objects.create(name=fiber1)
                else:
                    if FiberPercentage.objects.filter(fiber=fiber1, percentage=percentage1):
                        FiberPercentage.objects.create(fiber=fiber1, percentage=percentage1)

            if not Fiber.objects.filter(name=fiber2).exists():
                Fiber.objects.create(name=fiber2)

            if not Fiber.objects.filter(name=fiber3).exists():
                Fiber.objects.create(name=fiber3)




    data_error = {
        'status': "Failed to upload data.",
        'code': 500,
        "result": None
    }

    data = {
        'status': 'success',
        'code': HTTP_200_OK,
        "message": 'A verification link has been sent to your email address. Please open it to confirm your account.',
        "result": {
            "user": {
                #"email": excel_data['email'],
            }
        }
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