from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  
from .models import Stock

class StockAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    list_display = ['trade_code', 'date', 'open', 'high', 'low', 'close', 'volume']
    list_display_links = ('trade_code',)

admin.site.register(Stock, StockAdmin)

