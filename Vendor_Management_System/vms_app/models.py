from django.db import models
from django.utils import timezone
from django.db.models import Avg, ExpressionWrapper, F, fields

# Create your models here.



class VendorProfile(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=10, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)


    def calculations(self):
        
        completed_orders = self.purchaseorder_set.filter(status='completed', delivery_date__lte=timezone.now()).count()
        total_completed_orders = self.purchaseorder_set.filter(status='completed').count()
        self.on_time_delivery_rate = (completed_orders / total_completed_orders * 100) if total_completed_orders > 0 else 0.0

        quality_ratings = self.purchaseorder_set.filter(status='completed', quality_rating__isnull=False)
        total_ratings = quality_ratings.count()
        total_quality_rating = quality_ratings.aggregate(Avg('quality_rating'))['quality_rating__avg']
        self.quality_rating_avg = total_quality_rating if total_ratings > 0 else 0.0

        acknowledged_orders = self.purchaseorder_set.filter(acknowledgment_date__isnull=False)
        total_acknowledged_orders = acknowledged_orders.count()
        total_response_time = acknowledged_orders.aggregate(
        avg_response_time=Avg(ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=fields.DurationField())))['avg_response_time']
        self.average_response_time = total_response_time.total_seconds() if total_acknowledged_orders > 0 else 0.0

        successful_orders = self.purchaseorder_set.filter(status='completed', issue_date__isnull=False)
        total_orders = successful_orders.count()
        self.fulfillment_rate = (total_orders / self.purchaseorder_set.count() * 100) if total_orders > 0 else 0.0

        self.save()


    def __str__(self):
        return self.name



class PurchaseOrder(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    po_number = models.CharField(max_length=10, unique=True)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO {self.po_number} - {self.vendor.name}"


    

class HistorialPerformance(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"


