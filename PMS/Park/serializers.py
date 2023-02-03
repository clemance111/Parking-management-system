from rest_framework import serializers
from Park.models import Car, CarParking, Parking
from django.utils import timezone
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'

class CarParkingSerializer(serializers.ModelSerializer):
    price=serializers.SerializerMethodField()
    class Meta:
        model=CarParking
        fields='__all__'
    def get_price(self,obj):
        remaining_time = timezone.now()-obj.entry_time
        hour = remaining_time.seconds//3600
        if hour>0:
            return obj.parking.price*hour
        return obj.parking.price