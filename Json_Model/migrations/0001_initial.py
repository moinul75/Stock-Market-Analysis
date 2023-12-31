# Generated by Django 4.2.5 on 2023-09-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_code', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('open', models.CharField(max_length=20)),
                ('high', models.CharField(max_length=20)),
                ('low', models.CharField(max_length=20)),
                ('close', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=20)),
            ],
        ),
    ]
