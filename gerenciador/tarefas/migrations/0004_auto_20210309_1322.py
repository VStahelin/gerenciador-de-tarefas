# Generated by Django 3.1.7 on 2021-03-09 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_auto_20210308_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='user',
            new_name='usuario',
        ),
    ]
