# Generated by Django 2.1.8 on 2019-05-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190511_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
