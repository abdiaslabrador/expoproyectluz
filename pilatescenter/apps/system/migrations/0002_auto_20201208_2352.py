# Generated by Django 3.0.7 on 2020-12-09 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='description',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='name',
        ),
        migrations.AddField(
            model_name='exercise',
            name='delta_day',
            field=models.IntegerField(default=0),
        ),
    ]
