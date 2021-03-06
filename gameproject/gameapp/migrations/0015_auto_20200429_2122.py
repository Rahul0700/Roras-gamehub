# Generated by Django 3.0.3 on 2020-04-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0014_delete_choice1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerIp', models.CharField(max_length=254)),
                ('TimeofVisit', models.CharField(max_length=254)),
            ],
        ),
        migrations.RenameModel(
            old_name='UserFeedback',
            new_name='CustomerFeedback',
        ),
        migrations.DeleteModel(
            name='Visitor',
        ),
    ]
