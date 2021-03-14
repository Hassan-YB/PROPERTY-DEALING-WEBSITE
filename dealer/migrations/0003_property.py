# Generated by Django 3.0.4 on 2020-05-01 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0002_auto_20200423_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.ImageField(upload_to='')),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Area', to='dealer.Area')),
                ('Bathrooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Bathroom', to='dealer.Bathroom')),
                ('Bedrooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Bedroom', to='dealer.Bedroom')),
                ('Categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Categorie', to='dealer.Categorie')),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='City', to='dealer.Citie')),
                ('Offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Offer', to='dealer.Offer')),
            ],
        ),
    ]