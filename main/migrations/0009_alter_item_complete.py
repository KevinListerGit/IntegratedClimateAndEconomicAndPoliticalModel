# Generated by Django 4.0.3 on 2022-04-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_instructiondetail_instruction_instructiontext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='complete',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
