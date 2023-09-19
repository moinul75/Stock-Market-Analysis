from django.http import JsonResponse
from django.shortcuts import render,Http404,redirect
from .models import Stock
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import StockForm
from django.contrib import messages 



def home(request):
    selected_trade_code = request.GET.get('trade_code')
    records_per_page = 100  
    page_number = request.GET.get('page', 1)

    try:
        page_number = int(page_number)  
    except ValueError:
        raise Http404("Invalid page number")

    if page_number < 1:
        raise Http404("Invalid page number")

    # Create a Paginator instance with ordered queryset
    paginator = Paginator(Stock.objects.order_by('id'), records_per_page)
    
    try:
        stocks = paginator.page(page_number)
        first_stock = stocks[0]  
        # print(first_stock.date)
    except PageNotAnInteger:
        raise Http404("Invalid page number")
    except EmptyPage:
        raise Http404(f"Page {page_number} not found. You have {paginator.num_pages} pages available.")
    
   # Extract date, close, and volume data directly from the paginated queryset
    # Extract date, close, and volume data from the queryset 'stocks'
    date_data = [str(stock.date) for stock in stocks]
    #sort data with date wise
    date_data = sorted(date_data)
    close_data = [str(stock.close) for stock in stocks]
    volume_data = [str(stock.volume) for stock in stocks]
    trades_data = [str(stock.trade_code) for stock in stocks]
    #make distinct 
    trade_data = list(set(trades_data))
    
    
  

    # Create a context dictionary with the extracted data
    stock_data_context = {
        'dateData': date_data,
        'closeData': close_data,
        'volumeData': volume_data,
        'tradeData' : trade_data
    }
    
    
      # If a specific trade code is selected, filter the queryset by that trade code
    if selected_trade_code:
        stocks = Stock.objects.filter(trade_code=selected_trade_code).order_by('id')
        # Update the data based on the filtered queryset
        date_data = [str(stock.date) for stock in stocks]
        date_data = sorted(date_data)
        close_data = [str(stock.close) for stock in stocks]
        volume_data = [str(stock.volume) for stock in stocks]
        trade_data = [str(stock.trade_code) for stock in stocks]
        #for distinct only
        trade_data = list(set(trade_data))
        stock_data_context['dateData'] = date_data
        stock_data_context['closeData'] = close_data
        stock_data_context['volumeData'] = volume_data
        stock_data_context['tradeData'] = trade_data
    
    

    existing_context = {
        'stocks': stocks,
    }
    context = {**existing_context, **stock_data_context,'selectedTradeCode': selected_trade_code}

    return render(request, 'home.html', context)


def addStock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request,f"Stock Data Added Successfully..")
            return redirect('home')
        else:
            pass 
    else: 
        form = StockForm()
    context = {
        'form':form
    }
    return render(request,'addStock.html',context)



#update Stock data 
def updateStockData(request,stock_data):
    try: 
        #get the data  from id 
        stock_instance = Stock.objects.get(id=stock_data)
    except Stock.DoesNotExist : 
        pass 
    
    if request.method == 'POST':
        form = StockForm(request.POST,instance=stock_instance)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request,f"Stock Data Updated  Successfully..")
            return redirect('home')
        else:
            pass 
    else: 
        form = StockForm(instance=stock_instance)
    context = {
        'form':form
    }
    
    return render(request,'updatedStock.html',context)


def deleteStockData(request,stock_data):
    try:
        stock = Stock.objects.get(id=stock_data)
    except Stock.DoesNotExist:
        messages.error(request,f'Stock Data is not found..')
    #delete the data 
    stock.delete()
    messages.success(request,f"stock Deleted Successfully...")
    return JsonResponse({'message': 'Stock deleted successfully'})


def stock_data(request):
    # Query your Stock model to retrieve the required data
    # Replace this with your actual data retrieval logic
    stocks = Stock.objects.values('date', 'close', 'volume').order_by('date')
    
    #date data , 

    # Serialize the data to JSON
    data = {
        'dateData': [str(stock['date']) for stock in stocks],
        'closeData': [stock['close'] for stock in stocks],
        'volumeData': [stock['volume'] for stock in stocks],
    }
    
    return JsonResponse(data)
















