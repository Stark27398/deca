# Generated by Django 2.1.4 on 2019-11-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20190930_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='templates',
            name='check',
            field=models.TextField(default=''),
        ),
    ]