# Generated by Django 3.1.3 on 2021-01-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20210119_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]