# Generated by Django 4.2.7 on 2023-12-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbankaccount',
            name='bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]