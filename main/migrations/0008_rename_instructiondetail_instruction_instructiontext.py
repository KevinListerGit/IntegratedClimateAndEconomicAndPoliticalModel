# Generated by Django 4.0.3 on 2022-04-05 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_instruction_rename_todolist_item_todolist_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instruction',
            old_name='InstructionDetail',
            new_name='InstructionText',
        ),
    ]
