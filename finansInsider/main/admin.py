from django.contrib import admin
from .models import Bond, Quotation, MoneyValue

admin.site.register(Bond)
admin.site.register(Quotation)
admin.site.register(MoneyValue)
# Register your models here.
