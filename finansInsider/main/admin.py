from django.contrib import admin
from .models import Bond, Quotation, MoneyValue, HistoricCandle, Etf

admin.site.register(Bond)
admin.site.register(Quotation)
admin.site.register(MoneyValue)
admin.site.register(HistoricCandle)
admin.site.register(Etf)
# Register your models here.
