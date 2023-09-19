from django.contrib import admin
from .models import Stock
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class JsonStockAdmin(ImportExportModelAdmin):
    list_display = ['trade_code', 'date', 'open', 'high', 'low', 'close', 'volume']
    list_display_links = ('trade_code',)
    
    
admin.site.register(Stock,JsonStockAdmin)

