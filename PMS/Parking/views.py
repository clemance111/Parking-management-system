from Parking.serializers import *
from Parking.models import *
from rest_framework.response import Response
from rest_framework.views import APIView


class CarAPI(APIView):
    def get(self, request, plate_number=None):
        if plate_number:
            instance = Car.objects.get(plate_number=plate_number)
            serializer = CarSerializer(instance)
            return Response(serializer.data, status=200)
        instance = Car.objects.all()
        serializer = CarSerializer(instance, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class CarParkingAPI(APIView):
    def get(self, request, id=None):
        if id:
            parking_instance=CarParking.objects.get(id=id)
            serializer = CarParkingSerializer(parking_instance)
            return Response(serializer.data, status=200)
        instance = Car.objects.all()
        serializer = CarSerializer(instance, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        car = serializer.instance
        parking = Parking.objects.last()
        instance = CarParking(car=car, parking=parking)
        instance.save()
        keke = CarParkingSerializer(instance)
        return Response(keke.data, status=201)