# Generated by Django 3.1.2 on 2020-10-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girsu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleos',
            name='f_carga',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ggirsu',
            name='f_carga',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='recuperacion',
            name='f_carga',
            field=models.DateField(),
        ),
    ]
