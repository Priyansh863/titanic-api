# Generated by Django 2.2.5 on 2020-07-24 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titanic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='titanic',
            old_name='Sibsp',
            new_name='SibSp',
        ),
    ]