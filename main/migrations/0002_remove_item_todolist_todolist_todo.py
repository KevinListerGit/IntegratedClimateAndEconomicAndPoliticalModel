# Generated by Django 4.0.3 on 2022-04-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='todolist',
        ),
        migrations.AddField(
            model_name='todolist',
            name='ToDo',
            field=models.ManyToManyField(blank=True, to='main.item'),
        ),
    ]
