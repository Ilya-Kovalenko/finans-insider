from django.db import models
import enum


class Quotation(models.Model):
    units = models.BigIntegerField(null=True, blank=True, verbose_name="Целая часть суммы, может быть отрицательным "
                                                                       "числом")
    nano = models.IntegerField(null=True, blank=True, verbose_name="Дробная часть суммы, может быть отрицательным "
                                                                   "числом")


class MoneyValue(models.Model):
    currency = models.CharField(max_length=20, null=True, blank=True, verbose_name="Строковый ISO-код валюты")
    units = models.BigIntegerField(null=True, blank=True, verbose_name="Целая часть суммы, может быть отрицательным "
                                                                       "числом")
    nano = models.IntegerField(null=True, blank=True, verbose_name="Дробная часть суммы, может быть отрицательным "
                                                                   "числом")


class ShareType(enum.Enum):

    SHARE_TYPE_UNSPECIFIED = {
        'number': 0,
        'description': 'Значение не определено.'
        }
    SHARE_TYPE_COMMON = {
        'number': 1,
        'description': 'Обыкновенная'
        }
    SHARE_TYPE_PREFERRED = {
        'number': 2,
        'description': 'Привилегированная'
        }
    SHARE_TYPE_ADR = {
        'number': 3,
        'description': 'Американские депозитарные расписки'
        }
    SHARE_TYPE_GDR = {
        'number': 4,
        'description': 'Глобальные депозитарные расписки'
        }
    SHARE_TYPE_MLP = {
        'number': 5,
        'description': 'Товарищество с ограниченной ответственностью'
        }
    SHARE_TYPE_NY_REG_SHRS = {
        'number': 6,
        'description': 'Акции из реестра Нью-Йорка'
        }
    SHARE_TYPE_CLOSED_END_FUND = {
        'number': 7,
        'description': 'Закрытый инвестиционный фонд'
        }
    SHARE_TYPE_REIT = {
        'number': 8,
        'description': 'Траст недвижимости'
        }

    def __init__(self, vals):
        self.number = vals['number']
        self.description = vals['description']


class CommonInfo(models.Model):
    figi = models.CharField(max_length=12, null=True, blank=True, verbose_name="Figi-идентификатор инструмента.")
    ticker = models.CharField(max_length=12, null=True, blank=True, verbose_name="Тикер инструмента.")
    class_code = models.CharField(max_length=20, null=True, blank=True, verbose_name="Класс-код (секция торгов).")
    isin = models.CharField(max_length=12, null=True, blank=True, verbose_name="Isin-идентификатор инструмента.")
    lot = models.IntegerField(null=True, blank=True, verbose_name="Лотность инструмента. Возможно совершение операций "
                                                                  "только на количества ценной бумаги, кратные "
                                                                  "данному параметру.")
    currency = models.CharField(max_length=20, null=True, blank=True, verbose_name="Валюта расчётов.")
    klong = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related_klong",
                              null=True, blank=True, verbose_name="Коэффициент ставки риска длинной позиции по "
                                                                  "инструменту.")
    kshort = models.ForeignKey(Quotation, on_delete=models.CASCADE,
                               related_name="%(app_label)s_%(class)s_related_kshort", null=True, blank=True,
                               verbose_name="Коэффициент ставки риска короткой позиции по инструменту.")
    dlong = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related_dlong",
                              null=True, blank=True, verbose_name="Ставка риска минимальной маржи в лонг.")
    dshort = models.ForeignKey(Quotation, on_delete=models.CASCADE,
                               related_name="%(app_label)s_%(class)s_related_dshort", null=True, blank=True,
                               verbose_name="Ставка риска минимальной маржи в шорт.")
    dlong_min = models.ForeignKey(Quotation, on_delete=models.CASCADE,
                                  related_name="%(app_label)s_%(class)s_related_dlong_min", null=True, blank=True,
                                  verbose_name="Ставка риска начальной маржи в лонг.")
    dshort_min = models.ForeignKey(Quotation, on_delete=models.CASCADE,
                                   related_name="%(app_label)s_%(class)s_related_dshort_min", null=True, blank=True,
                                   verbose_name="Ставка риска начальной маржи в шорт.")
    short_enabled_flag = models.BooleanField(null=True, blank=True, verbose_name="Признак доступности для операций в "
                                                                                 "шорт.")
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="Название инструмента.")
    exchange = models.CharField(max_length=30, null=True, blank=True, verbose_name="Торговая площадка.")
    nominal = models.ForeignKey(MoneyValue, on_delete=models.CASCADE,
                                related_name="%(app_label)s_%(class)s_related_nominal", null=True, blank=True,
                                verbose_name="Номинал.")
    country_of_risk = models.CharField(max_length=10, null=True, blank=True,
                                       verbose_name="Код страны риска, т.е. страны, в которой компания ведёт "
                                                    "основной бизнес.")
    country_of_risk_name = models.CharField(max_length=30, null=True, blank=True,
                                            verbose_name="Наименование страны риска, т.е. страны, в которой компания "
                                                         "ведёт основной бизнес.")
    trading_status = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Текущий режим торгов "
                                                                                          "инструмента.")
    otc_flag = models.BooleanField(null=True, blank=True, verbose_name="Признак внебиржевой ценной бумаги.")
    buy_available_flag = models.BooleanField(null=True, blank=True, verbose_name="Признак доступности для покупки.")
    sell_available_flag = models.BooleanField(null=True, blank=True, verbose_name="Признак доступности для продажи.")
    iso_currency_name = models.CharField(max_length=3, null=True, blank=True, verbose_name="Строковый ISO-код валюты.")
    min_price_increment = models.ForeignKey(Quotation, on_delete=models.CASCADE,
                                            related_name="%(app_label)s_%(class)s_related_min_price_increment",
                                            null=True, blank=True, verbose_name="Шаг цены.")
    api_trade_available_flag = models.BooleanField(null=True, blank=True, verbose_name="Признак доступности торгов "
                                                                                       "через API.")

    class Meta:
        abstract = True


