from django.urls import path 
from .views import StockListView,StockCreateView,StockUpdateView,StockDestroyView



urlpatterns = [
    path('stock_list/',StockListView.as_view(),name='stock_view'),
    path('stock_create',StockCreateView.as_view(),name='stock_create'),
    path('update_stock/<int:pk>/',StockUpdateView.as_view(),name='stock_update2'),
    path('stock_destroy/<int:pk>/',StockDestroyView.as_view(),name='stock_destroy'),
    
]
