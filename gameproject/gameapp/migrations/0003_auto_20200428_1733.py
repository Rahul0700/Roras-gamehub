# Generated by Django 3.0.3 on 2020-04-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0002_auto_20200428_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
