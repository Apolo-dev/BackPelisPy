# Generated by Django 3.2.5 on 2021-09-28 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMovie', '0002_auto_20210928_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['name_movie']},
        ),
    ]
