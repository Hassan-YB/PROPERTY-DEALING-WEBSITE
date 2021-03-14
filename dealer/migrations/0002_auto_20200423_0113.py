# Generated by Django 3.0.4 on 2020-04-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='name',
            new_name='Type',
        ),
        migrations.RenameField(
            model_name='citie',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='name',
            new_name='Discount',
        ),
        migrations.RemoveField(
            model_name='bathroom',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bedroom',
            name='name',
        ),
        migrations.AddField(
            model_name='bathroom',
            name='Number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bedroom',
            name='Number',
            field=models.IntegerField(default=0),
        ),
    ]