# Generated by Django 3.0.3 on 2020-04-28 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0010_auto_20200428_2234'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visitors',
            new_name='Visitor',
        ),
    ]