from django.contrib import admin
from django.contrib import admin
from .models import Company, BusinessUnit, Metric, MetricValue

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'sector', 'reporting_time')
    search_fields = ('name', 'sector')

@admin.register(BusinessUnit)
class BusinessUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'function', 'company')
    search_fields = ('name', 'function')
    list_filter = ('company',)

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(MetricValue)
class MetricValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'metric', 'business_unit', 'reporting_period', 'value', 'unit')
    search_fields = ('metric__name', 'business_unit__name')
    list_filter = ('reporting_period', 'metric__category')

``