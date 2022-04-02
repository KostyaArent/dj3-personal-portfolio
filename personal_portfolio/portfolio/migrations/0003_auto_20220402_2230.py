# Generated by Django 3.2.12 on 2022-04-02 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_developer_facts_proglanguages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='facts',
        ),
        migrations.AddField(
            model_name='developer',
            name='facts',
            field=models.ManyToManyField(to='portfolio.Facts'),
        ),
        migrations.RemoveField(
            model_name='developer',
            name='languages',
        ),
        migrations.AddField(
            model_name='developer',
            name='languages',
            field=models.ManyToManyField(to='portfolio.ProgLanguages'),
        ),
    ]