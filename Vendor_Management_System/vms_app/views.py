from django.shortcuts import render
from rest_framework import generics
from . models import VendorProfile, PurchaseOrder
from.serializers import VendorSerializers, PurchaseOrderSerializers ,VendorPerformanceSerializer, AcknowledgePurchaseOrderSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class VendorCreateListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = VendorProfile.objects.all()
    serializer_class = VendorSerializers


class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = VendorProfile.objects.all()
    serializer_class = VendorSerializers


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseOrderSerializers

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        vendor_id = self.request.query_params.get('vendor_id', None)
        if vendor_id:
            queryset = queryset.filter(vendor__id=vendor_id)
        return queryset
    

class PurchaseOrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializers
    lookup_field = 'pk'


class VendorPerformanceview(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = VendorProfile.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.calculations()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgePurchaseOrderSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        if instance.status != 'pending':
            return Response({"error": "Purchase order is not in pending status."}, status=400)

        instance.acknowledgment_date = serializer.validated_data['acknowledgment_date']
        instance.status = 'completed'
        instance.save()   