from django.shortcuts import render
from .serializers import StockSerializer
from .models import Stock
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response




#pagination 
class LargeStockSetPagination(PageNumberPagination):
    page_size = 100
    page_query_param = 'page'


# Create your views here.
# class StockListView(generics.ListAPIView):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
#     pagination_class = 

class StockListView(generics.ListAPIView):
    serializer_class = StockSerializer
    pagination_class = LargeStockSetPagination

    def get_queryset(self):
        queryset = Stock.objects.all()
        selected_trade_code = self.request.query_params.get('trade_code')
        
        # Apply filter if trade code is provided in the request
        if selected_trade_code:
            queryset = queryset.filter(trade_code=selected_trade_code)
        
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            
            # Extract date, close, and volume data from the paginated queryset
            date_data = [str(stock.date) for stock in page]
            date_data = sorted(date_data)
            close_data = [str(stock.close) for stock in page]
            volume_data = [str(stock.volume) for stock in page]
            
            # Extract distinct trade_data from the paginated queryset
            trade_data = queryset.values_list('trade_code', flat=True).distinct()
            
            response_data = {
                'dateData': date_data,
                'closeData': close_data,
                'volumeData': volume_data,
                'tradeData': trade_data,
                'stocks': serializer.data,
            }
            
            return self.get_paginated_response(response_data)

        serializer = self.get_serializer(queryset, many=True)

        # Extract date, close, and volume data from the queryset
        date_data = [str(stock.date) for stock in queryset]
        date_data = sorted(date_data)
        print(date_data.count)
        close_data = [str(stock.close) for stock in queryset]
        volume_data = [str(stock.volume) for stock in queryset]
        
        # Extract distinct trade_data from the queryset
        trade_data = queryset.values_list('trade_code', flat=True).distinct()

        response_data = {
            'dateData': date_data,
            'closeData': close_data,
            'volumeData': volume_data,
            'tradeData': trade_data,
            'stocks': serializer.data,
        }

        return Response(response_data)
    
    
#create view 
class StockCreateView(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

#update view 
class StockUpdateView(generics.UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
    
#destroy view 
class StockDestroyView(generics.DestroyAPIView):
    queryset  = Stock.objects.all()
    serializer_class = StockSerializer
    
    
    



    


