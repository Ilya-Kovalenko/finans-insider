from django.db import models


class Quotation:  # work in progress
    def __init__(self):
        self.units = models.IntegerField()
        self.nano = models.IntegerField()


class MoneyValue:  # work in progress
    def __init__(self):
        self.currency = models.CharField(max_length=10)
        self.units = models.IntegerField()
        self.nano = models.IntegerField()


class Bond(models.Model):
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
    nominal = MoneyValue
    state_reg_date = models.DateTimeField()
    placement_date = models.DateTimeField()
    placement_price = MoneyValue
    aci_value = MoneyValue
    country_of_risk = models.CharField(max_length=30)
    country_of_risk_name = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    issue_kind = models.CharField(max_length=15)
    issue_size = models.BooleanField()
    issue_size_plan = models.IntegerField()
    trading_status = models.IntegerField()
    otc_flag = models.BooleanField()
    buy_available_flag = models.BooleanField()
    sell_available_flag = models.BooleanField()
    floating_coupon_flag = models.BooleanField()
    perpetual_flag = models.BooleanField()
    amortization_flag = models.BooleanField()
    min_price_increment = Quotation()
    api_trade_available_flag = models.BooleanField()


class Currency(models.Model):
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
    nominal = MoneyValue
    country_of_risk = models.CharField(max_length=30)
    country_of_risk_name = models.CharField(max_length=30)
    trading_status = models.IntegerField()
    otc_flag = models.BooleanField()
    buy_available_flag = models.BooleanField()
    sell_available_flag = models.BooleanField()
    iso_currency_name = models.CharField(max_length=30)
    min_price_increment = Quotation()
    api_trade_available_flag = models.BooleanField()


class Etf(models.Model):
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
    fixed_commission = Quotation
    focus_type = models.CharField(max_length=20)
    released_date = models.DateTimeField()
    num_shares = Quotation
    country_of_risk = models.CharField(max_length=30)
    country_of_risk_name = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    rebalancing_freq = models.CharField(max_length=30)
    trading_status = models.IntegerField()
    otc_flag = models.BooleanField()
    buy_available_flag = models.BooleanField()
    sell_available_flag = models.BooleanField()
    min_price_increment = Quotation()
    api_trade_available_flag = models.BooleanField()


class Share(models.Model):
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
    ipo_date = models.DateTimeField()
    issue_size = models.IntegerField()
    country_of_risk = models.CharField(max_length=30)
    country_of_risk_name = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    issue_size_plan = models.IntegerField()
    nominal = MoneyValue
    trading_status = models.IntegerField()
    otc_flag = models.BooleanField()
    buy_available_flag = models.BooleanField()
    sell_available_flag = models.BooleanField()
    div_yield_flag = models.BooleanField()
    share_type = models.IntegerField()
    min_price_increment = Quotation()
    api_trade_available_flag = models.BooleanField()
