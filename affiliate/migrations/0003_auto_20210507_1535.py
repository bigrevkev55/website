# Generated by Django 3.2 on 2021-05-07 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0002_auto_20210507_1521'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Boxers',
            new_name='Boxer',
        ),
        migrations.RenameModel(
            old_name='Fights',
            new_name='Fight',
        ),
        migrations.RenameModel(
            old_name='Styles',
            new_name='Style',
        ),
    ]
