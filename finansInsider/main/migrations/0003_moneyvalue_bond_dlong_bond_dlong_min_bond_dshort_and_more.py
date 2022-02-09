# Generated by Django 4.0.2 on 2022-02-09 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bond_currency_etf_quotation_share_delete_bonds_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=20)),
                ('units', models.BigIntegerField()),
                ('nano', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bond',
            name='dlong',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bond_dlong', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='dlong_min',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bond_dlong_min', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='dshort',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bond_dshort', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='dshort_min',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bond_dshort_min', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='kshort',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bond_kshort', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='min_price_increment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bond_min_price_increment', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='dlong',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currency_dlong', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='dlong_min',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currency_dlong_min', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='dshort',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currency_dshort', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='dshort_min',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currency_dshort_min', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='klong',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currency_klong', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='kshort',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currency_kshort', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='min_price_increment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currency_min_price_increment', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etf',
            name='dlong',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='etf_dlong', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etf',
            name='dlong_min',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='etf_dlong_min', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etf',
            name='dshort',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='etf_dshort', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etf',
            name='dshort_min',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='etf_dshort_min', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etf',
            name='fixed_commission',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='etf_fixed_commission', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etf',
            name='klong',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='etf_klong', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etf',
            name='kshort',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='etf_kshort', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etf',
            name='min_price_increment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='etf_min_price_increment', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etf',
            name='num_shares',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='etf_num_shares', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='dlong',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='share_dlong', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='dlong_min',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='share_dlong_min', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='dshort',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='share_dshort', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='dshort_min',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='share_dshort_min', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='klong',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='share_klong', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='kshort',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='share_kshort', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='min_price_increment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='share_min_price_increment', to='main.quotation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bond',
            name='klong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bond_klong', to='main.quotation'),
        ),
        migrations.AddField(
            model_name='bond',
            name='aci_value',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bond_aci_value', to='main.moneyvalue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='nominal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bond_nominal', to='main.moneyvalue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='placement_price',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bond_placement_price', to='main.moneyvalue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='nominal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='currency_nominal', to='main.moneyvalue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='nominal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='share_nominal', to='main.moneyvalue'),
            preserve_default=False,
        ),
    ]
