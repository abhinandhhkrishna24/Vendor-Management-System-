from rest_framework import serializers
from .models import VendorProfile,PurchaseOrder,HistorialPerformance



class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model =VendorProfile
        fields =  ['name','contact_details','address','vendor_code']
        
class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']


class PurchaseOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model =PurchaseOrder
        fields = ['po_number','vendor','order_date','delivery_date','items','quantity','status']   

class HistoricalPerormanceSerializers(serializers.ModelSerializer):
    class Meta:
        model =HistorialPerformance
        fields = '__all__'            

class AcknowledgePurchaseOrderSerializer(serializers.Serializer):
    acknowledgment_date = serializers.DateTimeField()


