from django.contrib import admin
from.models import VendorProfile, PurchaseOrder,HistorialPerformance

# Register your models here.
admin.site.register(VendorProfile)
admin.site.register(PurchaseOrder)
admin.site.register(HistorialPerformance)