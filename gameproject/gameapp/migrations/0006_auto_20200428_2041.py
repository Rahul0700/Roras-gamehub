# Generated by Django 3.0.3 on 2020-04-28 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0005_auto_20200428_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfeedback',
            old_name='voice',
            new_name='feedback',
        ),
    ]
