# Generated by Django 2.1.4 on 2019-09-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20190927_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmaster',
            name='price',
            field=models.FloatField(),
        ),
    ]