class Bond(CommonInfo):
    coupon_quantity_per_year = models.IntegerField(null=True, blank=True,
                                                   verbose_name="Количество выплат по купонам в год.")
    maturity_date = models.PositiveIntegerField(null=True, blank=True,
                                                verbose_name="Дата погашения облигации в часовом поясе UTC.")
    state_reg_date = models.PositiveIntegerField(null=True, blank=True,
                                                 verbose_name="Дата выпуска облигации в часовом поясе UTC.")
    placement_date = models.PositiveIntegerField(null=True, blank=True,
                                                 verbose_name="Дата размещения в часовом поясе UTC.")
    placement_price = models.ForeignKey(MoneyValue, on_delete=models.CASCADE,
                                        related_name="%(app_label)s_%(class)s_related_placement_price",
                                        null=True, blank=True, verbose_name="Цена размещения.")
    aci_value = models.ForeignKey(MoneyValue, on_delete=models.CASCADE,
                                  related_name="%(app_label)s_%(class)s_related_aci_value", null=True,
                                  blank=True, verbose_name="Значение НКД (накопленного купонного дохода) на дату.")
    sector = models.CharField(max_length=30, null=True, blank=True, verbose_name="Сектор экономики.")
    issue_kind = models.CharField(max_length=15, null=True, blank=True,
                                  verbose_name="Форма выпуска. Возможные значения:\n"
                                               "documentary — документарная;\n"
                                               "non_documentary — бездокументарная.")
    issue_size = models.BigIntegerField(null=True, blank=True, verbose_name="Размер выпуска.")
    issue_size_plan = models.BigIntegerField(null=True, blank=True, verbose_name="Плановый размер выпуска.")
    floating_coupon_flag = models.BooleanField(null=True, blank=True,
                                               verbose_name="Признак облигации с плавающим купоном.")
    perpetual_flag = models.BooleanField(null=True, blank=True, verbose_name="Признак бессрочной облигации.")
    amortization_flag = models.BooleanField(null=True, blank=True,
                                            verbose_name="Признак облигации с амортизацией долга.")

    class Meta:
        verbose_name = "Облигация"
        verbose_name_plural = "Облигации"


class Currency(CommonInfo):
    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Etf(CommonInfo):
    fixed_commission = models.ForeignKey(Quotation, on_delete=models.CASCADE,
                                         related_name="%(app_label)s_%(class)s_related_fixed_commission",
                                         null=True, blank=True, verbose_name="Размер фиксированной комиссии фонда.")
    focus_type = models.CharField(max_length=22, null=True, blank=True, verbose_name="""
focus_type\n
Возможные значения:\n
equity - акции;\n
fixed_income - облигации;\n
mixed_allocation - смешанный;\n
money_market - денежный рынок;\n
real_estate - недвижимость;\n
commodity - товары;\n
specialty - специальный;\n
private_equity - private equity;\n
alternative_investment - альтернативные инвестиции.""")
    released_date = models.PositiveIntegerField(null=True, blank=True, verbose_name="Дата выпуска в часовом поясе UTC.")
    num_shares = models.ForeignKey(Quotation, on_delete=models.CASCADE,
                                   related_name="%(app_label)s_%(class)s_related_num_shares", null=True,
                                   blank=True, verbose_name="Количество акций фонда в обращении.")
    sector = models.CharField(max_length=30, null=True, blank=True, verbose_name="Сектор экономики.")
    rebalancing_freq = models.CharField(max_length=20, null=True, blank=True, verbose_name="Частота ребалансировки.")

    class Meta:
        verbose_name = "Инвестиционный фонд"
        verbose_name_plural = "Инвестиционные фонды"


class Share(CommonInfo):
    ipo_date = models.PositiveIntegerField(null=True, blank=True, verbose_name="Дата IPO акции в часовом поясе UTC.")
    issue_size = models.BigIntegerField(null=True, blank=True, verbose_name="Размер выпуска.")
    sector = models.CharField(max_length=30, null=True, blank=True, verbose_name="Сектор экономики.")
    issue_size_plan = models.BigIntegerField(null=True, blank=True, verbose_name="Плановый размер выпуска.")
    div_yield_flag = models.BooleanField(null=True, blank=True, verbose_name="Признак наличия дивидендной доходности.")
    share_type = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Тип акции. Возможные "
                                                                                      "значения: ShareType")

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"


class HistoricCandle(models.Model):
    open = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related_open",
                             null=True, blank=True, verbose_name="Цена открытия за 1 лот.")
    high = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related_high",
                             null=True, blank=True, verbose_name="Максимальная цена за 1 лот.")
    low = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related_low",
                            null=True, blank=True, verbose_name="Минимальная цена за 1 лот.")
    close = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related_close",
                              null=True, blank=True, verbose_name="Цена закрытия за 1 лот.")
    volume = models.BigIntegerField(null=True, blank=True, verbose_name="Объём торгов в лотах.")
    time = models.PositiveIntegerField(null=True, blank=True, verbose_name="Время свечи в часовом поясе UTC")
    is_complete = models.BooleanField(null=True, blank=True, verbose_name="Признак завершённости свечи. false значит, "
                                                                          "свеча за текущие интервал ещё сформирована "
                                                                          "не полностью.")

    class Meta:
        verbose_name = "Информация о свече"
        verbose_name_plural = "Информация о свечах"
