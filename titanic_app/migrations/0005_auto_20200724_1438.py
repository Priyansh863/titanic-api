# Generated by Django 2.2.5 on 2020-07-24 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titanic_app', '0004_auto_20200724_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titanic',
            old_name='PassangerId',
            new_name='PassengerId',
        ),
    ]
