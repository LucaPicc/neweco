# Generated by Django 3.1.2 on 2020-10-21 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girsu', '0002_auto_20201020_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleos',
            name='f_carga',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='ggirsu',
            name='f_carga',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='girsu',
            name='f_corresp',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='recuperacion',
            name='f_carga',
            field=models.DateField(unique=True),
        ),
    ]
