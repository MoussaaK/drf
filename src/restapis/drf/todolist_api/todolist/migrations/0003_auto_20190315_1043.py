# Generated by Django 2.1.7 on 2019-03-15 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20190315_1014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('id', 'date')},
        ),
    ]
