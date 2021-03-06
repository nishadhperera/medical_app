# Generated by Django 2.1.8 on 2019-05-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_of_birth', models.DateField(default=None)),
                ('email', models.EmailField(max_length=100)),
                ('mobile_number', models.CharField(max_length=20)),
                ('specialization', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='created_on',
            field=models.DateField(auto_now=True),
        ),
    ]
