# Generated by Django 2.2.16 on 2023-10-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]