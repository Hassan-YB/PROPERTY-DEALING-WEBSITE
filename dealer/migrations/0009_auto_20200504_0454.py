# Generated by Django 3.0.4 on 2020-05-03 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0008_auto_20200504_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bathroom',
            name='Number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bedroom',
            name='Number',
            field=models.CharField(max_length=50),
        ),
    ]
