# Generated by Django 2.1.8 on 2019-05-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
