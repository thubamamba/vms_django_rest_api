# Generated by Django 2.2.16 on 2023-10-11 23:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20231011_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
