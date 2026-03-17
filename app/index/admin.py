from django.contrib import admin
from .models import Cow, MilkYield, ProductionSummary

@admin.register(Cow)
class CowAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name', 'breed', 'parity', 'status')
    search_fields = ('tag', 'name', 'breed')
    list_filter = ('status', 'breed')

@admin.register(MilkYield)
class MilkYieldAdmin(admin.ModelAdmin):
    list_display = ('cow', 'date', 'morning', 'evening', 'total', 'recorded_by')
    list_filter = ('date',)
    search_fields = ('cow__tag', 'cow__name')

@admin.register(ProductionSummary)
class ProductionSummaryAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_liters')