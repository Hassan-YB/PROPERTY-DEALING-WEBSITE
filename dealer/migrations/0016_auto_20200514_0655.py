# Generated by Django 3.0.4 on 2020-05-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0015_auto_20200514_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='Price_unit',
        ),
        migrations.AddField(
            model_name='property',
            name='Price_Unit',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
