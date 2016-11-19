from django.contrib import admin
from stockapi.models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

    
