# Generated by Django 3.1.2 on 2020-10-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mat',
            name='nom',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='prod',
            name='nom',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
