from django.urls import path 
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('add-stock',views.addStock,name='add_stock'),
    path('update/<int:stock_data>',views.updateStockData,name='stock_update'),
    path('delete/<int:stock_data>/',views.deleteStockData,name='stock_delete'),
]
