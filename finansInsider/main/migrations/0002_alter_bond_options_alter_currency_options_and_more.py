# Generated by Django 4.0.2 on 2022-02-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bond',
            options={'verbose_name': 'Облигация', 'verbose_name_plural': 'Облигации'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Валюта', 'verbose_name_plural': 'Валюты'},
        ),
        migrations.AlterModelOptions(
            name='etf',
            options={'verbose_name': 'Инвестиционный фонд', 'verbose_name_plural': 'Инвестиционные фонды'},
        ),
        migrations.AlterModelOptions(
            name='historiccandle',
            options={'verbose_name': 'Информация о свече', 'verbose_name_plural': 'Информация о свечах'},
        ),
        migrations.AlterModelOptions(
            name='share',
            options={'verbose_name': 'Акция', 'verbose_name_plural': 'Акции'},
        ),
        migrations.AlterField(
            model_name='etf',
            name='focus_type',
            field=models.CharField(blank=True, max_length=22, null=True, verbose_name='\nfocus_type\n\nВозможные значения:\n\nequity - акции;\n\nfixed_income - облигации;\n\nmixed_allocation - смешанный;\n\nmoney_market - денежный рынок;\n\nreal_estate - недвижимость;\n\ncommodity - товары;\n\nspecialty - специальный;\n\nprivate_equity - private equity;\n\nalternative_investment - альтернативные инвестиции.'),
        ),
    ]
