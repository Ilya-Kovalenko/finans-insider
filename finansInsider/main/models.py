from django.db import models


class Quotation:
    def __init__(self):
        self.units = models.IntegerField()
        self.nano = models.IntegerField()


class Bonds(models.Model):
    figi = models.CharField(max_length=12)
    ticker = models.CharField(max_length=12)
    class_code = models.CharField(max_length=12)
    isin = models.CharField(max_length=12)
    lot = models.IntegerField()
    currency = models.CharField(max_length=12)
    klong = Quotation
    kshort = Quotation
    dlong = Quotation
    dshort = Quotation
    dlong_min = Quotation
    dshort_min = Quotation
    short_enabled_flag = models.BooleanField()
    name = models.CharField(max_length=20)
    exchange = models.CharField(max_length=20)
    coupon_quantity_per_year = models.IntegerField()
    maturity_date = models.DateTimeField()
    nominal =

    date = models.DateTimeField('date published')


