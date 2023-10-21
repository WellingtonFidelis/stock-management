from django.contrib import admin
from stock_management.models import Stock, Category
from stock_management.forms import StockCreateForm


# Register your models here.


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ["category", "item_name", "quantity"]
    form = StockCreateForm
    list_filter = ["category"]
    search_fields = ["category", "item_name"]
    readonly_fields = ["last_updated", "created_date"]


admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
