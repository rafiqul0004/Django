# Generated by Django 4.2.7 on 2023-12-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_album_album_relese_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='rattings',
        ),
        migrations.AddField(
            model_name='album',
            name='ratings',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]
