# Generated by Django 4.0.2 on 2022-02-08 19:59

from django.db import migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonds',
            name='klong',
            field=main.models.QuotationField(default=0, max_length=104),
            preserve_default=False,
        ),
    ]
