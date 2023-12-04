from django.urls import path
from .views import (
    VendorCreateListView,
    VendorDetailView,
    PurchaseOrderListCreateView,
    PurchaseOrderDetailsView,
    VendorPerformanceview,
    AcknowledgePurchaseOrderView,
)

urlpatterns = [
    
    path('vendors/', VendorCreateListView.as_view(), name='vendor-list-create'), 
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
  
    
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailsView.as_view(), name='purchase-order-detail'),
    
    path('vendors/<int:pk>/performance/', VendorPerformanceview.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),
]
