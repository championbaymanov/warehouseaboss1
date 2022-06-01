from django.urls import path
from . views import *

urlpatterns = [
    path('product-list-create/', ProductListCreateAPIView.as_view()),
    path('warehouse-list-create/', WarehouseListCreateAPIView.as_view()),
    path('product-list/', ProductListAPIView.as_view()),

    
    

]