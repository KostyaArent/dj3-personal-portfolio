# Generated by Django 3.2.12 on 2022-04-02 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20220402_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='facts',
            new_name='fact',
        ),
        migrations.RenameField(
            model_name='developer',
            old_name='languages',
            new_name='language',
        ),
    ]
